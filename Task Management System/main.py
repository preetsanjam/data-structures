from Service.task_service import Task_Service
from Service.user_service import User_Service

def main():
    task_service=Task_Service()
    user_service=User_Service()

    user_service.add_user(123, "Sanjam", "sanjam@abc.com")
    task_service.create_task(1, "Teach Data Structure basics", "Crash course")
    task_service.create_task(2, "Teach advanced Data Structure", "Crash course")
    task_service.create_task(3, "Complete a project", "Assignment")
    
    print((task_service.complete_task()))
    print((task_service.complete_task()))
    print((task_service.complete_task()))
    
    history=task_service.get_task_history()
    while not history.is_empty():
        # Keep popping from the stack until it’s empty
        # Since task history is a stack (LIFO), the pop() calls will print tasks in reverse completion order
        print(history.pop().title)

    
if __name__=="__main__":
    main()