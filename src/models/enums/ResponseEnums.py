from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS="File validated succeeded"
    FILE_VALIDATED_FAILED="File validation failed"
    FILE_TYPE_NOT_SUPPORTED="File type not supported"
    FILE_SIZE_EXCEEDED="File size exceeded"
    FILE_UPLOAD_SUCCESS="File uploaded successfully"
    FILE_UPLOAD_FAILED="File upload failed"
    PROCESSING_SUCCESS="Processing Success"
    PROCESSING_FAILED="Processing Failed"
    

    