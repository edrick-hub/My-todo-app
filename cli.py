#from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    #Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

        
    if user_action.startswith("add"):
        todo = user_action[4:]

            #file = open("todos.txt", "r")
            #todos = file.readlines()       #this is how you create a list in a text file
            #file.close()                    # This can be done using the context manager as I do in the next lie
        todos = functions.get_todos()

        todos.append(todo + '\n')

            #file = open("todos.txt", 'w')  #we will use the context manager to write lines to this file as well
            #file.writelines(todos)
            #file.close()
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        
        todos = functions.get_todos()
        

            #new_todos = []    This is one way to strip the spaces in the list output

            #for item in todos:
                #new_item = item.strip('\n')
                #new_todos.append(new_item)

            #new_todos = [item.strip('\n') for item in todos]    #This is called a list comprehension and another way to strip the extra spaces 
            

        for index, item in enumerate(todos):        
            item = item.strip('\n')                 #or you can create a new item variable and strip it
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1
                
            todos = functions.get_todos()

            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            
            functions.write_todos( todos)

        except ValueError:
             print("Your command is not valid")
             continue

    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')        
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list" 
            print(message)
        except IndexError:
             print("There is no item with that number")
             continue
        
    elif user_action.startswith("exit"):
        break
    else:
         print("Command is not valid")

print("bye")