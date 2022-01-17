
from pySorted.tasks import AddTask

from datetime import date


def add_all_things_tasks(things_tasks_list):
    """Adds all tasks from Sorted."""
    
    for task in things_tasks_list:
        today_date = date.today().strftime('%Y-%m-%d')
        add_sorted_task(task["title"],today_date,"things3","10","30",task["tags"])
    
    
    

def add_sorted_task(title, start_date, list_choice, earlyAlert, duration, tags):
    """Add a task to Sorted."""
    task = AddTask(title,start_date,list_choice, earlyAlert, duration, tags)
    return task.callback_url
