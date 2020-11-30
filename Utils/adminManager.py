import os
from Utils.config import config
from Utils.Users.manage import userManage
from Utils.Users.userType import user

def checkAdminExist():
    adminPath = os.path.join(config["UserPath"],config["AdminID"])
    if os.path.exists(adminPath):
        if os.path.exists(os.path.join(adminPath,"user.pkl")):
            manager = userManage()
            u = manager.getUser(config["AdminID"])
            if isinstance(u,user):
                return True
    if not os.path.exists(adminPath):
        os.makedirs(adminPath)
    manager = userManage()
    u = manager.createUser(name=config["Admin"],key=config["AdminKey"])
    if isinstance(u,user):
        u.id = config["AdminID"]
        u.save()
    return False

