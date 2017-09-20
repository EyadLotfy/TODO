'''This module reads the lines in the file "Tasks.txt", for the user, to see their TODO list.'''
def exit_the_app():
    '''This function exits the app once the user hits enter.'''
    return 1
def read_tasks():
    '''This funciton reads the tasks line by line from "Tasks.txt".'''
    try:
        file_handle = open('tasks.txt', 'r')
        tasks = file_handle.readlines()
        for task_number in range(len(tasks)):
            if task_number != 0:
                if task_number == 1:
                    print '%i %s\n'%(task_number,tasks[-task_number])
                else:
                    print '%i %s'%(task_number,tasks[-task_number])
    except IOError:
        print "You haven't added anything to the TODO list, yet!"
    exit_the_app()
    return 1

def start_read_tasks_for_user():
    '''This is the starting function.'''
    read_tasks()
    return 1

