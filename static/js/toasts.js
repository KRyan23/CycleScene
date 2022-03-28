//Function was tested from a button action and toast will popup so issue must be with
// the messaging structure in python or the template.
 $(document).ready(function(){
    console.log('function called');
    $(".toast").click(function() {
        $('.toast').toast('show');
        console.log('toast should be visible at the top of page');
});
});