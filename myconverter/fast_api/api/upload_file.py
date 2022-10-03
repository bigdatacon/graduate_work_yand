from fastapi import File, UploadFile , APIRouter, FastAPI
import shutil
import requests
import os

router = APIRouter()
app = FastAPI()



# @router.post("/upload")
# def upload(file: UploadFile = File(...)):
#     try:
#         with open(file.filename, 'wb') as f:
#             shutil.copyfileobj(file.file, f)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()
#
#     return {"message": f"Successfully uploaded {file.filename}"}
#
# @app.post("/upload_to")
# async def root(file: UploadFile = File(...)):
#     with open('test.mp4', 'wb') as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {"file_name": file.filename}

# file_path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'

#I тестирование функции upload
file_path = str(os.path.join("..", "..", "mysite", "files", "тест.mp4"))
# url = 'http://127.0.0.1:8001/upload'
# file = {'file': open(file_path, 'rb')}
# resp = requests.post(url=url, files=file)
# print(resp.json())

#II тестирование функции root
url = 'http://127.0.0.1:8001/upload_to'
file = {'file': open(file_path, 'rb')}
resp = requests.post(url=url, files=file)
print(resp.json())