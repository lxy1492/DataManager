function setLogin(data) {
    localStorage.setItem("id",data["id"]);
    localStorage.setItem("state",data["state"]);
    localStorage.setItem("stateCode",data["stateCode"]);
    localStorage.setItem("lastSign",data["lastSign"]);
}

function logup(data) {
    loged = false;
    var r = "";
    $.ajax({
        url:"/server/logup/",
        data:data,
        async:false,
        dataType:"json",
        success:function (data) {
            if (data["result"]=="success"){
                setLogin(data);
                loged = true;
                r = data["result"];
            }else{
                r = data["result"];
            }
        }
    });
    if (loged==true){
        return r
    }else{
        return r
    }
}

function login(data) {
    r = "";
    $.ajax({
        url:"/server/login/",
        data:data,
        dataType:"json",
        async: false,
        success:function (data) {
            if (data["result"]=="success"){
                setLogin(data);
                r = "success";
                setLogin(data);
            }else{
                r = data["result"];
            }
        }
    });
    return r
}

function checkSignIn() {

    id = localStorage.getItem("id");
    state = localStorage.getItem("state");
    stateCode = localStorage.getItem("stateCode");
    lastSign = localStorage.getItem("lastSign");

    $.ajax({
        url:"/server/signCheck/",
        data:{id:id,state:state,stateCode:stateCode,lastSign:lastSign},
        dataType:"json",
        async:false,
        success:function (data) {
            if (data["result"]=="success"){
                setLogin(data);
            }else{
                window.location.href = "/login/";
            }
        }
    });
}

function getNameByID() {
    id_ = localStorage.getItem("id");
    var r;
        $.ajax({
            url:"/server/getuserNameByID/",
            data:{id:id_},
            dataType:"json",
            async:false,
            success:function (data) {
                if(data["result"]=="success"){
                    r = data["name"];
                    return r
                }else{
                    r = "未登录";
                }
            }
        });
        return r
}

function getWebQRcode() {
    $.ajax({
        url:"/server/getQrcode/",
        data:{data:""},
        dataType:"json",
        async:false,
        success:function (data) {
            // console.log(data);
            if (data["result"]=="success"){
                $("#logoImage").attr("src",data["image"]);
                $("#logoImage").width(120);
            }
            }

    });
}

function isEmpty(obj){
    if(typeof obj == "undefined" || obj == null || obj == ""){
        return true;
    }else{
        return false;
    }
}

function stringContains(str1,str2) {
    index_ = str1.indexOf(str2);
    if (index_>=0){
        return true;
    }else{
        return false;
    }
}