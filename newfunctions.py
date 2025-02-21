FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        todos_list = file.readlines()
        return todos_list

def updated_list(new_todo, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(new_todo)

if __name__ == "__main__":
    print("hey")