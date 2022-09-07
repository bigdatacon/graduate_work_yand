
from django.urls import include, path
from rest_framework import routers
from polls import views

router = routers.DefaultRouter()
router.register(r'fileupload', views.FileuplViewSet)
router.register(r'filmwork', views.FilmWorkViewSet)
router.register(r'questions', views.QuestionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


######################  то что было до этого

from django.contrib import admin
# from django.urls import include, path

urlpatterns = [
    # path('polls/question/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

### Cтарое
# urlpatterns = [
#     path('polls/question/', include('polls.urls')),
#     path('polls/', include('polls.urls')),
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]