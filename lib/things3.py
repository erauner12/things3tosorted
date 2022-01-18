from pyThings.tasks import UpdateTask

import subprocess
import json

auth_token = "zHtl26BeQnW5CuTDxgAfBw"

def get_today_tasks():
    process = subprocess.run(args=["./bin/things-cli","--json", "today"],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             encoding='utf8')
    return json.loads(process.stdout)
    
def update_task_tag(task_id, add_tags):
        UpdateTask(auth_token=auth_token, task_id=task_id, add_tags=add_tags)

    
