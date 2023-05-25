from test.test_app_config import app, client


def test_home_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_search_apartment_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/search_apartment")
    assert response.status_code == 200


def test_search_house_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/search_house")
    assert response.status_code == 200


def test_result_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/results")
    assert response.status_code == 200


def test_report_view_get_method_returns_200_status_code(client) -> None:
    response = client.get("/report")
    assert response.status_code == 200
