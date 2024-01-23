from re import I
from typing import overload
from Note import Note

class NotesManager:
    notes: list
    
    def __init__(self, notes):
        self.notes = notes
    
    def add(self, name, description):
        
        if(len(self.notes) > 0):
            last_id = max(note.id for note in self.notes)
        else:
            last_id = -1
            
        self.notes.append(Note(last_id + 1, name, description, None))
        
    def edit(self, id, new_name, new_description):
        note_index = self.get_index(id)
        
        if note_index == None:
            return
        
        self.notes[note_index].name = new_name
        self.notes[note_index].description = new_description
        
    def remove(self, id):
        note_index = self.get_index(id)
        
        if note_index == None:
            return
        
        self.notes.pop(note_index)
    
    def read(self):
        return self.notes
    
    def read_by_id(self, id):
        index = self.get_index(id)
        
        if index == None:
            return
        
        return self.notes[self.get_index(id)]
    
    def get_index(self, id):
        return next((index for (index, note) in enumerate(self.notes) if note.id == id), None)