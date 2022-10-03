from typing import List, Optional
from fastapi import APIRouter, Depends, Header, File, UploadFile
from services.modelhandlerservice import ModelHandler, get_modelhandler_service
import shutil

router = APIRouter()


@router.get("/")
async def get_model_object(
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.get_model_object()
    return result



@router.post("/add_one_object_to_table")
async def add_one_object_to_table(object_data: dict, file_path : Optional[str]= None,
        modelhandler_service: ModelHandler = Depends(get_modelhandler_service),
):
    result = await modelhandler_service.add_one_object_to_table(object_data, file_path)
    return result.json()


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