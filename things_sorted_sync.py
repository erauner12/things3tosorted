
"""
A small Python program that uses the npm search API to list
the packages based on a search term.
"""
import sys
import json
import pprint

import subprocess
# import things as api

from pyThings import Tasks

from lib.things3 import get_today_tasks


pp = pprint.PrettyPrinter(indent=4)



# Retrieve user input from Alfred
# search_query = sys.argv[1]

# Build the search URL with the user inputted search term appended as the query param
# NPM_API_URL = "https://www.npmjs.com/search/suggestions?q=" + search_query


def get_formatted_results(search_results):
    formatted_results = []
    for item in search_results:
        result = {
            "title": item["title"],
            "subtitle": item["notes"] if "notes" in item else "",
            "arg": item["uuid"],
            "autocomplete": item["title"],
            "icon": {
                "path": "./n-64.png"
            }
        }
        formatted_results.append(result)

    return formatted_results

def get_alfred_items(search_results):
    if len(search_results) == 0:
        result = {
            "title": "No packages found.",
            "subtitle": "Enter in a new search term",
        }
        return [result]
    else:
        return get_formatted_results(search_results)


def getProcessOutput(cmd):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE)
    process.wait()
    data, err = process.communicate()
    if process.returncode == 0:
        return data.decode('utf-8')
    else:
        print("Error:", err)
    return ""

if __name__ == "__main__":
   # Make API call to fetch the npm search results and assign it to a variable
    # npm_search_results = requests.get(NPM_API_URL).json()
    # https://github.com/thingsapi/things.py/
    # things_search_results = things.todos()
    
    # get a list of all today tasks
    json_list = get_today_tasks()
    
    
    pp.pprint(json_list)
    
    # get a list of all today tasks that contain a tag named "test"
    list_json = [x for x in json_list if x.get("tags") is not None if "test" in x["tags"]]
    
    
    
    # A Script Filter is required to return an items array of zero or more items.
    # Each item describes a result row displayed in Alfred.
    alfred_json = json.dumps({
        "items": get_alfred_items(json_list)
    }, indent=2)

    # # Pass the formatted JSON data back to Alfred
    sys.stdout.write(alfred_json)
