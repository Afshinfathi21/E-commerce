import requests


ORDER_SERVICE_URL='http://order:8000/orders/'

def update_order(token,order_id):
    response=requests.patch(f'{ORDER_SERVICE_URL}{order_id}',headers={'Authorization':token})
    return response.status_code == 200