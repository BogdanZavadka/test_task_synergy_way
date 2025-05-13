from datetime import datetime

from celery import Celery
import requests
import random

app = Celery('tasks', broker='redis://redis', backend='redis://redis')

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MyApp/1.0)'
}

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(55.0, add_user.s(), name='add user every 55 seconds')
    sender.add_periodic_task(57.0, add_address.s(), name='add address every 57 seconds')
    sender.add_periodic_task(60.0, add_card.s(), name='add credit card every 60 seconds')


@app.task
def add_user():
    try:
        response = requests.get('https://fakerapi.it/api/v2/persons?_quantity=1', headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch user data: {e}")
        return None

    try:
        response_result_json = response.json()['data'][0]
        data = {
            "first_name": response_result_json['firstname'],
            "last_name": response_result_json['lastname'],
            "gender": response_result_json['gender'],
            "age": datetime.today().year - datetime.strptime(response_result_json['birthday'], "%Y-%m-%d").year,
            "phone_number": response_result_json['phone'],
            "email": response_result_json['email']
        }

        post_response = requests.post('http://django-web:8000/api/users/create', data=data)
        post_response.raise_for_status()
        return post_response.json()
    except requests.RequestException as e:
        print(f"Failed to post user data: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error processing JSON: {e}")

    return None


@app.task
def add_address():
    try:
        response = requests.get('https://fakerapi.it/api/v2/addresses?_quantity=1', headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch user data: {e}")
        return None

    try:
        users = requests.get('http://django-web:8000/api/users')
        users.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch user data from db: {e}")
        return None

    users_ids = [user['id'] for user in users.json()]

    try:
        response_result_json = response.json()['data'][0]
        data = {
            "user_id": random.choice(users_ids),
            "country": response_result_json['country'],
            "city": response_result_json['city'],
            "street": response_result_json['streetName'],
            "house_number": response_result_json['buildingNumber'],
            "postal_code": response_result_json['zipcode']
        }
        post_response = requests.post('http://django-web:8000/api/addresses/create', data=data)
        post_response.raise_for_status()
        return post_response.json()
    except requests.RequestException as e:
        print(f"Failed to post address data: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error processing JSON: {e}")

    return None


@app.task
def add_card():
    try:
        response = requests.get('https://random-data-api.com/api/v2/credit_cards')
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch card data: {e}")
        return None

    try:
        users = requests.get('http://django-web:8000/api/users')
        users.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch user data: {e}")
        return None

    users_ids = [user['id'] for user in users.json()]

    try:
        response_result_json = response.json()
        data = {
            "user_id": random.choice(users_ids),
            "card_number": response_result_json['credit_card_number'],
            "cvv": random.randint(100, 999),
            "expiration_date": response_result_json['credit_card_expiry_date'],
            "bank_name": response_result_json['credit_card_type'],
        }
        post_response = requests.post('http://django-web:8000/api/credit_cards/create', data=data)
        post_response.raise_for_status()
        return post_response.json()
    except requests.RequestException as e:
        print(f"Failed to post card data: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error processing JSON: {e}")

    return None
