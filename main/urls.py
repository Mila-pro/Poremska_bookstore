from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.BookListCreate.as_view(), name='book-list'),
    path('api/books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('api/authors/', views.AuthorListCreate.as_view(), name='author-list'),
    path('api/publishers/', views.PublisherListCreate.as_view(), name='publisher-list'),
]