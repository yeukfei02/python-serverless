import json
import uuid

from model.Notes import NotesModel

def getNotes(event, context):
    response = {}

    notesListFromDB = NotesModel.scan()
    
    notesList = []
    if notesListFromDB:
        for notes in notesListFromDB:
            notesObj = dict(notes)
            notesList.append(notesObj)

        body = {
            "message": "getNotes",
            "notes": notesList
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    return response