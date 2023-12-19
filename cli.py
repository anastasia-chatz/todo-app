from functions import *
import time

fp = "todos.txt"
now = time.strftime('%b %d, %Y, %H:%M:%S')
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index = index - 1
            todos = get_todos()
            new_todo = input("Enter todo to replace existing todo: ")
            todos[index] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid. To edit a todo, enter the index of the todo after edit.")
            continue
    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            index = int(user_action[9:])
            todo_to_remove = todos[index - 1].strip("\n")
            todos.pop(index - 1)
            write_todos(todos)
            print(f"Todo completed: {index}. {todo_to_remove}. Yay!!")
        except IndexError:
            print(f"Your command is not valid. Todo with index {user_action[9:]} does not exist.")
            continue
        except ValueError:
            print("Your command is not valid. To complete a todo, enter the index of the todo after complete.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command not recognized.")

print("Bye!")
