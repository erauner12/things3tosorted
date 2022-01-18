
"""
A small Python program that uses the npm search API to list
the packages based on a search term.
"""
import sys
import json

from lib.things3 import get_today_tasks
from lib.sorted3 import add_all_things_tasks


# Retrieve user input from Alfred

# Not receiving user input yet leaving commented
# search_query = sys.argv[1]

# Build the search URL with the user inputted search term appended as the query param
# NPM_API_URL = "https://www.npmjs.com/search/suggestions?q=" + search_query

# Not doing anything yet, leaving commented
# def get_formatted_results(search_results):
#     formatted_results = []
#     for item in search_results:
#         result = {
#             "title": item["title"],
#             "subtitle": item["notes"] if "notes" in item else "",
#             "arg": item["uuid"],
#             "autocomplete": item["title"],
#             "icon": {
#                 "path": "./n-64.png"
#             }
#         }
#         formatted_results.append(result)

#     return formatted_results

# Not doing anything yet, leaving commented
# def get_alfred_items(search_results):
#     if len(search_results) == 0:
#         result = {
#             "title": "No packages found.",
#             "subtitle": "Enter in a new search term",
#         }
#         return [result]
#     else:
#         return get_formatted_results(search_results)


if __name__ == "__main__":
    
    # get a list of all today tasks
    json_list = get_today_tasks()
    
    # get a list of all today's to-do tasks (not projects)
    no_sorted_tag = [x for x in json_list
                     if x.get("tags",["fallback"]) is not None
                     and x.get("type") == "to-do"]
    
    add_all_things_tasks(no_sorted_tag)
    
    # Not doing anything yet, leaving commented
    # alfred_json = json.dumps({
    #     "items": get_alfred_items(json_list)
    # }, indent=2)

    # # # Pass the formatted JSON data back to Alfred
    
    # Not doing anything yet, leaving commented
    # sys.stdout.write(alfred_json)
