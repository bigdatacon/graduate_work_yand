from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Question, FilmWork, Fileupl
from  .views import FilmWorkViewSet
# from mysite.urls.py import  router
from rest_framework.test import force_authenticate, APIRequestFactory
from pathlib import Path
import requests


#https://github.com/erkarl/django-rest-framework-oauth2-provider-example/blob/master/apps/users/tests.py    - для тестов good
#https://www.django-rest-framework.org/api-guide/testing/
#, URLPatternsTestCase
class ConnectionTests(APITestCase):
    def setUp(self):
        # self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}
        self.path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files'
        self.fd = open('C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'.encode('utf-8'), 'rb')

    #1
    def test_connection_questions(self):
        """
        Ensure we can get access to the object .
        """
        response = self.client.get('/questions/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    #2
    def test_connection(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.get('/polls/question/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    #3
    def test_connection_by_id(self):
        """
        Ensure we can get object by id from table
        """
        response = requests.get("http://127.0.0.1:8000/filmwork/763af035-a450-4e62-931b-d59815c3d028")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #4
    # def test_post_data(self):
    #     """
    #     Ensure we can create a new object in model .
    #     """
    #     data = {'question_text': 'DabApps', 'files': {'file_path': self.fd}}
    #     # response = self.client.post('/polls/question/', data, format='json')
    #     response = self.client.post('/questions/', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Question.objects.get().question_text, 'DabApps')
    #

    #5
    def test_post_delete_data(self):
        response = requests.post("http://127.0.0.1:8000/filmwork/", {"title": "test", "certificate": "test"},
                                 files={'file_path': self.fd})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Answer is 201:
        id = response.json().get('id')
        response = requests.delete(f"http://127.0.0.1:8000/filmwork/{id}")
        # print(f"Answer is {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #6
    def test_post_many_files(self):
        """
        Ensure we can create many new objects in model by loading many files from path.
        """
        files = []
        i = 1
        for p in Path(self.path).rglob('*'):
            print(f' {i:} eto p : {str(p)}, type: {type(str(p))}')

            file_path = str(p.parent) + p.name
            print(f'eto file_path :')
            print(file_path)
            response = requests.post("http://127.0.0.1:8000/filmwork/",
                                     {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
                                     files={'file_path': file_path})
            print(f"Answer is with load_file_to_model {response.status_code}: {response.json()}")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            i += 1

    #7
    def test_can_update_film(self):
        # {
        #     "id": "c4563b47-e3a6-4ae0-a450-563901bde8e4",
        #     "title": "test_api_1",
        #     "certificate": "test_api_1",
        #     "file_path": "http://127.0.0.1:8000/film_works/file_path_3MbT583"
        # },
        response = requests.put("http://127.0.0.1:8000/filmwork/c4563b47-e3a6-4ae0-a450-563901bde8e4/", {"title": "test_UPDATE", "certificate": "test"},
                                 files={'file_path': self.fd})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f'Answer after update : {response.json().get("title")}, send to update : {"test_UPDATE"}')
