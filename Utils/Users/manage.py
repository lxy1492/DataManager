import os
import json
import shutil
import pickle
from Utils.config import config
from Utils.Users import userType
from Utils import createUUID


class userManage():
    def __init__(self):
        self.userPath = config["UserPath"]

    def createUser(self,name,key,phone=None,email=None,image=None,sex=None,age=-1):
        if os.path.exists(config["UserIDPool"]):
            id_pool = json.loads(open(config["UserIDPool"]).read())
        else:
            id_pool = []
        id = createUUID.create()
        while(True):
            c = False
            for each in id_pool:
                if id in each:
                    c = True
                    id = createUUID.create()
                if name in each:
                    name=False
                    c = False
            if c == False:
                break
        if name==False:
            return -1
        user = userType.user(name=name,key=key,sex=sex,age=age)
        user.setId(id)
        user.setPhone(phone)
        user.setEmail(email)
        user.save()
        id_pool.append([id,name])
        with open(config["UserIDPool"],"w") as f:
            f.write(json.dumps(id_pool))
            return user

    def findALLUserID(self):
        userlist = os.listdir(config["UserPath"])
        users = []
        for each in os.listdir(userlist):
            if os.path.isdir(os.path.join(config["UserPath"],each)):
                if os.path.exists(os.path.join(config["UserPath"],each,"user.pkl")):
                    users.append(users)
        return users

    def getUser(self,id):
        if os.path.exists(os.path.join(config["UserPath"],id)):
            if os.path.exists(os.path.join(config["UserPath"],id,"user.pkl")):
                user = userType.loadUser(Path=os.path.join(config["UserPath"],id,"user.pkl"))
                return user
        return None

    def getUserByName(self,name):
        if os.path.exists(config["UserIDPool"]):
            pass
        else:
            self.recreateIDPool()
        id_pool = self.loadIDPool()
        if id_pool!=None:
            for each in id_pool:
                if each[1] == name:
                    path = os.path.join(config["UserPath"],each[0],"user.pkl")
                    user = userType.loadUser(Path=path)
                    return user
        return None

    def getNameByID(self,id):
        if os.path.exists(os.path.join(config["UserPath"],id)):
            u = userType.loadUser(id=id)
            if isinstance(u,userType.user):
                return u.name
            return None
        return None

    def getIDByName(self,name):
        if os.path.exists(config["UserIDPool"]):
            pass
        else:
            self.recreateIDPool()
        id_pool = self.loadIDPool()
        if id_pool!=None:
            for each in id_pool:
                if each[1] == name:
                    return each[0]
        return None

    def loadIDPool(self):
        if os.path.exists(config["UserIDPool"]):
            f = open(config["UserIDPool"])
            data = f.read()
            f.close()
            return json.loads(data)
        return None

    def recreateIDPool(self):
        userList = self.findALLUserID()
        id_pool = []
        for each in userList:
            path = os.path.join(config["UserPath"],each,"user.pkl")
            user = userType.loadUser(Path=path)
            if isinstance(user,userType.user):
                id_pool.append([each,user.name])
        with open(config["UserIDPool"],"w") as f:
            f.write(json.dumps(id_pool))

    def removeUser(self,id=None,name=None):
        if id==None and name==None:
            return -1
        if isinstance(id, str):
            path = os.path.join(config["UserPath"], id)
            if os.path.exists(path):
                shutil.rmtree(path)
                self.removeFromIDPool(id)
                return 0
        if isinstance(name,str):
            id = self.getNameByID(id)
            return self.removeUser(id=id)
        return -1

    def removeFromIDPool(self,key):
        id_pool = self.loadIDPool()
        for each in id_pool:
            if key in each:
                id_pool.remove(each)
        with open(config["UserIDPool","w"]) as f:
            f.write(json.dumps(id_pool))

    def changePassWord(self,user,p,decrypto=False):
        if isinstance(user,userType.user):
            user.setPassWord(p,decrypto=decrypto)
            return 0
        elif isinstance(user,str):
            id_pool = self.loadIDPool()
            for each in id_pool:
                if user in each:
                    if each.index(user)==0:
                        userobj = self.getUser(user)
                    else:
                        userobj = self.getUserByName(user)
                    if isinstance(userobj,userType.user):
                        return self.changePassWord(userobj,p,decrypto)
        return -1