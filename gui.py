import functions
import PySimpleGUI as sg
import time

sg.theme('DarkBlue14')
clock = sg.Text(time.strftime('%d %B %Y, %H:%M:%S'), key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
error_label = sg.Text('', key='error-text')

window = sg.Window("My To-do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box],
                           [edit_button, complete_button],
                           [error_label]],
                   font=("RNS Sans", 12))
while True:
    event, values = window.read(timeout=900)
    window['clock'].update(value=time.strftime('%d %B %Y, %H:%M:%S'))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                window['error-text'].update(value='Please select a todo to edit.')
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = int(todos.index(todo_to_complete))
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                window['error-text'].update(value='Please select a todo to complete.')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()