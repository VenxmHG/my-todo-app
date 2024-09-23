#All capitals for a variable to hold a value
FILEPATH = "todos.txt"

#Creating custom function to open and read a file. Filepath will read any file path given as an argument. filepath=FILEPATH(("todos.txt")) is a default argument
def get_todos(filepath=FILEPATH):
    #doc-string for documenting the functions
    """ Read a text file and return the list of
    to-do items.
    """ 
    #Better way to open and read/write a file With-Context-Manager. Doesn't require close() at the end. Once code is executed, the file automatically closes.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    #Value returned
    return todos_local

#Creating custom function to write to a file. Notice nothing to return. Default arguments have to be after non-default arguments
def write_todos(todos_arg, filepath=FILEPATH):
        #doc-string for documenting the functions
        """ Write the to-do items list in the text file."""
        #Better way to open and read/write a file With-Context-Manager. Doesn't require close() at the end. Once code is executed, the file automatically closes.
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)

#If the user runs the code within functions.py, the below message will show. If main.py is run, the message below will not show.
if __name__ == "__main__":
     print("Hello!")
     print(get_todos())