import pprint

from prom_ua_toolkit import PromUaToolkit
from config import TOKEN

# API Prom.ua https://prom.ua/cloud-cgi/static/uaprom-static/docs/swagger/index.html#/

# API Settigs
AUTH_TOKEN = TOKEN  # Your authorization token


 
def main():
    # Initialize Client
    if not AUTH_TOKEN:
        raise Exception('Sorry, there\'s no any AUTH_TOKEN!')

    api_example = PromUaToolkit(AUTH_TOKEN)


# GET PRODUCTS LIST
    print("GET PRODUCTS LIST")
    product_list = api_example.get_product_list()
    if not product_list['products']:
        raise Exception('Sorry, there\'s no any product!')
    
    pprint.pprint(api_example.get_product_list())
 
# GET INFORMATION OF PRODUCT
    print("GET PRODUCTS ID")
    product_list = api_example.get_product_list()
    if not product_list['products']:
        raise Exception('Sorry, there\'s no any product!')
    
    product_id = product_list['products'][0]['id']
    pprint.pprint(api_example.get_product_id(product_id))

#?????????????????????????????????????????
 # SET PRODUCTS EDIT
    print("POST PRODUCTS EDIT")
    product_list = api_example.get_product_list()
    if not product_list['products']:
        raise Exception('Sorry, there\'s no any product!')
    
    product_id = product_list['products'][0]['id']
    
    product_data = {
        "id": product_id, # integer
        "presence": "available", # string [ available, not_available, order, waiting ]
        "presence_sure": True, # boolean
        "price": 200, # number (float)
        "status": "on_display", # string [ on_display, draft, deleted, not_on_display ]
        "discount": { 
            "value": 25, #	number
            "type": "percent", # string [ amount, percent ]
            "date_start": "30.06.2023", # string 
            "date_end": "03.07.2023" # string 
        },
        "name": "Вечернее платье", # string 
        "keywords": "Платье, коктейльное платье", # string 
        "description": "Коктейльное платье или платье-коктейль — укороченное женское платье для торжественных случаев без воротника и рукавов." # string 

    }
    pprint.pprint(api_example.edit_product(product_data))






# GET ORDERS LIST 
    print("GET ORDERS LIST")
    order_list = api_example.get_order_list()
    if not order_list['orders']:
        raise Exception('Sorry, there\'s no any order!')
    pprint.pprint(api_example.get_order_list())

# GET INFORMATION OF ORDER
    print("GET ORDERS ID")
    order_list = api_example.get_order_list()
    if not order_list['orders']:
        raise Exception('Sorry, there\'s no any order!')
    order_id = order_list['orders'][0]['id']
    pprint.pprint(api_example.get_order_id(order_id))

# SET ORDERS STATUS
    print("SET ORDER STATUS")
    order_list = api_example.get_order_list()
    if not order_list['orders']:
        raise Exception('Sorry, there\'s no any order!')
    order_id = order_list['orders'][0]['id']
    order_ids = [order_id]
    order_data = {
        "status": 'delivered', # string [ pending, received, delivered, canceled, draft, paid ]
        "ids": order_ids # List of unique identifiers.
    }

    pprint.pprint(api_example.set_order_status(order_data))










    message_list = api_example.get_message_list()
    if not message_list['messages']:
        raise Exception('Sorry, there\'s no any message!')
    
# GET MESSAGES LIST
    print("GET MESSAGES LIST")
    pprint.pprint(api_example.get_message_list())

# GET INFORMATION OF MESSAGE
    print("GET MESSAGES ID")
    message_id = message_list['messages'][0]['id']
    pprint.pprint(api_example.get_message_id(message_id))

# SET MESSAGE STATUS
    print("SET MESSAGE STATUS")
    message_id = message_list['messages'][0]['id']
    ids = [message_id]
    message_data_status= {
        "status": "read", #[ unread, read, deleted ]
        "ids": ids
    }
    pprint.pprint(api_example.set_message_status(message_data_status))

# SET MESSAGE REPLY
    print("SET MESSAGE REPLY")
    message_id = message_list['messages'][0]['id']
    message_data = {
        "id": message_id,
        "message": "Test message api" #string
    }
    pprint.pprint(api_example.set_message_reply(message_data))



if __name__ == '__main__':
    main()