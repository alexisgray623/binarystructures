'''
Name: Alexis Gray
Purpose: Pokemon Class
'''

class Poke:
    def __init__(self, aName, ID, jName):
        self.aName = aName
        self.jName = jName 
        self.ID = ID 

    def __str__(self):
        return f'{self.aName}  {self.jName} {self.ID}'

    def __eq__(self, other):
            return self.ID == other

    def __ne__(self, other):   
            return self.ID != other

    def __lt__(self, other):
         return self.ID < other
    
    def __le__(self, other):
            return self.ID <= other
    
    def __gt__(self, other):
            return self.ID > other
    
    def __ge__(self, other):
            return self.ID >= other


