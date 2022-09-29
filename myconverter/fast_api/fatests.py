import requests
print('начат main')
# answer = requests.get("http://127.0.0.1:8001/api/v1/apitesting")
# answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi")
answer = requests.get("http://127.0.0.1:8001/api/v1/modelhandlerapi/get_model_object_by_id/?film_uuid=efc94832-a392-4d68-b117-f90b5080218d")
file_path_to_convert = answer.json().get('file_path')
print(f' eto answer one user: {answer.json()}, file_path_to_convert : {file_path_to_convert}')


converted_file_path = requests.post("http://127.0.0.1:8001/api/v1/modelhandlerapi/resize/?file_path_to_convert")
print(f' eto converted_file_path: {converted_file_path.json()}')
