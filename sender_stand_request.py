# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data


def post_products_kits(products_ids):
   return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                        json=products_ids,
                        headers=data.headers)
response = post_products_kits(data.product_ids)


def post_new_user(user_body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=user_body,
                        headers=data.headers)

def get_users_table():
    return requests.get (configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

print(response.status_code)
print(response.json())
