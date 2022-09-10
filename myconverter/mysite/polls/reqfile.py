import requests
from .models import FilmWork
from .views import FilmWorkViewSet
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


# Проверяю методы putt, update, delete для модели FilmWork
# {
#     "id": "8f47c55a-e16a-42e5-a9f9-188fec5ed5de",
#     "title": "five",
#     "certificate": "f",
#     "file_path": "http://127.0.0.1:8000/film_works/bandicam_2022-09-02_11-44-41-932.mp4"
# },
# Сначала гет по ключу
ans_file = requests.get("http://127.0.0.1:8000/filmwork/", {'id': '8f47c55a-e16a-42e5-a9f9-188fec5ed5de', 'title' : "five", 'certificate': "f"})
print(f"Answer is {ans_file.status_code}: {ans_file.json()}")

#Пробую пример с гет запросом из теории
from rest_framework.test import force_authenticate, APIRequestFactory


factory = APIRequestFactory()
user = FilmWork.objects.get(id='8f47c55a-e16a-42e5-a9f9-188fec5ed5de')
view = FilmWorkViewSet.as_view()

# Make an authenticated request to the view...
request = factory.get('/filmwork/')
force_authenticate(request, user=user)
response = view(request)