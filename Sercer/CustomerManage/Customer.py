import os
import pickle
import time
import json
from Utils.config import config
from Utils.createUUID import create as createID
from threading import Thread
class customer():
    def __init__(self,id_,name,phone=None,address=None,buyTime=None,model=None,others=None,record=[],description=[]):
        self.name = name
        self.phone = phone
        self.address = address
        self.buyTime = buyTime
        self.model = model
        self.others = others
        self.record = record
        self.id = id_
        self.description = description

    def setDescription(self,d):
        if isinstance(d,str):
            self.description.append(d)

    def setPhone(self,phone):
        if isinstance(phone,str):
            try:
                _ = int(phone)
                self.phone = phone
            except:
                pass

    def setAddress(self,add):
        if isinstance(add,str):
            self.address = add

    def setModel(self,m):
        if isinstance(m,str):
            self.model = m

    def recordMaintain(self,date,content):
        self.record.append([date,content])

    def save(self):
        path = config["CustomerDataPath"]
        file = os.path.join(path,self.id+"_"+self.name+".pkl")
        fp = open(file,"wb")
        fp.write(pickle.dumps(self))

def createCustomer(name,phone=None,address=None,buyTime=None,model=None,others=None,record=[]):
    CustomerPath = config["CustomerDataPath"].replace("\\","/")
    if os.path.exists(CustomerPath):
        pass
    else:
        os.makedirs(CustomerPath)
    id_ = createID()
    idPool = []
    for each in os.listdir(CustomerPath):
        if each.split(".")[-1] == "pkl" and "_" in each:
            idPool.append(each.split("_")[0])
    while(True):
        if id_ in idPool:
            id_ = createID()
        else:
            break
    id_ = str(id_)
    jugdeModelContains(model)
    c = customer(id_,name,phone=phone,address=address,buyTime=buyTime,model=model,others=others,record=record)
    c.save()

def findSomeOne(name):
    files = []
    for each in os.listdir(config["CustomerDataPath"]):
        if each.split(".")[-1] == "pkl":
            if each.split("_")[-1].split('.')[0] == name:
                files.append(each)
    return files

def loadCustomer(id_):
    for each in os.listdir(config['CustomerDataPath']):
        if each.split("_")[0] == id_:
            f = open(os.path.join(config["CustomerDataPath"],each),"rb")
            c = pickle.loads(f.read())
            f.close()
            return c
    return None

def loadCustomerByName(name):
    r = []
    for each in os.listdir(config["CustomerDataPath"]):
        if each.split("_")[-1].split(".")[0] == name:
            f = open(os.path.join(config["CustomerDataPath"],each))
            c = pickle.loads(f.read())
            f.close()
            r.append(c)
    return r

def findAllCustomer():
    names = []
    for each in os.listdir(config["CustomerDataPath"]):
        name = each.split("_")[-1].split(".")[0]
        if not name in names:
            names.append([each.split("_")[0],name])
    return names

def getCustomerByName(name):
    c = []
    for each in os.listdir(config["CustomerDataPath"]):
        if each.split("_")[-1].split(".")[0] == name:
            f = open(os.path.join(config["CustomerDataPath"],each),"rb")
            cus = pickle.loads(f.read())
            f.close()
            if isinstance(cus,customer):
                c.append(cus)
    return c

class getAllCustomerInfo():
    def __init__(self):
        self.r = []
        self.id_name = []
    def getList(self):
        self.id_name = findAllCustomer()
    def getOneInfo(self,id_):
        u = loadCustomer(id_)
        if isinstance(u,customer):
            info = {
                "name":u.name,
                "id":u.id,
                "model":u.model,
                "buyTime":u.buyTime,
                "others":u.others,
                "record":u.record,
                "phone":u.phone,
            }
            self.r.append(info)
    def getAllUserInfo(self):
        th = []
        self.getList()
        for each in self.id_name:
            t = Thread(target=self.getOneInfo,args=(each[0],))
            th.append(t)
            t.start()
        for each in th:
            each.join()
        return self.r

def jugdeModelContains(model):
    if isinstance(model,str):
        pass
    else:
        return -1
    modelPath = config["modelPath"]
    if not os.path.exists(modelPath):
        f = open(modelPath,"w")
        f.write(json.dumps([model]))
        f.close()
    else:
        f = open(modelPath,"r")
        models = json.loads(f.read())
        f.close()
        if model in models:
            return 0
        else:
            models.append(model)
            with open(modelPath,"w") as f:
                f.write(json.dumps(models))
            return 1
    return -1

def getModels():
    if os.path.exists(config["modelPath"]):
        with open(config["modelPath"],"r") as f:
            models = json.loads(f.read())
            return models
    return []


if __name__ == '__main__':
    os.chdir("../../")
    for i in range(1000):
        createCustomer("测试客户N"+str(i)+"S",model="测试型号"+str(i%13),buyTime="2019-09-23")
    # allCustomer = findAllCustomer()
    # for each in allCustomer:
    #     print(each)
    # finder = getAllCustomerInfo()
    # print(finder.getAllUserInfo())
