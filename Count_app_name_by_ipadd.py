# Dang_Khoa_Le_123
#describe: dem so luot truy cap ung dung theo detect_protocol_name va local_ip
import json
import glob,os

listAccess = []
listAccessOk = []

def is_json(json_string):
    try:
        json.loads(json_string)
    except ValueError as e:
        return False
    return True

for filename in os.listdir("24:5e:be:5c:a1:49(1)"):
    with open(os.path.join("24:5e:be:5c:a1:49(1)", filename), 'r') as f:
        text = f.read()
        if is_json(text) == True:
            listObj = json.loads(text)
            for mac_add in listObj['devices']:
                mac_add_list = listObj['devices'][mac_add]
                for i in range (0,len(mac_add_list)):
                    ip_addr = listObj['devices'][mac_add][i]
                    for u in listObj['flows']['br-lan']:
                        try:
                            for in4 in range(0, len(u)):
                                try:
                                    if listObj['flows']['br-lan'][in4]['local_ip'] == ip_addr:
                                        detect_protocol_name = listObj['flows']['br-lan'][in4]['detected_protocol_name']
                                        # print(detect_protocol_name)
                                        list_app_by_ip = []
                                        list_app_by_ip.append(detect_protocol_name)
                                        list_app_by_ip.append(ip_addr)
                                        listAccess.append(list_app_by_ip)                         
                                except:
                                    pass
                        except:
                            pass
        else:
            print("This file is not in json fomat",filename)                    
for u in listAccess:
    if u not in listAccessOk:
        listAccessOk.append(u)

for u in listAccessOk:
    Num_access = listAccess.count(u)
    print(u)
    print(u[0],Num_access)

    data_dict = {
        "Protocol_name" : u[0],
        "Local ip" : u[1],
        "number of appearances" : Num_access
    }
    # print(x, "ok")
    with open("Count_protocol_Name_by_ip_Addr.json", 'a+') as file:
        json.dump(data_dict, file, indent=4)
        file.write(",\n")
