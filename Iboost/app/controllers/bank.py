from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators


def BankList():
    try:
        collBank = models.Bank.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collBank:
            dataArray.append({
                "bankId": str(d.id),
                "bankName": d.bankName,
                "bankCode": d.bankCode,
            })
        return responses.Make(
            Status=200,
            Message="success",
            Data=dataArray
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def BankCreate():
    try:
        bodyJson = request.json
        userId = ObjectId(request.args["userId"])
        err = validators.Bank(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collBank = models.Bank(
            bankName=bodyJson["bankName"], bankCode=bodyJson["bankCode"], updatedBy=userId, createdBy=userId)
        collBank.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "bankId": str(collBank.id),
                "bankName": collBank.bankName,
                "bankCode": collBank.bankCode,
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def BankDetail():
    try:
        bankId = ObjectId(request.args["bankId"])
        collbank = models.Bank.objects(
            id=bankId,
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "bankId": str(collbank.id),
                "bankName": collbank.bankName,
                "bankCode": collbank.bankCode
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def BankUpdate():
    try:
        bodyJson = request.json
        bankId = ObjectId(request.args["bankId"])
        userId = ObjectId(request.args["userId"])
        err = validators.Bank(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collBank = models.Bank.objects(id=bankId, isActive=True, isDelete=False).update(
            bankName=bodyJson["bankName"], bankCode=bodyJson["bankCode"], updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={}
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def BankDelete():
    try:
        bankId = ObjectId(request.args["bankId"])
        userId = ObjectId(request.args["userId"])
        collBank = models.Bank.objects(
            id=bankId,
            isActive=True, isDelete=False).first()
        if not collBank:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data=f"Data with id: {bankId} has been deleted"
            ), HTTPStatus.BAD_REQUEST.value
        collBank = models.Bank.objects(
            id=bankId,
            isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "succesfully deleted data with id": f'{bankId}'
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value