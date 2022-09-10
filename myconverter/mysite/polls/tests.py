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

#https://www.django-rest-framework.org/api-guide/testing/
#, URLPatternsTestCase
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

    def test_connection_by_id(self):
        """
        Ensure we can get object by id from table
        """
        factory = APIRequestFactory()
        user = FilmWork.objects.get(id='8f47c55a-e16a-42e5-a9f9-188fec5ed5de')
        view = FilmWorkViewSet.as_view()

        # Make an authenticated request to the view...
        request = factory.get('/filmwork/')
        force_authenticate(request, user=user)
        response = view(request)
        print(f'here response in test_connection_by_id : {response}')

    def test_post_data(self):
        """
        Ensure we can create a new object in model .
        """
        fd = open("C:\\Yand_final_sprint\\myconverter\\mysite\\files\\тест.mp4", "rb")
        data = {'question_text': 'DabApps', 'files': {'file_path': fd}}
        response = self.client.post('/polls/question/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.get().question_text, 'DabApps')

    def test_post_many_files(self):
        """
        Ensure we can create many new objects in model by loading many files from path.
        """
        path = 'C:\\Yand_final_sprint\\myconverter\\mysite\\files'
        files = []
        i = 1
        for p in Path(path).rglob('*'):
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
