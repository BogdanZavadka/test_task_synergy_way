import requests
from tasks import add_address


def test_add_address_success(mocker):
    mock_location_data = {
        "data": [{
            "country": "USA",
            "city": "Los Angeles",
            "streetName": "Sunset Blvd",
            "buildingNumber": 123,
            "zipcode": 90001
        }]
    }

    mock_user_list = [{"id": 1}, {"id": 2}]

    mocker.patch("tasks.random.choice", return_value=1)

    mock_get = mocker.patch("tasks.requests.get")
    mock_post = mocker.patch("tasks.requests.post")

    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: mock_location_data),
        mocker.MagicMock(status_code=200, json=lambda: mock_user_list)
    ]

    mock_post.return_value = mocker.MagicMock(status_code=201, json=lambda: {"id": 1})

    result = add_address()
    assert result == {"id": 1}


def test_add_address_randomuser_api_fail(mocker):
    mocker.patch("tasks.requests.get", side_effect=requests.RequestException("Network error"))
    result = add_address()
    assert result is None


def test_add_address_user_api_fail(mocker):
    mock_get = mocker.patch("tasks.requests.get")
    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: {"results": [{"location": {}}]}),
        requests.RequestException("Failed fetching users")
    ]
    result = add_address()
    assert result is None


def test_add_address_invalid_json(mocker):
    mocker.patch("tasks.random.choice", return_value=1)

    mock_get = mocker.patch("tasks.requests.get")
    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: {"results": [{"location": {"city": "Kyiv"}}]}),
        mocker.MagicMock(status_code=200, json=lambda: [{"id": 1}])
    ]

    result = add_address()
    assert result is None
