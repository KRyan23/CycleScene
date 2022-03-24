/* Change the quantity on each shopping bag item*/

$('.change-product-quantity').click(function (e) {
    var readFormQuantity = $(this).prev('.shopping-bag-form');
    readFormQuantity.submit();
})
