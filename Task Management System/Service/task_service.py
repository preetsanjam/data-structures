from Models.Task import Task
from Models.Queue import Queue
from Models.Stack import Stack
from Models.Graph import Graph

class Task_Service:
    def __init__(self):
        
        # Initialize an empty list to store all tasks
        self.tasks=[]
        
        # Initialize a queue to manage task execution order (FIFO)
        self.task_queue=Queue()
        
        # Initialize a stack to store completed task history (LIFO)
        self.task_history=Stack()
        
    def create_task(self, id, title, description):
        
         # Create a new Task object
        task=Task(id, title, description)
        
         # Add the task to the task list
        self.tasks.append(task)
        
        # Enqueue the task into the task queue
        self.task_queue.enqueue(task)
        
        # Return the created task
        return task
    
    def complete_task(self):
        
        # Check if the task queue is not empty
        if not self.task_queue.is_empty():
            
            # Remove the task from the front of the queue
            task=self.task_queue.dequeue()
            
             # Push the completed task into the history stack
            self.task_history.push(task) # We're pushing task history because it is of Stack DS
            
            return task.title  
        
        # If no task is available, return None
        return None
    
    def get_task_history(self):
        # Return the stack object storing the completed tasks
        return self.task_history