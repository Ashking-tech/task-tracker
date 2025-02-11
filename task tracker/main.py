from task_manager import add_task, delete_task
from storage import load_tasks

def print_menu():
    print("\n=== Task Tracker ===")
    print("1. add - Add a new task")
    print("2. list - List all tasks")
    print("3. delete - Delete a task")
    print("4. quit - Exit program")

def main():
    tasks = load_tasks()
    
    while True:
        print_menu()
        command = input("\nEnter command: ").lower().strip()
        
        if command == "add":
            task_text = input("Enter task: ")
            task_id = add_task(tasks, task_text)
            print(f"Task added with ID: {task_id}")
            
        elif command == "list":
            if not tasks:
                print("No tasks found!")
            else:
                for task_id, task in tasks.items():
                    print(f"{task_id}. {task['text']}")
                    
        elif command == "delete":
            task_id = input("Enter task ID to delete: ")
            if task_id.isdigit() and delete_task(tasks, int(task_id)):
                print("Task deleted successfully!")
            else:
                print("Invalid task ID!")
                
        elif command == "quit":
            print("Goodbye!")
            break
            
        else:
            print("Invalid command!")



if __name__ == '__main__':
    main()
