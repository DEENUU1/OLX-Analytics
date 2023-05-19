import pytest
from web import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_home_view_get_method_returns_200_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_search_apartment_view_get_method_returns_200_status_code(client):
    response = client.get("/search_apartment")
    assert response.status_code == 200


def test_search_house_view_get_method_returns_200_status_code(client):
    response = client.get("/search_house")
    assert response.status_code == 200


def test_result_view_get_method_returns_200_status_code(client):
    response = client.get("/results")
    assert response.status_code == 200
