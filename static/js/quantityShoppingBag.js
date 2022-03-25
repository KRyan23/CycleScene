/* Change the quantity on each shopping bag item*/

$('.change-product-quantity').click(function (e) {
    var readFormQuantity = $(this).prev('.shopping-bag-form');
    readFormQuantity.submit();
})


$('.remove-item').click(function(e) {
    console.log("1");
    var csrfToken = "{{ csrf_token }}";
    console.log("2");
    var itemId = $(this).attr('id');
    console.log(itemId);
    
    console.log("3");
    var url = `/shoppingbag/remove/${itemId}/`;
    console.log("4");
    var data = {'csrfmiddlewaretoken': csrfToken };
    console.log("5");
    $.post(url, data)
     .done(function() {
         location.reload();
     });
})

