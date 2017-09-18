'''This module is made to edit the tasks'''
def clear_tasks():
    '''clear "tasks.txt" file.'''
    try:
        file_handle = open('tasks.txt', 'w')
    except:
        print "You haven't added anything to the TODO list, yet!"
        return -1
def update_tasks(tasks):
    '''update "tasks.txt" file.'''
    if clear_tasks() == -1:
        return -1
    try:
        file_handle = open('tasks.txt', 'a')
        for task in tasks:
            file_handle.write(task)
    except:
        print "You haven't added anything to the TODO list, yet!"
def edit_task(tasks, task_number, new_task):
    '''edits tasks reterieved with the new task edits.'''
    try:
        if task_number+1 == len(tasks):
            tasks[task_number] = '-%s'%new_task
        else:
            tasks[task_number] = '-%s\n'%new_task
        return tasks
    except:
        print 'Task was not found!'
        return -1
def reterieve_tasks():
    '''reterieves tasks from "tasks.txt" file.'''
    try:
        file_handle = open('tasks.txt', 'r')
        tasks = file_handle.readlines()
        return tasks
    except:
        print "You haven't added anything to the TODO list, yet!"
        return 0
def promote_user_to_insert_the_edit():
    '''This function is used to ask the user for the edit'''
    new_task = raw_input('Task edit >>>')
    return new_task
def promote_user_to_insert_task_number():
    '''This function is used to ask the user for the task number.'''
    try:
        task_number = input('Task number? [EDIT]>>>')
    except:
        print 'Only numbers accepted!'
        return -1
    return task_number
def start():
    '''Starting function.'''
    task_number = promote_user_to_insert_task_number()
    if task_number == -1:
        return 0
    if task_number == 0:
        print 'Task was not found!'
        return 0
    tasks = reterieve_tasks()
    if tasks == 0:
        return 0
    edited_tasks = edit_task(tasks, task_number, promote_user_to_insert_the_edit())
    if edited_tasks == -1:
        return 0
    update_tasks(edited_tasks)
    return 1
while True:
    start()
