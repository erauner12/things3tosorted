
from pySorted.tasks import AddTask


def add_sorted_task(title, start_date, list_choice):
    """Add a task to Sorted."""
    task = AddTask(title,start_date,list_choice)
    return task.callback_url
