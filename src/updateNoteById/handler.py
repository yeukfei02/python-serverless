import json
import uuid

from model.Notes import NotesModel

def updateNoteById(event, context):
    response = {}

    if event['pathParameters']:
        id = event['pathParameters']['id']

        body = json.loads(event['body'])

        content = body['content']
        
        try:
            noteFromDB = NotesModel.get(id)
            noteFromDB.update(
                actions=[NotesModel.content.set(content)]
            )

            note = {}
            if noteFromDB:
                note = dict(noteFromDB)

                body = {
                    "message": "updateNoteById",
                    "note": note,
                }
        except:
            body = {
                "message": "updateNoteById error, no this id",
                "note": {},
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