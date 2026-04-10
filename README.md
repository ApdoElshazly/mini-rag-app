# mini-rag-app
This is a minimal implementation of the RAG model  for question answering.


## REQUIRMENTS 
pyton 3.10 or later
### install python using miniconda

1)Download and install miniconda from[here](https://www.anaconda.com/docs/getting-started/miniconda/install/overview)
2)create a new enviorment using the following  command :
```bash
$ conda create -n mini rag-app python=3.10 
```
3)Activate the enviroment using the following  command :
```bash
$ conda activate mini-rag-app

```
### (Optional) setup you command line interface for better readability
```bash
export PS1="\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ "
```
## Installation 
### Install requirements package
```bash
$ pip install -r requirements.txt
```
 ### Setup the enviorment variables 
 ```bash 
 $ cp .env.example .env 
 ```
 set your environment variables in the `.env` file. like `OPENAI_API_KEY` Value.
 ## Run the Fastapi Server
 ```bash
 $ uvicorn main:app --reload --host 0.0.0.0 --port 5000
 ```
 ## POSTMAN Colliction
 Download the POSTMAN Collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)