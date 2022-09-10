import requests
from rest_framework import status
# from .models import FilmWork
# from .views import FilmWorkViewSet
# print("Getting the list of all questions")
# ans = requests.get("http://127.0.0.1:8000/polls/question/")
# print(f"Answer is {ans.status_code}: {ans.json()}")
# print("Adding a new question")
# ans = requests.post("http://127.0.0.1:8000/polls/question/", json={'question_text': "New question"})
# print(f"Answer is {ans.status_code}: {ans.json()}")
#
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
#
# ans_file = requests.post("http://127.0.0.1:8000/questions/", {'question_text': "With file"}, files={'file_path': fd})
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")


### Пишу в модель для Фильмов - работает
# fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
# # fields = ['id', 'title', 'certificate', 'file_path']
#
# ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {'title' : "test_api", 'certificate': "test_api"}, files={'file_path': fd})
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")
#Пробую пример с гет запросом из теории
# from rest_framework.test import force_authenticate, APIRequestFactory
#
#
# factory = APIRequestFactory()
# user = FilmWork.objects.get(id='8f47c55a-e16a-42e5-a9f9-188fec5ed5de')
# view = FilmWorkViewSet.as_view()
#
# # Make an authenticated request to the view...
# request = factory.get('/filmwork/')
# force_authenticate(request, user=user)
# response = view(request)

# Проверяю методы putt, update, delete для модели FilmWork
# {
#     "id": "8f47c55a-e16a-42e5-a9f9-188fec5ed5de",
#     "title": "five",
#     "certificate": "f",
#     "file_path": "http://127.0.0.1:8000/film_works/bandicam_2022-09-02_11-44-41-932.mp4"
# },
# Сначала гет по ключу
# ans_file = requests.get("http://127.0.0.1:8000/filmwork/", {'id': '8f47c55a-e16a-42e5-a9f9-188fec5ed5de', 'title' : "five", 'certificate': "f"})
# ans_file = requests.get("http://127.0.0.1:8000/filmwork/8f47c55a-e16a-42e5-a9f9-188fec5ed5de")
# print(f"Answer is {ans_file.status_code}: {ans_file.json()}")



# cоздание и удаление  объекта работает
fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
ans_file = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"}, files={'file_path': fd})
print(f"Answer is {ans_file.status_code}: {ans_file.json()},  id : {ans_file.json().get('id')}")
#Answer is 201:
id = ans_file.json().get('id')
ans_file = requests.delete(f"http://127.0.0.1:8000/filmwork/{id}")
print(f"Answer is {ans_file.status_code}")
#Answer is 204


# update объекта
ans_file = requests.update(f"http://127.0.0.1:8000/filmwork/{id}",  {"title": "testupdate", "certificate": "test"}, files={'file_path': fd})
print(f"Answer is {ans_file.status_code}")
#Answer AttributeError: module 'requests' has no attribute 'update'
