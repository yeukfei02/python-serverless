import json

from model.Notes import NotesModel


def getNoteById(event, context):
    response = {}

    if event['pathParameters']:
        id = event['pathParameters']['id']

        try:
            noteFromDB = NotesModel.get(id)

            note = {}
            if noteFromDB:
                note = dict(noteFromDB)

                body = {
                    "message": "getNoteById",
                    "note": note
                }
        except:
            body = {
                "message": "getNoteById error, no this id",
                "note": {}
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
