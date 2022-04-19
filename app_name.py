import json 
import glob,os ,pandas as pd
import os
import simplejson as load
from importlib.resources import path
appVal = {}
def is_json(json_string):
  try:
    json.loads(json_string)
  except ValueError as e:
    return False
  return True
if os.path.isfile('appdata.json'):
    with open("appdata.json", 'r') as fp:
        j = json.load(fp)
else:
    json_obj = json.dumps(appVal, indent=4)
    with open('appdata.json', 'w') as f:
        f.write(json_obj)
        j = json.loads(json_obj)
app_name = []
for filename in os.listdir("24:5e:be:5c:a1:49"):
    with open(os.path.join("24:5e:be:5c:a1:49", filename), 'r') as f:
        text = f.read()
        if is_json(text):
            listObj = json.loads(text)
            for flow_entry in listObj['flows']['br-lan']:
                app_name.append(flow_entry['detected_application_name'])
                

        else:
            print("This file is not in json fomat",filename)
newAppname = list(dict.fromkeys(app_name))
for i in newAppname:
    if i not in j:
      newApp = {i : app_name.count(i)}
      j.update(newApp)
    else:
      updateApp = {i : app_name.count(i)+j[i] }
      del j[i]
      j.update(updateApp)

x_file_name = 'appdata.json'
with open(x_file_name, 'w') as json_file:
    str_rp = str(j)
    str_rp = str_rp.replace("'",'"')
    json_file.write(str_rp)
