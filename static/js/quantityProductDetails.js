// Script to increment and decrement the quantity value in the products details 
// 'add to bag' input box hard min and max set to 1 and 10 repectively + max and min messages


function increment(){
    var bagvalue = $('.form-quantity').val();
    bagvalue = Number(bagvalue);
    if (bagvalue === 10){
        bagvalue = 10
        document.getElementById('quantity-message').innerHTML="Hi items are limited to 10 / Order";
    }else{
        bagvalue = bagvalue + 1;
        document.getElementById('quantity-message').innerHTML="";
    }
    document.getElementsByClassName('form-quantity')[0].value = bagvalue;
   
}

function decrement(){
    var bagvalue = $('.form-quantity').val();
    bagvalue = Number(bagvalue);
    if (bagvalue === 1) {
        bagvalue = 1;
        document.getElementById('quantity-message').innerHTML="Hi the minimum order is 1!";
    }else{
        bagvalue = bagvalue - 1;
        document.getElementById('quantity-message').innerHTML="";
    }
    document.getElementsByClassName('form-quantity')[0].value = bagvalue;
}