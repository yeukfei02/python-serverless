import json


def main(event, context):
    body = {
        "message": "python serverless",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
