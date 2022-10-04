from typing import List, Optional
from fastapi import APIRouter, Depends, Header, File, UploadFile
from services.modelhandlerservice import ModelHandler, get_modelhandler_service
import shutil
from fastapi import Query, File, UploadFile

router = APIRouter()


@router.get("/")
async def get_model_object(
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object()
    return result



@router.post("/add_one_object_to_table")
async def add_one_object_to_table(
    file_path: UploadFile,
    title=Query(None, alias='title'),
    certificate=Query(None, alias='certificate'),
    modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    print(dir(file_path))
    print(file_path)
    print(file_path.filename)
    print(file_path.file)
    print(dir(file_path.file))
    result = await modelhandler_service.add_one_object_to_table({'title': title, 'certificate': certificate}, file_path=file_path)
    return result


@router.get("/get_model_object_by_id")
async def get_model_object_by_id(film_uuid,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object_by_id(film_uuid)
    return result


@router.post("/resize")
async def resize(input_file_path,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.resize(input_file_path)
    return result


@router.post("/resize_no_docker")
async def resize_no_docker(input_file_path,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.resize_no_docker(input_file_path)
    return result

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

@router.post("/upload_to")
async def root(file: UploadFile = File(...)):
    with open('test.mp4', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}