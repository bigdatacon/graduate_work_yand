from django.urls import include, path
from rest_framework import routers
from polls import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'fileupload', views.FileuplViewSet)
router.register(r'filmwork', views.FilmWorkViewSet)

from django.contrib import admin
# from django.urls import include, path

urlpatterns = [
    # path('polls/question/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
