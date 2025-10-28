import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from main.models import Author, Publisher, Book

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(
        username='testuser',
        password='testpass123',
        email='test@example.com'
    )

@pytest.fixture
def author():
    return Author.objects.create(
        name='Test Author',
        bio='Test Bio'
    )

@pytest.fixture
def publisher():
    return Publisher.objects.create(
        name='Test Publisher',
        country='Test Country'
    )

@pytest.fixture
def book(author, publisher):
    return Book.objects.create(
        title='Test Book',
        author=author,
        publisher=publisher,
        price=29.99,
        genre='Fiction',
        year=2023
    )