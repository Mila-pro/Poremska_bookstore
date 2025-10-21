from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Author, Publisher, Book
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer
import logging

logger = logging.getLogger(__name__)


class BookListCreate(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            logger.info(f"Book created: {book.title}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Book creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Book updated: {book.title}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        logger.info(f"Book deleted: {book.title}")
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorListCreate(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            logger.info(f"Author created: {author.name}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Author creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherListCreate(APIView):

    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            publisher = serializer.save()
            logger.info(f"Publisher created: {publisher.name}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Publisher creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
