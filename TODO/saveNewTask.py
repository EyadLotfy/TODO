def save_task(task_context):
    try:
        file = open('tasks.txt','a')
        file.write('\n-%s'%task_context)
        return 1
    except:
        return 0

def add_new_task():
    task_context = raw_input('New task>>>')
    if save_task(task_context) == 1:
        return 1
    else:
        return 0
    
def start():
    if add_new_task() == 1:
        return 1
    else:
        return 0

while True:
    if start() == 1:
        print('New task was saved!')
    else:
        print('Some failure occured!')
