"""
This file contain request call methods
"""
import requests

def get_request(endpoint_url, params):
    print(endpoint_url)
    print(params)
    result = requests.get(endpoint_url, params)
    return result
    
def post_request():
    pass

def put_request():
    pass
    
def delete_request():
    pass
    
def patch_request():
    pass

