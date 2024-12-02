import json
import http.client
# 

# API Prom.ua https://prom.ua/cloud-cgi/static/uaprom-static/docs/swagger/index.html#/


HOST = 'my.prom.ua'  # e.g.: my.prom.ua, my.tiu.ru, my.satu.kz, my.deal.by, my.prom.md 

class HTTPError(Exception):
    pass

 


class PromUaToolkit(object):

    def __init__(self, token):
        self.token = token




# PRODUCTS LIST
    def get_product_list(self):
        '''
        Use this method to get a list of products.

        Returns:
                Returns a list of products
        '''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}

        url = '/api/v1/products/list'
        method = 'GET'
        
        connection.request(method, url, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    
    
# INFORMATION OF PRODUCT
    def get_product_id(self, product_id: int):
        '''
        Use this method to get product information

        Args:
            product_id (int): product unique identifier

        Returns:
                Returns information about the product
        '''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}

        url = '/api/v1/products/{id}'
        method = 'GET'
        
        connection.request(method, url.format(id=product_id), headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    

# PRODUCTS LIST
    def edit_product(self, product_data: dict):
        '''
        Use this method to edit a product.

        Args:
            product_data (dict): information for editing the product

        Returns:
                Returns the product's unique identifier
        '''

        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}
        

        url = '/api/v1/products/edit'
        method = 'POST'
        
        body = [
            {
            "id": product_data["id"], # integer
            "presence": product_data["presence"], # string [ available, not_available, order, waiting ]
            "presence_sure": product_data["presence_sure"], # boolean
            "price": product_data["price"], # number (float)
            "status": product_data["status"], # string [ on_display, draft, deleted, not_on_display ]
            "discount": { 
                "value": product_data["discount"]["value"], # number
                "type": product_data["discount"]["type"], # string [ amount, percent ]
                "date_start": product_data["discount"]["date_start"], # string 
                "date_end": product_data["discount"]["date_end"], # string 
            },
            "name": product_data["name"], # string 
            "keywords": product_data["keywords"], # string 
            "description": product_data["description"], # string 
            }
        ]

        if body: 
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
        






# ORDER LIST
    def get_order_list(self):
        '''
        Use this method to get a list of orders.

        Returns:
                Returns a list of orders
        '''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                   'Content-type': 'application/json'}
        
        url = '/api/v1/orders/list'
        method = 'GET'

        connection.request(method, url, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())

# INFORMATION OF ORDER
    def get_order_id(self, order_id: int):
        '''
        Use this method to get order information

        Args:
            order_id (int): order unique identifier

        Returns:
                Returns information about the order
        '''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}

        url = '/api/v1/orders/{id}'
        method = 'GET'
        
        connection.request(method, url.format(id=order_id), headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    

# CHANGE OF ORDER STATUS 
    def set_order_status(self, order_data: dict):
        '''
        Use this method to change the product status

        Args:
            order_data (dict): status change information

        Returns:
                List of identifiers of processed messages.
        '''

        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}
        
        url = '/api/v1/orders/set_status'
        method = 'POST'

        body = {
            "status": order_data["status"], # string [ pending, received, delivered, canceled, draft, paid ]
            "ids": order_data["ids"] # List of unique identifiers.
        }

        if body: 
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    






# MESSAGE LIST
    def get_message_list(self):
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                   'Content-type': 'application/json'}
        
        url = '/api/v1/messages/list'
        method = 'GET'

        connection.request(method, url, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    

# INFORMATION OF MESSAGE
    def get_message_id(self, message_id: int):
        '''
        Use this method to get product information

        Args:
            product_id (int): product unique identifier

        Returns:
                Returns information about the product
        '''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}
        
        url = '/api/v1/messages/{id}'
        method = 'GET'
        
        connection.request(method, url.format(id=message_id), headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    

# CHANGE OF MESSAGE STATUS 
    def set_message_status(self, message_data_status: dict):
        '''
        Use this method to change the product status

        Args:
            order_data (dict): status change information

        Returns:
                List of identifiers of processed messages.
        '''

        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}
        url = '/api/v1/messages/set_status'
        method = 'POST'
        
        body = {
            "status": message_data_status["status"],
            "ids": message_data_status["ids"]
        }

        if body: 
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())
    
# Відповідь на повідомлення 
    def set_message_reply(self, message_data: dict):
        '''
        Use this method to change the product status

        Args:
            order_data (dict): status change information

        Returns:
                List of identifiers of processed messages.
        '''

        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                'Content-type': 'application/json'}

        url = '/api/v1/messages/reply'
        method = 'POST'

        body = {
            "id": message_data["id"], # integer
            "message": message_data["message"] # string
        }

        if body: 
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())