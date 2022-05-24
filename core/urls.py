from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, JournalViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('journals', JournalViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
