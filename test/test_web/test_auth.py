from test.test_app_config import client, app


def test_register_view_get_method_returns_200_status_code(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_delete_account_view_get_method_returns_200_status_code(client):
    response = client.get("/delete")
    assert response.status_code == 200
