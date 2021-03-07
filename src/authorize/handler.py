import jwt
import os
import logging as logger


def authorize(event, context):
    token = event['authorizationToken'].replace('Bearer ', '')
    # methodArn = event.methodArn;

    policyDocument = {}
    try:
        decoded = jwt.decode(
            token, os.environ['JWT_SECRET'], algorithms=["HS256"])
        effect = 'Deny'
        if decoded:
            effect = 'Allow'

        policyDocument = generatePolicyDocument(decoded['id'], effect)
    except:
        logger.info('error')

    return policyDocument


def generatePolicyDocument(principalId, effect):
    policyDocument = {}

    if principalId and effect:
        policyDocument = {
            "principalId": principalId,
            "policyDocument": {
                "Version": '2012-10-17',
                "Statement": [
                    {
                        "Action": 'execute-api:Invoke',
                        "Effect": effect,
                        "Resource": '*',
                    },
                ],
            },
        }

    return policyDocument
