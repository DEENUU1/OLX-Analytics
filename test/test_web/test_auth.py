from test.test_app_config import app, client


def test_register_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/register")
    assert response.status_code == 200


def test_delete_account_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/delete")
    assert response.status_code == 200
