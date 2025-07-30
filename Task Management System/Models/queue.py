from collections import deque # deque -- double-ended queue

class Queue():
    def __init__(self):
        self.items=deque()
        
    # enqueue means enter
    def enqueue(self, item): 
        self.items.append(item)
        
    # dequeue means to exit
    '''
    The reason why item is not passed to the dequeue() method is because:
    Dequeue removes the first item — no need to specify which one
    '''
    def dequeue(self):
        return self.items.popleft() # popleft() removes the first item
    
    def is_empty(self):
        return len(self.items)==0