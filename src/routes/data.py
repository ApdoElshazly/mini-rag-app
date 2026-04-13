from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController,ProcessController
from models import ResponseSignal
from.schemes.data import ProcessRequest
import os
import aiofiles
import logging



logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings)
):

    # VALIDATE THE FILE PROPERTIES
    data_controller = DataController()
    is_valid, result_signal = data_controller.Validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"Signal": result_signal}
        )

    Project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path,file_id = data_controller.genrate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)

    except Exception as e:
        logger.error(f"Error uploading file: {e}")


        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"Signal": ResponseSignal.FILE_UPLOAD_FAILED.value, "Error": str(e)}
        )

    return JSONResponse(content={"Signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value, "FileID": file_id})



@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str,process_request:ProcessRequest):
    
    file_id=process_request.file_id
    chunk_size =process_request.chunk_size
    over_lap=process_request.over_lap
    process_controller=ProcessController(project_id=project_id)
    file_content=process_controller.get_file_content(file_id=file_id)
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=over_lap
    )

    if file_chunks is None or len(file_chunks)==0:
         return JSONResponse(
             
             status_code=status.HTTP_400_BAD_REQUEST,
             content={"Signal": ResponseSignal.PROCESSING_FAILED.value}
             )
    
    return file_chunks
       
