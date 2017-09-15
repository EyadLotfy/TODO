'''this module creates & saves new tasks to "tasks.txt" file.'''
def save_task(task_context):
    '''saves a new task into "tasks.txt" file.'''
    try:
        file_handler = open('tasks.txt', 'a')
        file_handler.write('\n-%s'%task_context)
        return 1
    except IOError:
        return 0
def add_new_task():
    '''adds new task and process it to be saved in "tasks.txt" file.'''
    task_context = raw_input('New task>>>')
    if save_task(task_context) == 1:
        return 1
    else:
        return 0
def start():
    '''starting function.'''
    if add_new_task() == 1:
        return 1
    else:
        return 0
while True:
    if start() == 1:
        print 'New task was saved!'
    else:
        print 'Some failure occured!'
