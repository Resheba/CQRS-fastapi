import pytest
from fastapi.testclient import TestClient

from src.app.app import app


@pytest.fixture(scope='module')
def client():
    return TestClient(app())


class TestUserRouter:
    def test_get_user(self, client: TestClient):
        response = client.get('/user')
        assert response.status_code == 200
        assert response.json() == {"status": "success", "msg": None, "data": [] }
    
    def test_create_user(self, client: TestClient):
        response = client.post('/user', json={"username": "test"})
        assert response.status_code == 201
        assert response.json().get('data').get('username') == 'test'

    def test_delete_user(self, client: TestClient):
        response = client.post('/user', json={"username": "test"})
        assert response
        user = response.json().get('data')
        assert response.status_code == 201

        response = client.request('DELETE', f'/user', json={"user_id": user.get('id')})
        assert response.status_code == 204

        response = client.get('/user')
        assert response.status_code == 200
        assert len(response.json().get('data')) == 1

    def test_invalid_user(self, client: TestClient):
        response = client.post('/user', json={"rg": "a"*100})
        assert response.status_code == 422
    
    def test_invalid_user2(self, client: TestClient):
        response = client.post('/user', json={"username": "a"*100})
        assert response.status_code == 409
