from rest_framework import viewsets
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAdminUser


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAdminUser]
