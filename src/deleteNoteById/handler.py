import json
import uuid

from model.Notes import NotesModel

def deleteNoteById(event, context):
    response = {}

    if event['pathParameters']:
        id = event['pathParameters']['id']

        try:
            noteFromDB = NotesModel.get(id)

            noteFromDB.delete()

            body = {
                "message": "deleteNoteById",
            }
        except:
            body = {
                "message": "deleteNoteById error, no this id",
            }

            response = {
                "statusCode": 400,
                "body": json.dumps(body)
            }

            return response

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    return response