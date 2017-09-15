'''This module reads the lines in the file "Tasks.txt".'''
def exit_the_app():
    '''This function exits the app once the user hits enter.'''
    if raw_input('Please hit enter to exit!') == "\r":
        exit()
    return 1
def read_tasks():
    '''This funciton reads the tasks line by line from "Tasks.txt".'''
    try:
        file_handle = open('tasks.txt', 'r')
        for line_number, line_content in enumerate(file_handle):
            if line_number is not 0:
                print line_number, line_content
    except:
        print "You haven't added anything to the TODO list, yet!"
    exit_the_app()
    return 1
def start():
    '''This is the starting function.'''
    read_tasks()
    return 1
start()
