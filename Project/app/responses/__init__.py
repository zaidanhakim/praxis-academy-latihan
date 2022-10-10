from flask import jsonify

def Make(Status, Message, Data):
    data = {
        "status": Status,
        "message": Message,
        "data": Data
    }
    return data