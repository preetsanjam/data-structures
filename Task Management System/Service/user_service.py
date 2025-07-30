from Models.user import User

class User_Service():
    def __init__(self):
        # Initialize an empty dictionary to store users
        # Key = user ID, Value = User object
        self.users={}
    
    def add_user(self, id, name, email):
        
        # Create a new User object with the given name, id and email
        user=User(name, id, email)
        
        # Add the user to the users dictionary using the ID as the key
        self.users[id]=user
        
        return user 
    
    def get_user(self, id):
        # Retrieve the User object with the given ID from the users dictionary
        return self.users.get(id)