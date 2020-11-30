import os
import pickle
import time
from Utils.config import config
from Utils import cryptoManage
from Utils import createUUID

class user():
    def __init__(self,name=None,id=None,phone=None,email=None,key=None,state="off",stateCode=None,sex=None,age=-1):
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email
        self.key = key
        self.sex = sex
        self.age = age
        self.state = state
        self.stateCode = stateCode
        self.ip = None
        self.leavel = 0
        self.lastLogin = -1
        self.faceImage = None

    def setName(self,name):
        if isinstance(name,str):
            self.name = name
            return 0
        return -1

    def setPhone(self,phonenumber):
        if isinstance(phonenumber,str):
            self.phone = phonenumber
            return 0
        return -1

    def setEmail(self,email):
        if isinstance(email,str):
            if "@" in email:
                self.email = email
                return 0
        return -1

    def setLeaval(self,l):
        if isinstance(l,int):
            if l>=0:
                self.leavel = l
                return 0
        return -1

    def setip(self,ip):
        if isinstance(ip,str):
            if "." in ip:
                for each in ip.split("."):
                    try:
                        _ = int(each)
                    except:
                        return -1
                self.ip = ip
                return 0
        return -1

    def setImagePath(self,path):
        if isinstance(path,str):
            if os.path.exists(path):
                self.faceImage = path
                return 0
        return -1

    def setState(self,state):
        if isinstance(state,str):
            if state in ["on","off"]:
                self.state = state
                return 0
        return -1

    def setStateCode(self,stateCode):
        if isinstance(stateCode,str):
            if len(stateCode)>10:
                self.stateCode = stateCode
                return 0
        return -1

    def signin(self):
        stateCode = createUUID.create()
        self.setStateCode(stateCode)
        self.setState("on")
        self.setLastLogin(time.time())
        self.save()

    def signoff(self):
        self.setStateCode("")
        self.setState("off")
        self.save()

    def setKey(self,key):
        self.key = key
        return 0

    def setLastLogin(self,t):
        if isinstance(t,float):
            if t>0:
                self.lastLogin = t
                return 0
        return -1

    def setId(self,id):
        if isinstance(id,str):
            self.id = id

    def save(self):
        dirPath = os.path.join(config["UserPath"],self.id)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        path = os.path.join(config["UserPath"],self.id,"user.pkl")
        with open(path,"wb") as f:
            f.write(pickle.dumps(self))

    def verifyKey(self,key,decrypto=True):
        if decrypto:
            key = cryptoManage.deCrypto(key)
        if key==self.key:
            return True
        return False

    def setPassWord(self,p):
        if isinstance(p,str):
            if len(p)>=3:
                self.key = p

    def changePassWord(self,password,decrypto=False):
        if decrypto:
            password = cryptoManage.deCrypto(password)
        self.setPassWord(password)

    def __str__(self):
        string = "name:"+str(self.name)+";"
        string += "sex:"+str(self.sex)+";"
        string += "age:"+str(self.age)+";"
        string += "id:"+str(self.id)+";"
        string += "phone:"+str(self.phone)+";"
        string += "email:"+str(self.email)+";"
        string += "state:"+str(self.state)+";"
        string += "stateCode:"+str(self.stateCode)+";"
        return string


def loadUser(id=None,Path=None):
    if id==None and Path==None:
        return None
    if isinstance(id,str):
        path = os.path.join(config["UserPath"],id,"user.pkl")
        if os.path.exists(path):
            with open(path,"rb") as f:
                try:
                    user = pickle.loads(f.read())
                    return user
                except:
                    print("读取用户对象失败：",id)
                    return None
    if isinstance(Path,str):
        if os.path.exists(Path):
            if os.path.isfile(Path):
                with open(Path, "rb") as f:
                    try:
                        user = pickle.loads(f.read())
                        return user
                    except:
                        print("读取用户对象失败：", Path)
                        return None
            else:
                if os.path.isfile(os.path.join(Path,"user.pkl")):
                    with open(os.path.join(Path,"user.pkl"),"rb") as f:
                        try:
                            user = pickle.loads(f.read())
                            return user
                        except:
                            print("读取用户对象失败：", Path)
                            return None
    return None