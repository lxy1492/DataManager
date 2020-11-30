# #-*- coding:utf-8 -*-
# from Crypto import Random
# from Crypto.Hash import SHA
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
# from Crypto.PublicKey import RSA
#
#
# # windows环境下用一下方式引入crypto
#
#
# import base64,os
# from LxyWebSite.settings import BASE_DIR
#
# def create_key():
#     # 伪随机数生成器
#     random_generator = Random.new().read
#     # rsa算法生成实例
#     rsa = RSA.generate(1024, random_generator)
#     # A的秘钥对的生成
#     private_key = rsa.exportKey()
#     publick_key = rsa.publickey().exportKey()
#     publick_path = os.path.join(BASE_DIR,"DataBase/key/public.pem")
#     private_path = os.path.join(BASE_DIR,"DataBase/key/private.pem")
#     with open(private_path,"wb") as f:
#         f.write(private_key)
#     with open(publick_path,"wb") as f:
#         f.write(publick_key)
#
# def get_publickKey():
#     publick_path = os.path.join(BASE_DIR, "DataBase/key/public.pem")
#     with open(publick_path,"r") as f:
#         return f.read()
#
# def encypt_withPublicKey(message):
#     publick_path = os.path.join(BASE_DIR, "DataBase/key/public.pem")
#     with open(publick_path) as f:
#         key = f.read()
#         rsakey = RSA.importKey(str(key))
#         cipher = Cipher_pkcs1_v1_5.new(rsakey)
#         cipher_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
#         return cipher_text
#
# def deEncrypt_withPrivateKey(message):
#     private_path = os.path.join(BASE_DIR, "DataBase/key/private.pem")
#     with open(private_path) as f:
#         key = f.read()
#         rsakey = RSA.importKey(key)
#         cipher = Cipher_pkcs1_v1_5.new(rsakey)
#         text = cipher.decrypt(base64.b64decode(message),None)
#         return text
#
# def signature(message):
#     private_path = os.path.join(BASE_DIR, "DataBase/key/private.pem")
#     with open(private_path) as f:
#         key = f.read()
#         rsakey = RSA.importKey(key)
#         signer = Signature_pkcs1_v1_5.new(rsakey)
#         digest = SHA.new()
#         digest.update(message.encode("utf8"))
#         sign = signer.sign(digest)
#         signature = base64.b64encode(sign)
#         return signature
#
# def verify(message):
#     publick_path = os.path.join(BASE_DIR, "DataBase/key/public.pem")
#     with open(publick_path) as f:
#         key = f.read()
#         rsakey = RSA.importKey(key)
#         verifier = Signature_pkcs1_v1_5.new(rsakey)
#         digest = SHA.new()
#         digest.update(message.encode("utf8"))
#         is_verify = verifier.verify(digest, base64.b64decode(signature))
#         return is_verify
#

def enCrypto(message):
    return message

def deCrypto(message):
    return message

# if __name__ == '__main__':
#     os.chdir("../")
#     msg = "hello pycrypto"
#     t = encypt_withPublicKey(msg)
#     d = deEncrypt_withPrivateKey(t)
#     print(d)