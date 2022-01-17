
"""
A small Python program that uses the npm search API to list
the packages based on a search term.
"""
import sys
import json
import pprint

import subprocess
# import things as api



from lib.things3 import get_today_tasks, update_all_things_tasks
from lib.sorted3 import add_all_things_tasks



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


if __name__ == "__main__":
   # Make API call to fetch the npm search results and assign it to a variable
    # npm_search_results = requests.get(NPM_API_URL).json()
    # https://github.com/thingsapi/things.py/
    # things_search_results = things.todos()
    
    
    # get a list of all today tasks
    json_list = get_today_tasks()
    
    
    # pp.pprint(json_list)
    
    # get a list of all today tasks that DO NOT contain a tag named "sorted3"
    no_sorted_tag = [x for x in json_list
                     if x.get("tags",["fallback"]) is not None
                     and x.get("type") == "to-do"]
    
    pp.pprint(no_sorted_tag)
    
    # Add them to sorted
    # add_all_things_tasks(no_sorted_tag)
                         
    # Add "sorted3" tag to all things3 tasks that were just added to sorted
    # Need uuid of each things3 task
    auth_token = "zHtl26BeQnW5CuTDxgAfBw"
    # update_all_things_tasks(auth_token, no_sorted_tag)
    
    
    # # A Script Filter is required to return an items array of zero or more items.
    # # Each item describes a result row displayed in Alfred.
    # alfred_json = json.dumps({
    #     "items": get_alfred_items(json_list)
    # }, indent=2)

    # # # Pass the formatted JSON data back to Alfred
    # sys.stdout.write(alfred_json)
