from http.client import responses
from flask import jsonify, request
from app import validators
from app import responses
from http import HTTPStatus
from app import models
from bson import ObjectId

def Create():
    bodyJson = request.json
    err = validators.TesCre(bodyJson)  
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message="error",
            Data=str(err)
        )
    
    collTable = models.Tables(nama=bodyJson["nama"], deskripsi=bodyJson["deskripsi"])
    collTable.save()
    
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={}
    )

def List():
    collTable = models.Tables.objects().all()
    data = []
    for i in collTable:
        data.append({
            "id": str(i.id),
            "nama": i.nama,
            "deskripsi": i.deskripsi,
        })
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=data
    ), HTTPStatus.OK.value

def Update(tableId):
    bodyJson = request.json
    err = validators.TesUp(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.OK,
            Message="error",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collTable = models.Tables.objects(id=ObjectId(tableId)).update(nama=bodyJson["nama"], deskripsi=bodyJson["deskripsi"])
    return bodyJson

def Delete(tableId):
    models.Tables.objects(id=ObjectId(tableId)).delete()
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=f"successfully deleted table with id: {tableId}"
    ), HTTPStatus.OK.value

def Detail(tableId):
    collTable = models.Tables.objects(id=ObjectId(tableId)).first()
    if not collTable:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="doesn't exist."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "nama": collTable.nama,
            "deskripsi": collTable.deskripsi
        }
    ), HTTPStatus.OK.value