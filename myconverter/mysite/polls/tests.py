from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Question
# from mysite.urls.py import  router
#https://www.django-rest-framework.org/api-guide/testing/

#Проверка что можно подключится к странице и получить статус код = HTTP_200_OK

from rest_framework.test import RequestsClient
client = RequestsClient()
# response = client.get('http://testserver/users/')
response = client.get('http://127.0.0.1:8000/polls/')
assert response.status_code == 200


# class ConnectionTests(APITestCase, URLPatternsTestCase):
class ConnectionTests(APITestCase):
    # urlpatterns = [
    #     # path('api/', include('api.urls')),
    #     # path('', include(router.urls)),
    #     path('polls/', include('polls.urls')),
    # ]

    def test_connection(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        # url = reverse('polls')
        #
        # response = self.client.get(url, format='json')
        response = self.client.get('/polls/question/', format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

    def test_post_data(self):
        """
        Ensure we can create a new object in model .
        """
        fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
        data = {'question_text': 'DabApps', 'files': {'file_path': fd}}
        response = self.client.post('/polls/question/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.get().question_text, 'DabApps')

