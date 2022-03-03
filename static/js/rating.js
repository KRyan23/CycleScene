// Retrieves the star rating from the product page in 0.5 steps then renders out the correct number of stars.

var ratingslist = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
var startlist = ["<i class='fas fa-star starcolor star-color-effect'></i>", "<i class='fas fa-star-half-alt starcolor star-color-effect'></i>", "<i class='fas fa-star empty-star'></i>"];

function getProductRating(){
    var star = Number(document.getElementById("readStarRating").innerText);
    var tensandunits = [...String(star)].map(Number);
    if (tensandunits[2] > 0){
        var emptystars = 4 - tensandunits[0];
    }else{
        var emptystars = 5 - tensandunits[0];
    }
    for (var i=0; i<tensandunits[0]; i++){
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[0]}`);}
    if (tensandunits[2] > 0){ 
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[1]}`);}
    for (var j=0; j<emptystars; j++){
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[2]}`);}
}

getProductRating();