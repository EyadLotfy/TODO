'''This module is built to mark tasks as "Done" in "tasks.txt" file.'''
def rewrite_tasks_file(file_lines):
    '''This function is used to rewrite the "tasks.txt" file, to update the "Done" tasks.'''
    file_handle = open('tasks.txt', 'w')
    file_handle.write('\r')
    for line in file_lines:
        file_handle.write('\r%s'%line)
    print 'Task was marked [DONE]!'
    return 1
def mark_task_as_done(line_number):
    '''This function is used to mark tasks in "tasks.txt" as "Done".'''
    try:
        file_handle = open('tasks.txt', 'r')
        file_lines = file_handle.readlines()
    except IOError:
        print "You haven't added anything to the TODO list, yet!"
        return 0
    try:
        line_to_mark_as_done = file_lines[line_number]
        if '[DONE]' in line_to_mark_as_done:
            print 'Task is already done!'
            return 1
        #Applying some changes to the line in order to include\
        #the [DONE] mark and reposition the '-' mark.
        line_to_mark_as_done = line_to_mark_as_done.replace('-', ' ')
        file_lines[line_number] = '-[DONE]' + line_to_mark_as_done
        rewrite_tasks_file(file_lines)
        return 1
    except IOError:
        print 'Task was not found!'
        return 0
    except IndexError:
        print 'Task was not found!'
        return 0
def insert_task_number():
    '''This function asks the user to insert the task number to mark it as "Done".'''
    try:
        line_number = input('Task number? [Done] >>>')
        return line_number
    except NameError:
        print 'Only numbers accepted!'
        return 0
def start():
    '''Staring function!'''
    while True:
        task_number = insert_task_number()
        if task_number == 0 :
            print 'Task was not found!'
        else:
            mark_task_as_done(task_number)
    return 1
start()
