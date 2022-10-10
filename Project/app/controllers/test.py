import collections
from distutils.log import error
from http.client import responses
from flask import jsonify, request
from app import validators
from app import responses
from http import HTTPStatus
from app import models

def index():
    data = [
        {
        "id" : 1,
        "name": "zidan"
    },
    {
        "id" : 2,
        "name": "hakim"
    }
    ]
    return jsonify(data)

def create():
    bodyJson = request.json
    err = validators.test(bodyJson)
    if err:
        return responses.Make(Status=HTTPStatus.BAD_REQUEST.value,
                              Message="error",
                              Data=str(err)
                              ), HTTPStatus.BAD_REQUEST.value
    collUser = models.User(userName=bodyJson["userName"], userPassword=bodyJson["userPassword"]).save() #coll = tabel
    #collUser.save()
    #print(err)
    return responses.Make(Status=HTTPStatus.OK.value,
                              Message="succes",
                              Data={}
                              ), HTTPStatus.OK.value
    return ""