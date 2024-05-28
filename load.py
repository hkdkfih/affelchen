import json
import requests

def load(name):
    # 从给定URL加载JSON文件并将其解析为Python对象
    with open("config.json", "r") as openfile:
        server = json.load(openfile)["server_url"]
    json_name = name+".json"
    try:
        r = requests.get(server+"/"+json_name)
    except:
        return None
    if r.status_code == 404:
        return None
    json_object = json.loads(r.text)
    return json_object

def save(name, save_dict):
    # 将给定的Python字典保存为JSON文件
    json_name = name+".json"
    with open(json_name, "w") as openfile:
        json.dump(save_dict, openfile)