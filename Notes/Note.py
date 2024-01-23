import datetime


class Note:
    
    id: int
    name: str
    description: str
    date: str
    
    def __init__(self, id, name, description, date):
        self.id = id
        self.name = name
        self.description = description
        
        if(date == None):
            self.date = datetime.datetime.utcnow().strftime("%d.%m.%Y %H:%M").__str__()
        else:
            self.date = date.__str__()
        
            
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, description: {self.description}, date: {self.date}"
    
    def __repr__(self):
        return self.__str__()