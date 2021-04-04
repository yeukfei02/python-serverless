import json
import bcrypt
import jwt
import uuid
import os
import logging as logger

from model.User import UserModel


def login(event, context):
    response = {}

    if event['body']:
        body = json.loads(event['body'])

        email = body['email']
        password = body['password']

        if email and password:
            for userFromDB in UserModel.scan(UserModel.email == email):
                logger.info('userFromDB = {0}', userFromDB)
                if userFromDB:
                    userHashedPasswordFromDB = userFromDB.password
                    isPasswordValid = bcrypt.checkpw(password.encode(
                        'utf-8'), userHashedPasswordFromDB.encode('utf-8'))
                    if isPasswordValid:
                        token = jwt.encode(
                            {
                                "id": str(uuid.uuid4()),
                                "email": email
                            },
                            os.getenv('JWT_SECRET'),
                            algorithm="HS256"
                        )

                        body = {
                            "message": "login",
                            "token": token,
                        }

                        response = {
                            "statusCode": 200,
                            "body": json.dumps(body)
                        }
                    else:
                        body = {
                            "message": "login error, wrong password",
                        }

                        response = {
                            "statusCode": 400,
                            "body": json.dumps(body)
                        }
                else:
                    body = {
                        "message": "login error, no this user",
                    }

                    response = {
                        "statusCode": 400,
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
