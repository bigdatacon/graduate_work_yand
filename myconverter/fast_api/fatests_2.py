import requests
import os
print('начат main')
import sys
import uuid

#1 скачиваю файл, путь до видео идет почему то c django - но так сеть не видит, поэтому делаю replace на 127.0.0.1
film_uuid="9f4bc97f-917c-4f1d-b099-cd1d16ec7269"
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=9f4bc97f-917c-4f1d-b099-cd1d16ec7269")
answer = requests.get(f"http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid={film_uuid}")
print(f'here answer.json for get_model_object_by_id : {answer.json().get("file_path").replace("django", "127.0.0.1")}')
file_path_from_database = answer.json().get("file_path").replace('django', '127.0.0.1')
output_file_path = f"{uuid.uuid4()}loaded.mp4"
# url = 'https://www.facebook.com/favicon.ico'
r = requests.get(file_path_from_database, allow_redirects=True)
open(f'./loaded/{output_file_path}', 'wb').write(r.content)
print('WRITE')



#2 закидываю полученный файл в resize
# file_path = os.path.join("./loaded", "dd9b7e11-4c4d-4af6-93cf-bc9e9d62ace6loaded.mp4")
file_path = os.path.join(f'./loaded/{output_file_path}')
fd = open(file_path, 'rb')
try:
    print(f'start resize')
    response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize/",
                             files={'input_file_path': fd})
    print(f"RESULT RESIZE ....")
    file_path_after_resize = response.json()
    print(file_path_after_resize)
except Exception as e:
    print(f'except in add_one_object_to_table : {e.args}')

fd.close()


#3 Закидываю файл полученный от resize в таблицу fileupload
try:
    open(f'./loaded_resize/loaded_resize{file_path_after_resize}', 'wb').write(file_path_after_resize)
except Exception as e:
    print(f' except in upload_to file_system after resize : {e.args}')

file_path = os.path.join(f'./loaded_resize/loaded_resize{file_path_after_resize}')
fd = open(file_path, 'rb')
object_data = {"resolution": "convert_video", "codec_name": "convert_videotest", 'display_aspect_ratio': 5, 'fps': 1,
               'film': film_uuid}
response = requests.post("http://127.0.0.1:8000/fileupload/", object_data,
                         files={'file_path': fd})

print(f' в тесте ответ после загрузки в fileupload: {response.status_code, response.json()}')


# try:
#     convert_model.add_one_object_to_table_no_docker(object_data, file_path_after_resize)
#     return True
# except Exception as e:
#     print(f'exception in create_object_for_converted_video, CAUSE : {e.args}')
#     return False
