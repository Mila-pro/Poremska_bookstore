from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Author, Publisher, Book
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer



class BookListCreate(APIView):
    """Отримати список книг або додати нову"""

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)




class BookDetail(APIView):
    """Перегляд, редагування або видалення конкретної книги"""

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorListCreate(APIView):
    """Отримати список авторів або додати нового"""

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)



class PublisherListCreate(APIView):
    """Отримати список видавництв або додати нове"""

    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)
