import json
import uuid

from model.Notes import NotesModel

def createNotes(event, context):
    response = {}

    if event['body']:
        body = json.loads(event['body'])
        
        content = body['content']

        uuidStr = str(uuid.uuid4())

        notesModel = NotesModel(id=uuidStr, content=content)
        notesModel.save()

        body = {
            "message": "createNotes",
        }

        response = {
            "statusCode": 201,
            "body": json.dumps(body)
        }
    else:
        body = {
            "message": "please enter content in request body",
        }

        response = {
            "statusCode": 400,
            "body": json.dumps(body)
        }

    return response