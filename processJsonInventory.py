import json
import glob, sys

  
# Opening JSON file
f = open(sys.argv[1])
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for minion in data["data"]["minions"]:
    print("minion_" + str(minion["type"]) + "," + minion["name"])
  
# Closing file
f.close()