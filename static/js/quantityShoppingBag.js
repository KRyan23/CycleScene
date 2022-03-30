// Script to increment and decrement the quantity value in the products details 
// 'add to bag' input box hard min and max set to 1 and 10 repectively + max and min messages

$(document).ready(function(){
    $(".increment-value").click(function() {
        var dataId = $(this).attr("id");
        var thenum = dataId.replace( /^\D+/g, '');
        var inputFieldValue = document.getElementById('id_qty_'+thenum).value;
        inputFieldValue = Number(inputFieldValue);        
        if (inputFieldValue === 10){
            inputFieldValue = 10
            document.getElementById('error_id_'+thenum).innerHTML="Hi items are limited to 10 / Order";
        }else{
            inputFieldValue++;
            document.getElementById('error_id_'+thenum).innerHTML="";
        }
        document.getElementById('id_qty_'+thenum).value = inputFieldValue;
    });
});

$(document).ready(function(){
    $(".decrement-value").click(function() {
        var dataId = $(this).attr("id");
        var thenum = dataId.replace( /^\D+/g, '');
        var inputFieldValue = document.getElementById('id_qty_'+thenum).value;
        inputFieldValue = Number(inputFieldValue);        
        if (inputFieldValue === 1 ){
            inputFieldValue = 1
            document.getElementById('error_id_'+thenum).innerHTML="Hi the minimum order is 1!";
        }else{
            inputFieldValue--;
            document.getElementById('error_id_'+thenum).innerHTML="";
        }
        document.getElementById('id_qty_'+thenum).value = inputFieldValue;
    });
});