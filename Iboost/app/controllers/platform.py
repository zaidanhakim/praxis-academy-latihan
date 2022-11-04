from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators


def PlatformList():
    try:
        collPlatform = models.Platforms.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collPlatform:
            dataArray.append({
                "platformId": str(d.id),
                "platformName": d.platformName,
                "platformCode": d.platformCode,
                "platformPrice": d.platformPrice
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


def PlatformCreate():
    try:
        bodyJson = request.json
        userId = ObjectId(request.args["userId"])
        err = validators.Platform(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform = models.Platforms(
            platformName=bodyJson["platformName"], platformCode=bodyJson["platformCode"], platformPrice=bodyJson["platformPrice"], updatedBy=userId, createdBy=userId)
        collPlatform.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "platformId": str(collPlatform.id),
                "platformName": collPlatform.platformName,
                "platformCode": collPlatform.platformCode,
                "platformPrice": collPlatform.platformPrice
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def PlatformDetail():
    try:
        platformId = ObjectId(request.args["platformId"])
        collPlatform = models.Platforms.objects(
            id=platformId,
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "platformId": str(collPlatform.id),
                "platformName": collPlatform.platformName,
                "platformCode": collPlatform.platformCode,
                "platformPrice": collPlatform.platformPrice
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def PlatformUpdate():
    try:
        bodyJson = request.json
        platformId = ObjectId(request.args["platformId"])
        userId = ObjectId(request.args["userId"])
        err = validators.Platform(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform = models.Platforms.objects(id=platformId, isActive=True, isDelete=False).update(
            platformName=bodyJson["platformName"], platformCode=bodyJson["platformCode"], platformPrice=bodyJson["platformPrice"], updatedBy=userId)
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


def PlatformDelete():
    try:
        platformId = ObjectId(request.args["platformId"])
        userId = ObjectId(request.args["userId"])
        collPlatform = models.Platforms.objects(
            id=platformId,
            isActive=True, isDelete=False).first()
        if not collPlatform:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data=f"Data with id: {platformId} has been deleted"
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform = models.Platforms.objects(
            id=platformId,
            isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "succesfully deleted data with id": f'{platformId}'
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
        
    # platformId = ObjectId(request.args["platformId"])
    # userId = ObjectId(request.args["userId"])
    # collPlatform = models.Platforms.objects(
    #         id=platformId,
    #         isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
    # if not collPlatform:
    #     return responses.Make(
    #         Status=HTTPStatus.OK.value,
    #         Message="error",
    #         Data=f"Data dengan id: {platformId} sudah terhapus"
    #     ), HTTPStatus.BAD_REQUEST.value
    
    # return responses.Make(
    #     Status=HTTPStatus.OK.value,
    #     Message="success",
    #     Data=f"successfully deleted table with id: {platformId}"
    # ), HTTPStatus.OK.value