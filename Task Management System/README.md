# Project Structure

This project is a Task Management System that demonstrates practical usage of Python data structures in a modular, production-like format.

Functionalities:
- Stores tasks using a list.
- Stores users using a dictionary.
- Manages task assignments using a queue.
- Tracks task history using a stack.
- Handles task dependencies using a graph. 

```
task management system/
│
├── requirements.txt        # Dependencies
├── main.py                 # Entry point
├── models/                 # Data structures and classes
│   ├── task.py
│   ├── user.py
│   ├── graph.py
│   ├── stack.py
│   └── queue.py
│
├── services/               # Business logic
│   ├── task_service.csv
│   └── user_service.py
│
├── utils/                  # Helper functions
│    └── helpers.py
│
└── data/                   # Sample data
    ├── tasks.json
    └── users.json
```