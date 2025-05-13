import requests
from tasks import add_card


def test_add_card_success(mocker):
    card_data = {
        "credit_card_number": "4111111111111111",
        "credit_card_expiry_date": "2025-12-31",
        "credit_card_type": "Visa"
    }

    users_data = [{"id": 1}, {"id": 2}]

    mocker.patch("tasks.random.choice", return_value=1)
    mocker.patch("tasks.random.randint", return_value=123)

    mock_get = mocker.patch("tasks.requests.get")
    mock_post = mocker.patch("tasks.requests.post")

    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: card_data),
        mocker.MagicMock(status_code=200, json=lambda: users_data)
    ]

    mock_post.return_value = mocker.MagicMock(status_code=201, json=lambda: {"id": 1})

    result = add_card()
    assert result == {"id": 1}


def test_add_card_fetch_card_data_fail(mocker):
    mocker.patch("tasks.requests.get", side_effect=requests.RequestException("Network error"))
    result = add_card()
    assert result is None


def test_add_card_fetch_users_fail(mocker):
    mock_get = mocker.patch("tasks.requests.get")
    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: {"credit_card_number": "1234"}),
        requests.RequestException("DB error")
    ]
    result = add_card()
    assert result is None


def test_add_card_invalid_json(mocker):
    mocker.patch("tasks.random.choice", return_value=1)
    mocker.patch("tasks.random.randint", return_value=123)

    mock_get = mocker.patch("tasks.requests.get")
    mock_get.side_effect = [
        mocker.MagicMock(status_code=200, json=lambda: {"credit_card_type": "Visa"}),  # missing keys
        mocker.MagicMock(status_code=200, json=lambda: [{"id": 1}])
    ]

    result = add_card()
    assert result is None
