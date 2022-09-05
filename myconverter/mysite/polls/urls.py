from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/question/', views.snippet_list),
    path('polls/question/<int:pk>/', views.question_detail),
]
