import requests
import os
print('начат main')
import sys

# answer = requests.get("http://127.0.0.1:8001/api/v1/apitesting")
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi")
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=efc94832-a392-4d68-b117-f90b5080218d")

#0 Внимание вот такой код точно добавляет данные в reqfile.py
#!!!! Вот такой путь не видит os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'files', 'тест.mp4')
object_data = {"title": "test", "certificate": "test"}

# title =  "test"
# certificate = "testcertificate"

title =  {"title": "test"}
certificate = {"certificate": "test"}

# file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'

file_path = os.path.join("..", "mysite", "files", "тест.mp4")

# print(f" eto file_path : {file_path}, eto  os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'files', 'тест.mp4') : {os.path.join('C:', 'Yand_final_sprint', 'myconverter', 'mysite', 'files', 'тест.mp4')}")
fd = open(file_path, 'rb')

response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
                         files={'file_path': fd})
print(f' в тесте fatests : {response.status_code, response.json()}')





#1добавляю объект в базу через API
#ниже пробные не рабочие примеры
# object_data = {"title": "test_api", "certificate": "test_api3009", 'file_path' :fd}
# object_data = {"title": "test_api", "certificate": "test_api3009", 'file_path' :file_path}

try:
    # response = requests.get(f"http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/?object_data={object_data}&file_path={fd}")
    # response = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/?object_data=object_data&file_path=fd")
    # response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/", json=object_data, files=fd)
    # response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/", object_data=object_data, file_path=file_path)
    # response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/", object_data, files={'file_path': fd})
    response = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/add_one_object_to_table/", title, certificate, files={'file_path': fd})
    if response.status_code != 201:
        print(f"Error ....")
        print(response.json())
        print(f' eto response from add_one_object_to_table : {response}')
        sys.exit(1)
except Exception as e:
    print(f'except in add_one_object_to_table : {e.args}')





# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=efc94832-a392-4d68-b117-f90b5080218d")
# file_path_to_convert = answer.json().get('file_path')
# file_path_to_convert_from_stroka_15 = 'http://127.0.0.1:8000/media/film_works/%D1%82%D0%B5%D1%81%D1%82_GI7BI9C.mp4'
# print(f' eto answer one user: {answer.json()}, file_path_to_convert : {file_path_to_convert} , {file_path_to_convert_from_stroka_15}')
#
#
# converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize/?file_path_to_convert")
# print(f' eto converted_file_path: {converted_file_path.json()}')
#
#
# converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize/?file_path_to_convert_from_stroka_15")
# print(f' eto converted_file_path_from_stroka_15: {converted_file_path.json()}')
#
#
#
# #II resize_no_docker
# converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize_no_docker/?file_path_to_convert")
# print(f' eto converted_file_path: {converted_file_path.json()}')
#
#
# converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize_no_docker/?file_path_to_convert_from_stroka_15")
# print(f' eto converted_file_path_from_stroka_15: {converted_file_path.json()}')
