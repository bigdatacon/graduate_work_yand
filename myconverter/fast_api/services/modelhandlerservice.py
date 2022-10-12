from functools import lru_cache
from typing import List, Optional
from pathlib import Path
import requests
from typing import Optional
from rest_framework import status
import ffmpeg
import os
import time
import argparse
import uuid
import requests
from fastapi import UploadFile, File
from io import BytesIO


class ModelHandler:
    def __init__(self, model_url: str):
        self.model_url = model_url

    #0
    async def get_model_object(self):
        """
        Ensure we can get model objects
        """
        response = requests.get(f"{self.model_url}")
        return response.json()

    #1
    async def get_model_object_by_id(self, object_id : str):
        """
        Ensure we can get object by id from table
        """
        response = requests.get(f"{self.model_url}{object_id}")
        return response.json()

    #2
    # async def add_one_object_to_table(self, object_data: dict, file_path : Optional[str]= None): - СТАРОЕ
    #     try:
    #         fd = open(file_path.encode('utf-8'), 'rb')
    #         response = requests.post(f'{self.model_url}', object_data, files={'file_path': fd})
    #         assert  response.status_code == 201, 'not add object_data in function add_one_object_to_table'
    #         return response.json().get('id')
    #     except Exception as e:
    #         print(f'except in add_one_object_to_table : {e.args}')
    #         return False

    async def add_one_object_to_table(self, object_data: dict, file_path: UploadFile):
        try:
            response = requests.post(f'{self.model_url}', object_data, files={'file_path': file_path.file})
            if response.status_code != 201:
                print(response.json())
            return response.json().get('id')
        except Exception as e:
            print(f'except in add_one_object_to_table : {e.args}')
            raise

    async def add_one_object_to_table_no_docker(self, object_data: dict, file_path : Optional[str]= None):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5,
                       'fps': 1,
                       'film': film_to_convert_id}

        try:
            response = requests.post("http://127.0.0.1:8000/fileupload/", object_data,
                                     files={'file_path': file_path})
            print(f' in fileupload response.status_code, response.json() : {response.status_code, response.json()}')
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')


    #3
    async def delet_one_object_to_table(self, object_id: dict):
        try:
            response = requests.delete(f"{self.model_url}{object_id}")
            return True
        except Exception as e:
            print(f'except in delet_one_object_to_table : {e.args}')
            return False

    #4
    async def add_many_object_to_table(self, object_title: Optional[str] =None, object_certificate : Optional[str] =None,  path : Optional[str]=None):
        """
        Ensure we can create many new objects in model by loading many files from path.
        """
        try:
            files = []
            for p in Path(path).rglob('*'):

                file_path = str(p.parent) + p.name
                response = requests.post(f"{self.model_url}",
                                         {'title': f"{object_title}", 'certificate': f"{object_certificate}"},
                                         files={'file_path': file_path})
            return True
        except Exception as e:
            print(f'except in add_many_object_to_table : {e.args}')
            return False

    #5
    async def update_object_by_id(self, object_id : str,  object_data : dict = None,  file_path : Optional[str] = None):
        """
        Ensure we can update object by id.
        """
        try:
            if file_path:
                fd = open(file_path.encode('utf-8'), 'rb')
                response = requests.put(f"{self.model_url}{object_id}",
                                         object_data,
                                         files={'file_path': fd})
                return True
            else:
                response = requests.put(f"{self.model_url}{object_id}",
                                         object_data)

                return True

        except Exception as e:
            print(f'except in update_object_by_id : {e.args}')
            return False
        pass


    # def resize(self, output_file_name: str):
    #     stream =  ffmpeg.input(os.path.join("/usr", "src", "app", "тест.mp4"))
    #     stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
    #     stream = ffmpeg.output(stream, f"{output_file_name}.mp4")
    #     ffmpeg.run(stream)

    async def get_file_from_existing_object_by_id(self, object_id):
        object_data = self.get_model_object_by_id(object_id)
        file_path = object_data.get('file_path')
        file_id = object_data.get('id')
        return file_path, file_id

    # async def resize(self, input_file_path: str):
    #     file_path = input_file_path.split('/')[-1]
    #     output_file_path =  f"{uuid.uuid4()}"
    #     resp = requests.get(input_file_path)
    #     print(f'eto in resize resp.json : {resp.json()}')
    #     open(os.path.join("/fast_api_converter", file_path), "wb").write(resp.content)
    #     stream =  ffmpeg.input(os.path.join("/fast_api_converter", file_path))
    #     stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
    #     stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
    #     ffmpeg.run(stream)
    #     return f"{output_file_path}.mp4"

    async def resize(self, input_file_path: UploadFile, file_id: str):
        filename = input_file_path.filename
        file = input_file_path.file
        output_file_path = f"{uuid.uuid4()}"
        open("iterim_file.mp4", "wb").write(file.read())
        stream =  ffmpeg.input("iterim_file.mp4")
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
        ffmpeg.run(stream)


        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5,
                       'fps': 1, 'film': file_id}
        file_path_new_2 = open(f"{output_file_path}.mp4")
        try:
            response = requests.post(f'{MODEL_LINK}fileupload/', object_data, files={'file_path': file_path_new_2})
            if response.status_code != 201:
                print(response.json())
            return response.json().get('id')
        except Exception as e:
            print(f'except in add_one_object_to_table_fileupload in resize : {e.args}')
            raise

        return f"{output_file_path}.mp4", True

    async def resize_full(self, file_id: str):
        #1 load file from database
        # answer = requests.get(
        #     f"http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid={file_id}")

        # answer = requests.get(
        #     f"{API_LINK}get_model_object_by_id/?film_uuid={file_id}")

        # answer = requests.get(f'http://127.0.0.1:8000/filmwork/{file_id}/')
        # answer = requests.get(f'http://127.0.0.1:8000/filmwork/{file_id}/')
        print('first print in resize_full')
        answer = requests.get(f'http://django:8000/filmwork/{file_id}/')
        # answer = requests.get('http://django:8000/filmwork/9f4bc97f-917c-4f1d-b099-cd1d16ec7269/')

        # print(f'here answer.json for get_model_object_by_id : {answer.json()}')
        # print(
        #     f'here answer.json detail for get_model_object_by_id : {answer.json().get("file_path").replace("django", "127.0.0.1")}')
        # file_path_from_database = answer.json().get("file_path").replace('django', '127.0.0.1')

        # print(
        #     f'here answer.json detail for get_model_object_by_id : {answer.json().get("file_path")}')
        file_path_from_database = answer.json().get("file_path")
        print(f' eto file_path_from_database : {file_path_from_database}')

        r = requests.get(file_path_from_database, allow_redirects=True)
        output_file_path_from_database = f"{uuid.uuid4()}.mp4"
        open(output_file_path_from_database, 'wb').write(r.content)
        print('WRITE')

        #2 open file that was loaded from database
        print('WRITE in resize_full')
        fd = open(output_file_path_from_database, 'rb')
        output_file_path = f"{uuid.uuid4()}"

        #3 send opened file to resize and do resize
        # stream =  ffmpeg.input(fd)
        stream = ffmpeg.input(output_file_path_from_database)
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
        ffmpeg.run(stream)


        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5,
                       'fps': 1, 'film': file_id}
        #4 Open file after resize and try to load in fileupload
        file_path_new_2 = open(f"{output_file_path}.mp4", 'rb')

        try:
            response = requests.post(f'{MODEL_LINK}fileupload/', object_data, files={'file_path': file_path_new_2})
            if response.status_code != 201:
                print(response.json())
            return response.json().get('id')
        except Exception as e:
            print(f'except in add_one_object_to_table_fileupload in resize_full : {e.args}')
            raise

        return f"{output_file_path}.mp4", True


    async def create_object_for_converted_video(self, convert_video_path: str, convert_model, file_id):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1, 'film': file_id}
        # file_path_new_2 = os.path.join("/fast_api_converter", convert_video_path)
        # file_path_new_2 = open(file_path_new_2, 'rb')
        file_path_new_2  = open(convert_video_path)

        try:
            convert_model.add_one_object_to_table(object_data, file_path_new_2)
            file_path_new_2.close()
            return True
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
            return False

    # async def create_object_for_converted_video(self, convert_video_path:str, convert_model, file_id):
    #     object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1, 'film': file_id}
    #     file_path_new_2 = os.path.join("/usr", "src", "app", convert_video_path)
    #
    #     try:
    #         convert_model.add_one_object_to_table(object_data, file_path_new_2)
    #         return True
    #     except Exception as e:
    #         print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
    #         return False



MODEL_LINK = os.getenv('MODEL_LINK', 'http://127.0.0.1:8000/')
API_LINK = os.getenv('API_LINK', 'http://127.0.0.1:8001/api/v1/modelhandlerapi/')

# @lru_cache()
# def get_modelhandler_service() -> ModelHandler:
#     return ModelHandler('http://127.0.0.1:8000/filmwork/')


@lru_cache()
def get_modelhandler_service() -> ModelHandler:
    return ModelHandler(f'{MODEL_LINK}filmwork/')