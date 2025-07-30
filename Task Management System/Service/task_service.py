from Models.task import Task
from Models.queue import Queue
from Models.stack import Stack
from Models.Graph import Graph

class Task_Service:
    def __init__(self):
        self.tasks=[]
        self.task_queue=Queue()
        self.task_histoty=Stack()
        