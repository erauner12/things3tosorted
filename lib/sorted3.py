
from pySorted.tasks import AddTask

from datetime import date

from lib.things3 import update_task_tag



def add_all_things_tasks(things_tasks_list):
    """Adds all tasks from Sorted."""
    
    today_date = date.today().strftime('%Y-%m-%d')
    for task in things_tasks_list:
        if "sorted3" not in task.get("tags","fallback"):
            # TODO: You should be passing these as args so that you do not have to handle errors like this
            try:
                add_sorted_task(task["title"],today_date,"things3","10","30",task["tags"])
                update_task_tag(task["uuid"], add_tags=["sorted3"])
            except KeyError as e:    
                add_sorted_task(task["title"],today_date,"things3","10","30",["None"])
                update_task_tag(task["uuid"], add_tags=["sorted3"])
                
    
    
    

def add_sorted_task(title, start_date, list_choice, earlyAlert, duration, tags):
    """Add a task to Sorted."""
    task = AddTask(title,start_date,list_choice, earlyAlert, duration, tags)
    return task.callback_url
