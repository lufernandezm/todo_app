import typer
from typer import Option
from task_manager import add_task, list_tasks, select_task_to_complete
from utils import print_bold

default_option = Option(None, "--option", "-o", help="Option number")

def get_menu_option():  
    print("_" * 60)
    print_bold("Options")
    print("1. Add a new task.")
    print("2. List my tasks.")
    print("3. Mark a task as completed.")
    print("4. Exit.")
    try:
        option = int(input("Select an option: "))
    except ValueError:
        return None
    return option

def handle_option(option):
    try:
        if option == 1:
            add_task()
        elif option == 2:
            list_tasks()
        elif option == 3:
            select_task_to_complete()
        elif option == 4:
            print_bold("Good bye! :)")
            return False
        else:
            print_bold("Invalid option, please try again.")
        return True
    except Exception as e:
        print_bold(e)
        return True



def main(option=default_option):
    while True:
        if option is None:
            option = get_menu_option()
        if not handle_option(option):
            break
        option = None


if __name__ == "__main__":
    typer.run(main)
