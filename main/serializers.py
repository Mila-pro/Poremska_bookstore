from rest_framework import serializers
from .models import Author, Publisher, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'country']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    author_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Author.objects.all(), source='author' 
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Publisher.objects.all(), source='publisher'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'price', 'genre', 'year', 'author_id', 'publisher_id']