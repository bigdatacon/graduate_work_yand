import logging

import uvicorn
from core.logger import LOGGING
from fastapi import FastAPI
from api import apitesting, modelhandlerapi
import requests


app = FastAPI()
app.include_router(apitesting.router, prefix='/api/v1/apitesting')
app.include_router(modelhandlerapi.router, prefix='/api/v1/modelhandlerapi')

def main() -> None:
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        log_config=LOGGING,
        log_level=logging.DEBUG,  # TODO set level through env var
    )


if __name__ == '__main__':
    main()
    print('начат main in main')
    # answer = requests.get("http://127.0.0.1:8001/api/v1/apitesting")
    # answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi")
    answer = requests.get(
        "http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=efc94832-a392-4d68-b117-f90b5080218d")
    file_path_to_convert = answer.json().get('file_path')
    print(f' eto answer one user: {answer.json()}, file_path_to_convert : {file_path_to_convert}')

    converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize/?file_path_to_convert")
    print(f' eto converted_file_path: {converted_file_path.json()}')