from pathlib import Path
import requests
from typing import Optional
from rest_framework import status
import ffmpeg
import os
import time
import argparse


class ModelHandler:
    def __init__(self, model_url: str):
        self.model_url = model_url

    #0
    def get_model_object(self):
        """
        Ensure we can get model objects
        """
        response = requests.get(f"{self.model_url}")
        return response.json()

    #1
    def get_model_object_by_id(self, object_id : str):
        """
        Ensure we can get object by id from table
        """
        response = requests.get(f"{self.model_url}{object_id}")
        return response.json()

    #2
    def add_one_object_to_table(self, object_data: dict, file_path : Optional[str]= None):
        try:
            fd = open(file_path.encode('utf-8'), 'rb')
            response = requests.post(f'{self.model_url}', object_data, files={'file_path': fd})
            assert  response.status_code == 201, 'not add object_data in function add_one_object_to_table'
            return response.json().get('id')
        except Exception as e:
            print(f'except in add_one_object_to_table : {e.args}')
            return False


    #3
    def delet_one_object_to_table(self, object_id: dict):
        try:
            response = requests.delete(f"{self.model_url}{object_id}")
            return True
        except Exception as e:
            print(f'except in delet_one_object_to_table : {e.args}')
            return False

    #4
    def add_many_object_to_table(self, object_title: Optional[str] =None, object_certificate : Optional[str] =None,  path : Optional[str]=None):
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
    def update_object_by_id(self, object_id : str,  object_data : dict = None,  file_path : Optional[str] = None):
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

    def get_file_from_existing_object_by_id(self, object_id):
        object_data = self.get_model_object_by_id(object_id)
        file_path = object_data.get('file_path')
        file_id = object_data.get('id')
        return file_path, file_id

    def resize(self, input_file_path: str , output_file_path: str):
        file_path = input_file_path.split('/')[-1]
        resp = requests.get(input_file_path)
        file_path = open(os.path.join("/usr", "src", "app", file_path), "wb").write(resp.content)
        stream =  ffmpeg.input(os.path.join("/usr", "src", "app", file_path))
        stream = stream.filter('fps', fps=5, round = 'up').filter('scale', w=128, h=128)
        stream = ffmpeg.output(stream, f"{output_file_path}.mp4")
        ffmpeg.run(stream)
        return os.listdir(".")[0]

    def create_object_for_converted_video(self, convert_video_path:str, convert_model, file_id):
        object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1, 'film': file_id}
        file_path_new_2 = os.path.join("/usr", "src", "app", convert_video_path)

        try:
            convert_model.add_one_object_to_table(object_data, file_path_new_2)
            return True
        except Exception as e:
            print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
            return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-host", type=str, default="127.0.0.1", help="Целевой хост")
    args = parser.parse_args()
    # if args.target_host == "127.0.0.1":
    #     print("base url ")
    api_base_url = f"http://{args.target_host}:8000/"
    # else:
    #     print("django url ")
    #     api_base_url = "http://django:8000/"


    #0 базовые параметры
    time.sleep(5)
    output_file_name = "NEW_MOVIE2.mp4"
    # object_id = "d90e9345-09c2-4d46-97a3-d6505b767f30"   # этот объект точно есть в модели
    # model = ModelHandler('http://django:8000/filmwork/')
    # convert_model = ModelHandler('http://django:8000/fileupload/')

    #use api_base_url
    model = ModelHandler(f'{api_base_url}filmwork/')
    convert_model = ModelHandler(f'{api_base_url}fileupload/')

# {
#     "id": "d90e9345-09c2-4d46-97a3-d6505b767f30",
#     "title": "test",
#     "certificate": "test",
#     "file_path": "http://127.0.0.1:8000/film_works/%D1%82%D0%B5%D1%81%D1%82_4c0oXm9.mp4"
# }
    #1 Cоздаю объект в модели FilmWork
    object_data = {"title": "test2", "certificate": "test2"}
    file_path_new_2 = os.path.join("/usr", "src", "app", "тест.mp4")
    object_id = model.add_one_object_to_table(object_data, file_path_new_2)

    #2 получаею путь до файла в докере из модели filmwork
    file_path_to_convert, film_to_convert_id = model.get_file_from_existing_object_by_id(object_id)

    #3 отправляю полученный путь на конвертацию и получаю имя сконвертированного файла в докер волюме
    converted_file_path = model.resize(file_path_to_convert, output_file_name)

    #4 заливаю видео в модели fileupload
    model.create_object_for_converted_video(converted_file_path, convert_model, film_to_convert_id)

