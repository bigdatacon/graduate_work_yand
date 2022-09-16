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
import os

#Загрука файлов через формы https://stackabuse.com/handling-file-uploads-with-django/
#https://github.com/erkarl/django-rest-framework-oauth2-provider-example/blob/master/apps/users/tests.py    - для тестов good
#https://www.django-rest-framework.org/api-guide/testing/
#, URLPatternsTestCase

class ConnectionTests(APITestCase):
    def setUp(self):
        # self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}
        self.path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files'
        self.fd = open('C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4'.encode('utf-8'), 'rb')
        self.url = '/filmwork/'
        self.url_long = "http://127.0.0.1:8000/filmwork/"
        # self.test_client  = FilmWork.objects.create(title="test_object", certificate = 'test_sertificate', files={'file_path': self.fd})  # - если грузить тут файл - не работает так, я не нашел как простым способом добавить файлы
        self.test_filmwork  = FilmWork.objects.create(title="test_object", certificate = 'test_sertificate')
        self.test_filmwork_id = self.test_filmwork.id
        print(f' eto self.test_client_id: {self.test_filmwork_id}, eto self.test_client : {self.test_filmwork.title}')
        self.files = {'file_path': self.fd}

    #1
    def test_connection_questions(self):
        """
        Ensure we can get access to the object .
        """
        response = self.client.get('/filmwork/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #
    # #2
    def test_connection(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.get('/polls/question/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #
    # #3
    def test_connection_by_id(self):
        """
        Ensure we can get object by id from table
        """
        response = self.client.get(f"{self.url}{self.test_filmwork_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #4
    def test_post_data(self):
        """
        Ensure we can create a new object in model .
        """
        data = {'question_text': 'DabApps', 'files' : self.files.get('file_path', None)}
        response = self.client.post('/questions/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.get().question_text, 'DabApps')


    #5
    def test_post_delete_data(self):
        # response = requests.post(self.url_long, {"title": "test", "certificate": "test"},
        #                          files={'file_path': self.fd})

        # response = self.client.post(f"{self.url}", {"title": "test", "certificate": "test"},
        #                          files=self.files)

        response = self.client.post(self.url, {"title": "test", "certificate": "test", "file_path": self.fd})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Answer is 201:
        id = response.json().get('id')
        # response = requests.delete(f"{self.url_long}{id}")
        response = self.client.delete(f"{self.url}{id}/")
        # print(f"Answer is {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # #6
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
            # response = requests.post("http://127.0.0.1:8000/filmwork/",
            #                          {'title': f"test_api_{i}", 'certificate': f"test_api_{i}"},
            #                          files={'file_path': file_path})

            response = self.client.post(self.url,
                                     {'title': f"test_api_{i}", 'certificate': f"test_api_{i}", 'file_path': file_path})
            # response = self.client.post(self.url_long,
            #                          {'title': f"test_api_{i}", 'certificate': f"test_api_{i}", 'file_path': file_path})
            print(f"Answer is with load_file_to_model {response.status_code}: {response.json()}")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            i += 1
    #
    # #7
    def test_can_update_film(self):
        # response = requests.put("http://127.0.0.1:8000/filmwork/c4563b47-e3a6-4ae0-a450-563901bde8e4/", {"title": "test_UPDATE", "certificate": "test"},
        #                          files={'file_path': self.fd})

        response = self.client.put(f'{self.url}{self.test_filmwork_id}/', {"title": "test_UPDATE", "certificate": "test", 'file_path': self.fd})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f'Answer after update : {response.json().get("title")}, send to update : {"test_UPDATE"}')

    def tearDown(self):
        self.fd.close()
        self.test_filmwork.delete()


