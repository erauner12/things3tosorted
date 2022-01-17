
import subprocess
import json

def get_today_tasks():
    process = subprocess.run(args=["./bin/things-cli","--json", "today"],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             encoding='utf8')
    return json.loads(process.stdout)