from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='polls'),

    # path('questions/', views.QuestionViewSet), # добавил для вива запись чтобы проходился тест
    path('question/', views.question_list),
    path('question/<int:pk>/', views.question_detail),
]




### Cтарое
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('polls/question/', views.question_list),
#     path('polls/question/<int:pk>/', views.question_detail),
# ]