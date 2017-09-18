'''This module is made to provide interface for the user'''
from savenewtask import start_new_task
from readtasks import start_read_tasks
from markdone import start_mark_done
from edittask import start_edit_task
from deletetask import start_delete_task
#All functions imported are listed here!
#start_new_task()
#start_read_tasks()
#start_mark_done()
#start_edit_task()
#start_delete_task()
#All functions imported are listed here!
def start_instructions():
    '''This function gives instructions to the user about how to use Qweedo'''
    print '-Use one of the following commands to perform an operation-'
    print '0 - To save a new task.'
    print '1 - To read tasks.'
    print '2 - To mark a task as done.'
    print '3 - To edit a task.'
    print '4 - To remove a certain task or clear all tasks.'
    print '5 - To list all the available commands again.'
start_instructions()
while True:
    try:
        command_number = input('command number? >>>')
        if command_number == 0:
            start_new_task()
        elif command_number == 1:
            start_read_tasks()
        elif command_number == 2:
            start_read_tasks()
            start_mark_done()
        elif command_number == 3:
            start_read_tasks()
            start_edit_task()
        elif command_number == 4:
            start_read_tasks()
            start_delete_task()
        elif command_number == 5:
            start_instructions()
        else:
            print 'command wasn not recognized.'
    except:
        start_instructions()
    
