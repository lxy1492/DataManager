import os
import re
import base64
import qrcode
import socket
from io import BytesIO
from PIL import Image

from django.http import HttpResponse
from django.http import JsonResponse

from Utils.config import config

def createQrcode(message,boxSize=10,border=4,make_fit=True):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxSize,
        border=border,
    )
    if isinstance(message,str):
        qr.add_data(message)
        qr.make(fit=make_fit)
        image = qr.make_image()
        return image
    return None

def createQrcodeWithPhotoAndColor(message,boxsize=10,border=4,make_fit=True,fill_color="black",back_color="white",photo=None,logoSizeFactor=6,transforBase64=False):
    if not isinstance(message,str):
        return None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=boxsize,
        border=border,
    )
    qr.add_data(message)
    qr.make(make_fit)
    image = qr.make_image(fill_color=fill_color,back_color=back_color)
    if photo!=None:
        if os.path.exists(photo):
            icon = Image.open(photo)
            imag_w,image_h = image.size
            factor =  logoSizeFactor
            size_w = int(imag_w/factor)
            size_h = int(image_h/factor)
            icon_w, icon_h = icon.size
            if icon_w>size_w:
                icon_w = size_w
            if icon_h> size_h:
                icon_h = size_h
            icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)
            w= int((imag_w-icon_w)/2)
            h = int((image_h-icon_h)/2)
            image.paste(icon,(w,h),mask=None)
    if transforBase64:
        image = transforPILToBase64(image)
    return image

def transforPILToBase64(pil_image):
    output_buffer = BytesIO()
    pil_image.save(output_buffer,format="JPEG")
    bytedata = output_buffer.getvalue()
    base64str = base64.b64encode(bytedata)
    return base64str

def convertBase64ToPIL(base64_image):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_image)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    image = Image.open(image_data)
    return image

def getLocalQrCodeImage(request):
    if request.is_ajax():
        ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        add = "http://"+ip+":"+config["Port"]
        image = createQrcode(add,border=2)
        image = transforPILToBase64(image)
        base64_image ="data:image/jpeg;base64," + image.decode()
        return JsonResponse({
            "result":"success",
            "image":base64_image,
        })
    return HttpResponse("error!")