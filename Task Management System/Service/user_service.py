from Models.user import User

class User_Service():
    def __init__(self):
        self.users={}
    
    def add_user(self, id, name, email):
        user=User(name, id, email)
        self.users[id]=user 