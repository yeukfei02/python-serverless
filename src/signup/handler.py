import json
import uuid
import hashlib
from model.User import UserModel


def signup(event, context):
    response = {}

    if event['body']:
        body = json.loads(event['body'])

        email = body['email']
        password = body['password']

        uuidStr = str(uuid.uuid4())

        password_encode = password.encode('utf-8')
        hashedPassword = hashlib.sha256(password_encode).hexdigest()

        userModel = UserModel(id=uuidStr, email=email,
                              password=hashedPassword)
        userModel.save()

        if email and password:
            body = {
                "message": "signup",
            }

            response = {
                "statusCode": 201,
                "body": json.dumps(body)
            }
    else:
        body = {
            "message": "please enter email and password in request body",
        }

        response = {
            "statusCode": 400,
            "body": json.dumps(body)
        }

    return response
