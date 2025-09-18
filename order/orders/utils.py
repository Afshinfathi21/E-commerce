import requests

PRODUCT_SERVICE_URL='http://product:8000/api/products/'
INVENTORY_SERVICE_URL='http://inventory:8000/api/inventories/'

def product_exist(product_id):
    response=requests.get(f'{PRODUCT_SERVICE_URL}{product_id}/')
    return response.status_code == 200

def check_inventory(product_id,quantity):
    response=requests.get(f'{INVENTORY_SERVICE_URL}{product_id}/')
    if response.status_code != 200:
        return False
    stock=response.json().get('quantity',0)
    return stock >= quantity

def reduce_inventory(product_id,quantity,token):
    response=requests.patch(f'{INVENTORY_SERVICE_URL}{product_id}/',json={'quantity':quantity},headers={'Authorization':f'Bearer {token}'})
    return response.status_code == 200
