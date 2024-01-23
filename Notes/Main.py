import json
import sys
from argparse import ArgumentParser
from Note import Note
from JsonManager import JsonManager
from NotesManager import NotesManager

parser = ArgumentParser()
parser.add_argument("--title", help="Note title")
parser.add_argument("--content", help="Note content")
parser.add_argument("--import_path", help="Notes file path")
parser.add_argument("--save_path", help="Path to save new notes file")
parser.add_argument("--id", help="Note id")
parser.add_argument("--add", action="store_true", help="Add note")
parser.add_argument("--edit", action="store_true", help="Edit note by id")
parser.add_argument("--remove", action="store_true", help="Remove note by id")
parser.add_argument("--print", action="store_true", help="Print loaded notes")


args = parser.parse_args()

if args.import_path == None:
    manager = NotesManager(list())
else:
    with open(args.import_path, "r") as file:
        notes = JsonManager.Deserialize(json.load(file))
        manager = NotesManager(notes)
    
    
if args.add:
    manager.add(args.title, args.content)
    
if args.edit:
    manager.edit(args.id, args.title, args.content)
    
if args.remove:
    manager.remove(args.id)

if args.print:
    print(manager.read())
 
if args.save_path != None:
    with open(args.save_path, "w") as file:
        file.writelines(JsonManager.Serialize(manager.read()))