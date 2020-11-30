from django.urls import path,include
from django.conf.urls import url

from Sercer import login
from Sercer.CustomerManage import CustomerServer
from Sercer.qrcode import getLocalQrCodeImage

urlpatterns = [
    url(r"logup/$",login.signup),
    url(r"signCheck/",login.checkSign),
    url(r"login/$",login.signin),
    url(r"getuserNameByID/$",login.getUserNameByID),
    url(r"getAllCustomer/$",CustomerServer.getAllCustomerInfo),
    url(r"getCustomer/$",CustomerServer.getCustomer),
    url(r"addCustomer",CustomerServer.addCustomer),
    url(r"getQrcode/$",getLocalQrCodeImage),
    url(r"getUserInfoByName/$",CustomerServer.getCustomer),
    url(r"addCustomer/$",CustomerServer.addCustomer),
    url("getModels/$",CustomerServer.getModelList),
]