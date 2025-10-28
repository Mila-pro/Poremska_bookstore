import pytest
from django.urls import reverse
from main.models import Book


@pytest.mark.django_db
def test_get_books_list(api_client, book):
    response = api_client.get("/api/books/")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_books_empty_list(api_client):
    response = api_client.get("/api/books/")
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_get_book_detail(api_client, book):
    response = api_client.get(f"/api/books/{book.id}/")
    assert response.status_code == 200
    assert response.data['title'] == 'Test Book'


@pytest.mark.django_db
def test_create_book_with_auth(api_client, user, author, publisher):
    api_client.force_authenticate(user=user)
    
    response = api_client.post(
        "/api/books/",
        {
            'title': 'New Book',
            'author': author.id,
            'publisher': publisher.id,
            'price': 19.99,
            'genre': 'Science Fiction', 
            'year': 2024
        },
        format='json'
    )
    
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_book_with_auth(api_client, user, book):
    api_client.force_authenticate(user=user)
    
    response = api_client.put(
        f"/api/books/{book.id}/",
        {
            'title': 'Updated Book',
            'author': book.author.id,
            'publisher': book.publisher.id,
            'price': 39.99,
            'genre': 'Updated Genre',
            'year': 2025
        },
        format='json'
    )
    
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_book_with_auth(api_client, user, book):
    api_client.force_authenticate(user=user)
    
    response = api_client.delete(f"/api/books/{book.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_book_invalid_data(api_client, user):
    api_client.force_authenticate(user=user)
    
    response = api_client.post(
        "/api/books/",
        {
            'title': '',
            'author': 1,
            'publisher': 1,
            'price': 19.99,
            'genre': 'Genre',
            'year': 2024
        },
        format='json'
    )
    
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_nonexistent_book(api_client):
    response = api_client.get("/api/books/999/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_book_invalid_token(api_client):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer invalidtoken')
    
    response = api_client.post(
        "/api/books/",
        {
            'title': 'New Book',
            'author': 1,
            'publisher': 1,
            'price': 19.99,
            'genre': 'Genre',
            'year': 2024
        },
        format='json'
    )
    
    assert response.status_code == 401