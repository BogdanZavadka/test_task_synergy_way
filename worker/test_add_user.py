import requests
from tasks import add_user


def mock_user_data():
    return {
        "data": [{
            "firstname": "John",
            "lastname": "Doe",
            "gender": "male",
            "birthday": "2005-05-05",
            "phone": "1234567890",
            "email": "john.doe@example.com"
        }]
    }


def test_add_user_success(mocker):
    mock_get = mocker.patch("tasks.requests.get")
    mock_post = mocker.patch("tasks.requests.post")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_user_data()

    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 1}

    result = add_user()
    assert result == {"id": 1}
    assert mock_post.called


def test_add_user_get_failure(mocker):
    mocker.patch("tasks.requests.get", side_effect=requests.exceptions.RequestException("Network error"))
    result = add_user()
    assert result is None


def test_add_user_post_failure(mocker):
    mock_get = mocker.patch("tasks.requests.get")
    mock_post = mocker.patch("tasks.requests.post", side_effect=requests.exceptions.HTTPError("500 error"))

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_user_data()

    result = add_user()
    assert result is None
