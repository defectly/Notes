import json
from Note import Note

class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
    
class JsonManager:
    def Serialize(notes):
        return json.dumps(notes, cls = NoteEncoder)
    
    def Deserialize(data):
        loaded_notes = list()
        
        for obj in data:
            note = Note(obj['id'], obj['name'], obj['description'])
            loaded_notes.append(note)
        
        return loaded_notes