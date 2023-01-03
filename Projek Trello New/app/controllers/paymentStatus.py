from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def PaymentStatusList():
    try:
        collPaymentStatus = models.PaymentStatus.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collPaymentStatus:
            dataArray.append({
                "paymentStatusId": str(d.id),
                "paymentStatusName": d.paymentStatusName,
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

def PaymentStatusCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.PaymentStatus(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPaymentStatus = models.PaymentStatus(
            paymentStatusName=bodyJson["paymentStatusName"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collPaymentStatus.save()
        return responses.Make(
            Status=200,
            Message="Success create Payment Status",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PaymentStatusDetail():
    try:
        paymentStatusId = request.args["paymentStatusId"]
        collPaymentStatus = models.PaymentStatus.objects(
            id=ObjectId(paymentStatusId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PaymentStatusUpdate():
    try:
        bodyJson = request.json
        paymentStatusId = request.args["paymentStatusId"]
        userId = request.args["userId"]
        err = validators.PaymentStatus(bodyJson)
        collPaymentStatus = models.PaymentStatus.objects(id=ObjectId(paymentStatusId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collPaymentStatus:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Payment Status not found"
            ), HTTPStatus.BAD_REQUEST.value
        collPaymentStatus.update(paymentStatusName=bodyJson["paymentStatusName"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Payment Status",
            Data=f"PaymentStatus with paymentStatusId {paymentStatusId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PaymentStatusDelete():
    try:
        paymentStatusId = request.args["paymentStatusId"]
        userId = request.args["userId"]
        collPaymentStatus = models.PaymentStatus.objects(
            id=ObjectId(paymentStatusId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collPaymentStatus:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Payment Status not found"
            ), HTTPStatus.BAD_REQUEST.value
        collPaymentStatus.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete Payment Status",
            Data=f"Payment Status with paymentStatusId {paymentStatusId} was deleted by {userId}"
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value