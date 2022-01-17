from pyThings.tasks import UpdateTask

import subprocess
import json

def get_today_tasks():
    process = subprocess.run(args=["./bin/things-cli","--json", "today"],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             encoding='utf8')
    return json.loads(process.stdout)


def update_all_things_tasks(auth_token, things3_today_tasks):
    for item in things3_today_tasks:
        update_task(auth_token, item["uuid"], add_tags=["sorted3"])
    
def update_task(auth_token, task_id, add_tags):
        UpdateTask(auth_token=auth_token, task_id=task_id, add_tags=add_tags)

    
