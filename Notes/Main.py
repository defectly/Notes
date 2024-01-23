import json
from datetime import datetime
from argparse import ArgumentParser
from JsonManager import JsonManager
from NotesManager import NotesManager

parser = ArgumentParser()
parser.add_argument("--title", help="Note title")
parser.add_argument("--content", help="Note content")
parser.add_argument("--import_path", help="Notes file path")
parser.add_argument("--save", action="store_true", help="Save this file with new changes")
parser.add_argument("--save_path", help="Path to save new notes file")
parser.add_argument("--id", help="Note id")
parser.add_argument("--start_date", help="Take from this date (dd.MM.YYYY HH:MM)")
parser.add_argument("--end_date", help="Take to this date (dd.MM.YYYY HH:MM)")
parser.add_argument("--add", action="store_true", help="Add note")
parser.add_argument("--edit", action="store_true", help="Edit note by id")
parser.add_argument("--remove", action="store_true", help="Remove note by id")
parser.add_argument("--print", action="store_true", help="Print loaded notes (or by id)")


args = parser.parse_args()

if args.import_path == None:
    manager = NotesManager(list())
else:
    with open(args.import_path, "r") as file:
        notes = JsonManager.Deserialize(json.load(file))
        manager = NotesManager(notes)

if args.start_date != None:
    sorted_notes = list()
    for note in manager.notes:
        if datetime.strptime(note.date, "%d.%m.%Y %H:%M") >= datetime.strptime(args.start_date, "%d.%m.%Y %H:%M"):
            sorted_notes.append(note)
    
    manager.notes = sorted_notes

if args.end_date != None:
    sorted_notes = list()
    for note in manager.notes:
        if datetime.strptime(note.date, "%d.%m.%Y %H:%M") <= datetime.strptime(args.end_date, "%d.%m.%Y %H:%M"):
            sorted_notes.append(note)
    
    manager.notes = sorted_notes
    
if args.add:
    manager.add(args.title, args.content)
    
if args.edit:
    manager.edit(args.id, args.title, args.content)
    
if args.remove:
    manager.remove(args.id)

if args.print:
    if args.id != None:
        print(manager.read_by_id(int(args.id)))
    else:
        print(*manager.read(), sep="\n")
        
if args.save:
    with open(args.import_path, "w") as file:
        file.writelines(JsonManager.Serialize(manager.read()))
 
if args.save_path != None:
    with open(args.save_path, "w") as file:
        file.writelines(JsonManager.Serialize(manager.read()))