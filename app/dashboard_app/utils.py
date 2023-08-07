from pymongo import MongoClient
from urllib.parse import quote_plus

def get_db_handle(db_name, host, port, username, password):
    db_uri = "mongodb://" + username + ":" + password + "@" + \
    host + "/customer_contacts?authSource=admin&retryWrites=true&w=majority"
    try:
        # client = MongoClient(
        #     host=host,
        #     #port=port,
        #     username=username,
        #     password=password,
        #     authSource=db_name,
        #     authMechanism='SCRAM-SHA-256'
        # )
        client = MongoClient(db_uri)
        db_handle = client[db_name]
        return db_handle, client
    except Exception:
        print("Error:" + Exception)
        return None 

