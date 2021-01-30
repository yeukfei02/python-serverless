import json
import uuid
import bcrypt

from model.User import UserModel

def signup(event, context):
    response = {}

    if event['body']:
        body = json.loads(event['body'])
        
        email = body['email']
        password = body['password']
        
        uuidStr = str(uuid.uuid4())

        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)
        hashedPasswordDecoded = hashedPassword.decode('utf-8')
        
        userModel = UserModel(id=uuidStr, email=email, password=hashedPasswordDecoded)
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
