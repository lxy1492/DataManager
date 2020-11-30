

function setCustomerInfo(name) {
    userid = localStorage.getItem("id");
    $.ajax({
        url:"/server/getUserInfoByName/",
        data:{data: name,userid:userid},
        dataType:"json",
        success:function (data) {
            if (data["result"]=="success"){
                $("#customerName").text(data["name"]);
                $("#contact").text(data["phone"]);
                info = data["production"]+'<br><a rel=\"nofollow\" href=\"#\">编辑此客户</a><br>'+'购买时间：'+data["buyTime"]+'<br>'+data["marked"]+' <br><br>\n' +
                '\t\t\t\t\t\t\t\t\t\t\tChange icons by <a rel=\"nofollow\" href=\"#/font-awesome-icon-world-map/\">Font Awesome</a> (version 4). Example: <span class=\"blue\">&lt;i class=&quot;fa fa-refresh&quot;&gt;&lt;/i&gt;</span>';
                console.log(info);
                document.getElementById("customerInfo").innerHTML = info;

            }else{
                alert("无法获取此用户资料！");
            }
        }
    });
}

function addCustomer(data) {
    var r={"result":"无法连接到服务器"};
    $.ajax({
        url:"/server/addCustomer/",
        data:data,
        dataType: "json",
        async:false,
        success:function (data) {
            r = data;
        }
    });
    return r
}

function getModels() {
    var r = [];
    $.ajax({
        url:"/server/getModels/",
        data:{data:""},
        dataType:"json",
        async: false,
        success:function (data) {
            if (data["result"]=="success"){
                r  =data["models"];
            }
        }
    });
    // alert(r);
    return r
}