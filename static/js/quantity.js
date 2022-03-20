/* Script to increment and decrement the quantity value in the products details 
'add to bag' input box hard min and max set to 1 and 10 repectively */


function increment(){
    var bagvalue = $('.form-quantity').val();
    bagvalue = Number(bagvalue);
    if (bagvalue === 10){
        bagvalue = 10
    }else{
        bagvalue = bagvalue + 1;
    }
    document.getElementsByClassName('form-quantity')[0].value = bagvalue;
   
}

function decrement(){
    var bagvalue = $('.form-quantity').val();
    bagvalue = Number(bagvalue);
    if (bagvalue === 1) {
        bagvalue = 1;
    }else{
        bagvalue = bagvalue - 1;
    }
    document.getElementsByClassName('form-quantity')[0].value = bagvalue;
}