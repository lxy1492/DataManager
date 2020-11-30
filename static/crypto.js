function encrypto(message) {
    var states= true;
    var encrypted = "";
    $.ajax({
           url:"/Server/PublicKey/",
            dataType:"json",
            async:false,
            success:function (data) {
                if(data["result"]=="success"){
                    key=data["key"];
                    var rsa_encrypt = new JSEncrypt();
                    rsa_encrypt.setPublicKey(key);
                    encrypted = rsa_encrypt.encrypt(message);
                    states = false;
                }else{
                }
            }
        });
    return encrypted;
}