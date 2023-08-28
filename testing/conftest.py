from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
