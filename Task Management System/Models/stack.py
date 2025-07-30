class Stack():
    def __init__(self):
         # Initialize an empty list to store stack items
        self.items=[]
    
    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
        
    def pop(self):
        # Remove and return the top item of the stack
        return self.items.pop()
        
    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.items)==0