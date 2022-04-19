import json
import os
import simplejson as load
from importlib.resources import path

OutPut = {}

def is_json(json_string):
  try:
    json.loads(json_string)
  except ValueError as e:
    return False
  return True

# with open('1648973804.json') as json_file:
#     data = json.load(json_file)

if os.path.isfile('toai.json'):
    with open("toai.json", 'r') as fp:
        j = json.load(fp)
else:
    json_obj = json.dumps(OutPut, indent=4)
    with open('toai.json', 'w') as f:
        f.write(json_obj)
        j = json.loads(json_obj)

for filename in os.listdir("24:5e:be:5c:a1:49"):
    with open(os.path.join("24:5e:be:5c:a1:49", filename), 'r') as f:
        text = f.read()
        if is_json(text) == True:
            listObj = json.loads(text)
            for flow_entry in  listObj['flows']['br-lan']:
                if flow_entry['detected_application_name'] in j:
                    if flow_entry['other_ip'] not in j[flow_entry['detected_application_name']]['ip_list']:
                        print(flow_entry['other_ip'])
                        new_ip_data_set = {flow_entry['other_ip']: flow_entry['other_port']}
                        j[flow_entry['detected_application_name']]['ip_list'].update(new_ip_data_set)
                    if "host_server_name" in flow_entry:
                        if flow_entry['host_server_name'] not in j[flow_entry['detected_application_name']]['host_server_name'] :
                            print(flow_entry['host_server_name'])
                            j[flow_entry['detected_application_name']]['host_server_name'].append(flow_entry['host_server_name'])
                else:
                    ip = { flow_entry['other_ip']: flow_entry['other_port']}
                    if "host_server_name" in flow_entry:
                        host = [flow_entry['host_server_name']]
                    else:
                        host = []
                    new_data_set =  { flow_entry['detected_application_name'] : { "ip_list" : ip, "host_server_name" : host } }
                    j.update(new_data_set)
        else:
            print("This file is not in json fomat",filename)

x_file_name = 'toai.json'
with open(x_file_name, 'w') as json_file:
    str_rp = str(j)
    str_rp = str_rp.replace("'",'"')
    json_file.write(str_rp)
