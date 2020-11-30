import os
import json

DataBase = "./DataBase"

config = {

    "Port":"2020",
    
    "DataPath":DataBase,
    "ConfigPath":os.path.join(DataBase,"Config","config.json").replace("\\","/"),
    "UserPath":os.path.join(DataBase,"User").replace("\\","/"),
    "UserIDPool":os.path.join(DataBase,"User","UID.json").replace("\\","/"),
    "CheckSignTime":180,

    "Admin":"admin",
    "AdminID":"001",
    "AdminKey":"123456",

    "CustomerDataPath":os.path.join(DataBase,"Customer").replace("\\","/"),

    "modelPath":os.path.join(DataBase,"model.json").replace("\\","/"),
}

def createConfig(data = config):
    dirPath = os.path.dirname(config["ConfigPath"]).replace("\\","/")
    # print(dirPath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    if os.path.exists(dirPath):
        f = open(config["ConfigPath"],"w")
    else:
        f = open(config["ConfigPath"],"w")
    config_dir = json.dumps(data)
    f.write(config_dir)
    f.close()

def loadConfig(path=None):
    global config
    if path!=None:
        if isinstance(path,str):
            if os.path.exists(path):
                f = open(path,"r")
                config = json.loads(f.read())
                f.close()
    if os.path.exists(config["ConfigPath"]):
        f = open(config["ConfigPath"],"r")
        config = json.loads(f.read())
        f.close()
    else:
        createConfig()

if __name__ == '__main__':
    os.chdir("../")
    createConfig()
