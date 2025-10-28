import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_register_user(api_client) -> None:
    response = api_client.post(
        reverse('register'),
        {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password_check': 'newpass123'
        },
        format="json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_user(api_client, user) -> None:
    response = api_client.post(
        reverse('login'),
        {
            'username': 'testuser',
            'password': 'testpass123'
        },
        format="json"
    )
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_logout_user(api_client, user) -> None:
    login_response = api_client.post(
        reverse('login'),
        {
            'username': 'testuser',
            'password': 'testpass123'
        },
        format="json"
    )
    access_token = login_response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    
    response = api_client.post(reverse('logout'))
    assert response.status_code == 200