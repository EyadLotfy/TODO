'''This module reads the lines in the file "Tasks.txt", in correct order to, '''
'''This module reads the lines in the file "Tasks.txt", in correct order to, promote the user to make changes like [EDIT], [DONE], [DELETE]'''
def exit_the_app():
    '''This function exits the app once the user hits enter.'''
    return 1
def read_tasks():
    '''This funciton reads the tasks line by line from "Tasks.txt".'''
    try:
        file_handle = open('tasks.txt', 'r')
        for line_number, line_content in enumerate(file_handle):
            if line_number is not 0:
                print line_number, line_content
    except IOError:
        print "You haven't added anything to the TODO list, yet!"
    exit_the_app()
    return 1

def start_read_tasks():
    '''This is the starting function.'''
    read_tasks()
    return 1

