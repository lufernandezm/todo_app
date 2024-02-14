from storage import save_tasks, load_tasks
from utils import print_bold

def add_task():
    description = input('Enter task description: ').strip()
    if not description:
        raise ValueError('Task description is required')

    pending_tasks = [task for task in load_tasks() if not task['completed']]
    if any(task['description'] == description for task in pending_tasks):
        raise ValueError('Task description must be unique among pending tasks')

    task = {'id': len(pending_tasks) + 1, 'description': description, 'completed': False}
    save_tasks(pending_tasks + [task])
    print_bold('Task added: ' + description)


def get_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    completed_tasks = [task for task in tasks if task["completed"]]
    pending_tasks = [task for task in tasks if not task["completed"]]

    return completed_tasks, pending_tasks


def format_task(index, task_list):
    return f"{index + 1}. {task_list[index]['description']}" if index < len(task_list) else ""


def print_task_header():
    print_bold(f"\n{'Completed Tasks':<30} | {'Pending Tasks'}")
    print("-" * 60)


def print_tasks(completed_tasks, pending_tasks):
    max_length = max(len(completed_tasks), len(pending_tasks))
    for i in range(max_length):
        completed = format_task(i, completed_tasks)
        pending = format_task(i, pending_tasks)
        print(f"{completed:<30} | {pending}")
        
        
def list_tasks():
    completed_tasks, pending_tasks = get_tasks()
    print_task_header()
    print_tasks(completed_tasks, pending_tasks)


def print_pending_tasks(pending_tasks):
    print_bold("Here are the pending tasks.")
    for i, task in enumerate(pending_tasks):
        print(f"{i + 1}. {task['description']}")

def capture_task_number(pending_tasks):
    while True:  
        try:
            task_number = int(input("Which one do you want to mark as completed? : "))
            if 1 <= task_number <= len(pending_tasks):
                return task_number
            else:
                print(f"Please enter a number between 1 and {len(pending_tasks)}.")  
        except ValueError:
            print("Please enter a valid option.")

def select_task_to_complete():
    _, pending_tasks = get_tasks()
    if not pending_tasks:  
        print_bold("No pending tasks available.")
        return

    print_pending_tasks(pending_tasks)
    task_number = capture_task_number(pending_tasks)
    complete_task(pending_tasks[task_number - 1])

def complete_task(task_completed):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_completed["id"]:
            task["completed"] = True
            break
    save_tasks(tasks)
    print_bold(f"The task: {task_completed['description']} was marked as completed.")
