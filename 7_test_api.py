from urllib import response
import pytest
import requests
import json

# go to https://reqres.in/  => then click "LOGIN - SUCCESSFUL"

def test_valid_login():
    url="https://reqres.in/api/login/"
    data={"email":"abc@xyz.com","password":"qwerty"}
    response =requests.post(url,data=data)
    print(response)
    token =json.loads(response.text)
    assert response.status_code ==200
    assert token["token"]=="QpwL5tke4Pnpja7X4"