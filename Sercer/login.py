import time

from django.http import HttpResponse
from django.http import JsonResponse

from Utils.Users.manage import userManage
from Utils.Users.userType import user
from Utils.config import config

def signin(request):
    if request.is_ajax():
        userName = request.GET.get("name")
        pwd = request.GET.get("pwd")
        manager = userManage()
        if isinstance(userName,str) and isinstance(pwd,str):
            if len(userName)>0 and len(pwd)>0:
                u = manager.getUserByName(userName)
                if isinstance(u,user):
                    if u.verifyKey(pwd,decrypto=False):
                        u.signin()
                        r = {
                            "result":"success",
                            "state":u.state,
                            "id":u.id,
                            "stateCode":u.stateCode,
                            "lastSign":u.lastLogin,
                        }
                        return JsonResponse(r)
                    return JsonResponse({"result":"密码错误，请注意大小写！"})
                return JsonResponse({
                    "result":"不存在此用户！"
                })
            return JsonResponse({
                "result":"服务器未获取到用户名和密码！"
            })
        return JsonResponse({
            "result": "服务器未获取到用户名和密码！"
        })
    return HttpResponse("error!")

def signup(request):
    if request.is_ajax():
        name = request.GET.get("name")
        tel = request.GET.get("tel")
        pwd = request.GET.get("pwd")
        # print(name,tel,pwd)
        manager = userManage()
        if isinstance(name,str) and isinstance(pwd,str):
            if len(name)>0 and len(pwd)>0:
                r = manager.createUser(name,pwd)
                if isinstance(r,user):
                    if "@" in tel:
                        r.setEmail(tel)
                    else:
                        try:
                            _ = int(tel)
                            r.setPhone(tel)
                        except:
                            r = {
                                "result":"邮箱或电话号码格式错误！"
                            }
                            print("创建账号失败：", name, "邮箱或电话号码格式错误",tel)
                            return JsonResponse(r)
                    r.signin()
                    r.save()
                    id_ = r.id
                    state = r.state
                    code = r.stateCode
                    t = r.lastLogin
                    r = {
                        "result":"success",
                        "id":id_,
                        "state":state,
                        "stateCode":code,
                        "lastSign":t,
                    }
                    return JsonResponse(r)
                else:
                    print("创建账号失败：",name,"可能是用户名重复")
                    r = {
                        "result":"创建用户失败，可能是用户名重复。"
                    }
                    return JsonResponse(r)
            else:
                r = {
                    "result": "服务器未能获取到正确格式的用户名或密码！"
                }
                print("创建账号失败：", name, "服务器未能获取到正确格式的用户名或密码")
                return JsonResponse(r)
        else:
            r = {
                "result": "服务器未能获取到正确格式的用户名或密码！"
            }
            print("创建账号失败：", name, "服务器未能获取到正确格式的用户名或密码")
            return JsonResponse(r)
    return HttpResponse("error!")

def checkSign(request):
    if request.is_ajax():
        id_ = request.GET.get("id")
        state  = request.GET.get("state")
        stateCode = request.GET.get("stateCode")
        lastSign = request.GET.get("lastSign")
        usermanager = userManage()
        try:
            lastSign = float(lastSign)
        except:
            lastSign=-1.0
        if isinstance(id_,str) and isinstance(stateCode,str):
            if len(id_)>0 and len(stateCode)>0:
                if time.time()-lastSign>config["CheckSignTime"]:
                    u = usermanager.getUser(id_)
                    if isinstance(u,user):
                        if u.stateCode==stateCode:
                            u.signin()
                            stateCode = u.stateCode
                            lastSign = u.lastLogin
                            r = {
                                "result":"success",
                                "id":u.id,
                                "state":u.state,
                                "stateCode":stateCode,
                                "lastSign":lastSign,
                            }
                            return JsonResponse(r)
                        else:
                            r = {
                                "result": "登录超时，验证失败！"
                            }
                            return JsonResponse(r)
                    else:
                        r = {
                                "result":"登录超时，验证失败！"
                            }
                        return JsonResponse(r)
                else:
                    if len(stateCode)>10:
                        u = usermanager.getUser(id_)
                        # print(u)
                        r = {
                            "result": "success",
                            "id": u.id,
                            "state": u.state,
                            "stateCode": stateCode,
                            "lastSign": lastSign,
                        }
                        return JsonResponse(r)
                    else:
                        return JsonResponse({
                            "resul":"登录超时",
                        })
        return JsonResponse({
            "resul":"无登录验证信息",
        })

def getUserNameByID(request):
    if request.is_ajax():
        id_ = request.GET.get("id")
        # print(id_)
        usermanager = userManage()
        name = usermanager.getNameByID(id_)
        # print(name)
        if isinstance(name,str):
            if len(name)>0:
                return JsonResponse({
                    "result":"success",
                    "name":name,
                })
        return JsonResponse({
            "result":"no found!",
        })
    return HttpResponse("error!")