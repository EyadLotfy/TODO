'''This module is made to remove tasks by number'''
def clear_tasks():
    '''This function clears "tasks.txt" file.'''
    try:
        file_handle = open('tasks.txt', 'w')
    except:
        print "You haven't added anything to the TODO list, yet!"
def write_updates_to_tasks_file(task):
    '''This task updates the "tasks.txt" file.'''
    #quick edit done to var task to remove qoutes
    task = list(task)
    del task[0] #removes the first qoute mark
    del task[-1] #remove the last qoute mark
    task = ''.join(task)
    task = task.replace('\\n', '')
    task = task.replace('\\r', '')
    #quick edit done to var task to remove qoutes
    try:
        file_handle = open('tasks.txt', 'a')
        try:
            file_handle.write(task+'\n')
        except:
            print 'Error occured while updating tasks!'
    except:
        print "You haven't added anything to the TODO list, yet!"
def remove_the_desired_task(tasks, task_number):
    '''This function removes the desired task from the in-cache tasks.'''
    if task_number == 0:
        print 'Task was not found!'
        return 0
    try:
        del tasks[task_number]
        clear_tasks()
        if len(tasks) == 1:
            clear_tasks()
            print 'Task was no.1 deleted!'
        else:
            for task in tasks:
                write_updates_to_tasks_file(repr(task))
            print 'Task was no.%i deleted!'%task_number
    except:
        print 'Task was not found!'
def reterieve_tasks():
    '''This function is made to reterieve the tasks from "tasks.txt" file.'''
    try:
        file_handle = open('tasks.txt', 'r')
        tasks = file_handle.readlines()
        return tasks
    except:
        print "You haven't added anything to the TODO list, yet!"
def task_number_promot():
    '''This function is made to ask the user to input the task number.'''
    try:
        task_number = input('Task number? [DELETE] or (-200) to [CLEAR]>>>')
        return task_number
    except:
        print 'Only numbers accepted!'
        return -1
def start():
    '''Staring function.'''
    task_number = task_number_promot()
    if task_number == -200:
        print 'Tasks were cleared!'
        clear_tasks()
        return 0    
    if task_number != -1:
        remove_the_desired_task(reterieve_tasks(), task_number)
    return 1
while True:
    start()
