import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def get_next_id(tasks):
    if not tasks:
        return 1  # Start from 1 if there are no tasks
    return max(map(int, tasks.keys()), default=0) + 1  # Convert keys to int before finding max


def add_task(tasks, task_text):
    task_id = get_next_id(tasks)
    tasks[task_id] = {
        "text": task_text,
        "completed": False
    }
    save_tasks(tasks)
    return task_id

def delete_task(tasks, task_id):
    task_id = str(task_id)
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        return True
    return False

