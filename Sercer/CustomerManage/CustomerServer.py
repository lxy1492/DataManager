import os
from threading import Thread
from django.http import HttpResponse
from django.http import JsonResponse

from Utils.config import config
from Sercer.CustomerManage import Customer,customer

def getAllCustomerInfo(request):
    if request.is_ajax():
        finder = Customer.getAllCustomerInfo()
        r = finder.getAllUserInfo()
        return JsonResponse({
            "result":"success",
            "data":r,
        })
    return HttpResponse("error!")

def getCustomer(request):
    if request.is_ajax():
        name = request.GET.get("data")
        userid = request.GET.get("userid")
        customerFIles = Customer.getCustomerByName(name)
        models = []
        buyTime = []
        market = []
        recv = []
        others = []
        phone = "暂无联系电话"
        for each in customerFIles:
            if isinstance(each,customer):
                if each.model!=None:
                    models.append(each.model)
                if each.buyTime!=None:
                    buyTime.append(each.buyTime)
                if len(each.description)>0:
                    market.extend(each.description)
                if len(each.record)>0:
                    recv.extend(each.record)
                if each.others!=None:
                    others.append(each.others)
                phone = each.phone
        production = ""
        for each in models:
            production += ";"
            production += each
        buyt = buyTime[0]
        for each in buyTime:
            if each>buyt:
                buyt=each
        market = "暂无此客户描述信息！"
        production = "购买型号："+production[1:]
        r = {
            "result":"success",
            "production":production,
            "name":name,
            "phone":phone,
            "buyTime":buyt,
            "marked":market,
        }
        return JsonResponse(r)
    return HttpResponse("error!")



def addCustomer(request):
    if request.is_ajax():
        name = request.GET.get("name")
        model = request.GET.get("model")
        phone = request.GET.get("phone")
        others = request.GET.get("others")
        date = request.GET.get("date")
        Thread(target=Customer.jugdeModelContains,args=(model,)).start()
        Customer.createCustomer(name,phone,buyTime=date,model=model,others=others)
        return JsonResponse({"result":"success"})
    return HttpResponse("error!")

def getModelList(request):
    if request.is_ajax():
        r = Customer.getModels()
        return JsonResponse({
            "result":"success",
            "models":r
        })
    return HttpResponse("error!")

if __name__ == '__main__':
    os.chdir("../../")
    # getAllCustomerInfo("ds")
    print(Customer.getModels())