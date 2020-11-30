function getCustomerList() {
    var l=[];
    $.ajax({
        url:"/server/getAllCustomer/",
        data:{type:"all"},
        dataType:"json",
        async:false,
        success:function (data) {
            if(data["result"]=="success"){
                l = data["data"];
            }
        }
    });
    return l
}