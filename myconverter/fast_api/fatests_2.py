import requests
import os
print('начат main')
import sys
import uuid

#1 скачиваю файл, путь до видео идет почему то c django - но так сеть не видит, поэтому делаю replace на 127.0.0.1
answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=9f4bc97f-917c-4f1d-b099-cd1d16ec7269")
print(f'here answer.json for get_model_object_by_id : {answer.json().get("file_path").replace("django", "127.0.0.1")}')
file_path_from_database = answer.json().get("file_path").replace('django', '127.0.0.1')
output_file_path = f"{uuid.uuid4()}loaded.mp4"
# url = 'https://www.facebook.com/favicon.ico'
r = requests.get(file_path_from_database, allow_redirects=True)
open(f'./loaded/{output_file_path}', 'wb').write(r.content)
print('WRITE')



#2 закидываю полученный файл в resize
file_path = os.path.join("./loaded", "ad25419c-1a29-4f38-b65e-a50fa8c62f1dloaded.mp4")
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

