import sys
import json
import os

DB_FILE = os.path.expanduser("~/.taskmgr_data.json")

ID_COUNTER = 0
TODO = []
DOING = []
DONE = []


def save_data():
    """Saves the current lists and ID counter to a JSON file."""
    data = {
        "id_counter": ID_COUNTER,
        "todo": TODO,
        "doing": DOING,
        "done": DONE
    }
    try:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(" -> (Auto-Saved)") 
    except Exception as erro:
        print(f"Error saving data: {erro}")

def load_data():
    """Loads data from JSON file and restores integer keys."""
    global TODO, DOING, DONE, ID_COUNTER
    
    if not os.path.exists(DB_FILE):
        return  

    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)

        ID_COUNTER = data.get("id_counter", 0)

        def clean_list(json_list):
            cleaned = []
            for item in json_list:
                for k, v in item.items():
                    cleaned.append({int(k): v})
            return cleaned

        TODO = clean_list(data.get("todo", []))
        DOING = clean_list(data.get("doing", []))
        DONE = clean_list(data.get("done", []))
        
        print("Data loaded successfully.")

    except Exception as erro:
        print(f"Error loading data: {erro}")


def print_section(title, task_list):
    """Helper to print lists cleanly"""
    print(f"{title}:")
    if not task_list:
        print("  (Empty)")
    else:
        for task in task_list:
            for t_id, t_name in task.items():
                print(f"  [{t_id}] {t_name}")
    print("-" * 65)

def menu():
    """Display the menu and return user choice"""
    print(r""" _            _
| |_ __ _ ___| | __  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __
| __/ _` / __| |/ / | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
| || (_| \__ \   <  | | | | | | (_| | | | | (_| | (_| |  __/ |
 \__\__,_|___/_|\_\ |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                                 |___/
        """)
    
    print_section("TODO", TODO)
    print_section("DOING", DOING)
    print_section("DONE", DONE)

    print(r"""
    [1] Update Task Status (Move Forward)
    [2] Add New Task
    [3] Remove Task
    [4] Quit
          """)
    return input("Watcha gonna du? >>> ")


def add_task():
    global ID_COUNTER 
    task_name = input("What's ur task? Type: ")
    if not task_name: return
    
    ID_COUNTER += 1
    task = {int(ID_COUNTER): task_name}
    TODO.append(task)
    print("Task added!")
    save_data() 

def update_task():
    try:
        t_id = int(input("Enter the ID of the task to advance: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for index, task in enumerate(TODO):
        if t_id in task:
            moved_task = TODO.pop(index)
            DOING.append(moved_task)
            print(f"Task {t_id} moved to DOING.")
            save_data() 
            return

    for index, task in enumerate(DOING):
        if t_id in task:
            moved_task = DOING.pop(index)
            DONE.append(moved_task)
            print(f"Task {t_id} moved to DONE.")
            save_data() 
            return

    for task in DONE:
        if t_id in task:
            print(f"Task {t_id} is already completed!")
            return

    print("ID not found.")

def remove_task():
    try:
        rm_choice = int(input(f"What task number u wish to pop? Type: "))
        found = False

        for current_list in [TODO, DOING, DONE]:
            for index, task in enumerate(current_list):
                if rm_choice in task:
                    current_list.pop(index)
                    print(f"Popped task {rm_choice}.")
                    found = True
                    save_data() 
                    break
            if found: break

        if not found:
            print("Task ID not found anywhere.")

    except ValueError:
        print(f"ID must be a number.")
    except Exception as erro:
        print(f"An error occurred: {erro}")

def quit_app():
    print('See ya later...')
    sys.exit()

load_data()

while True:
    try:
        choice = menu()
        
        if choice == "1":
            update_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            quit_app()
        else:
            print("\nInvalid option.")
            input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\nExiting safely...")
        sys.exit()