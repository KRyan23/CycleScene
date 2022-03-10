// Retrieves the star rating from the product page in 0.5 steps then renders out the correct number of stars.
// If the rating happens to be outside the range it will display 5 empty stars + the contents of 'norating'.
var ratingslist = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
var startlist = ["<i class='fas fa-star starcolor star-color-effect'></i>", "<i class='fas fa-star-half-alt starcolor star-color-effect'></i>", "<i class='fas fa-star empty-star'></i>"];
var norating = ["<p>Not Yet Rated</p>"]

function getProductRating() {
    var star = Number(document.getElementById("readStarRating").innerText);
    var tensandunits = [...String(star)].map(Number);

    if (ratingslist.includes(star)) {
        if (tensandunits[2] > 0) {
        var emptystars = 4 - tensandunits[0];
        } else {
        var emptystars = 5 - tensandunits[0];
        }
        for (var i = 0; i < tensandunits[0]; i++) {
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[0]}`);
        }
        if (tensandunits[2] > 0) {
            document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[1]}`);
        }
        for (var j = 0; j < emptystars; j++) {
            document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[2]}`);
        }
    }else{noRatingMessage
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${startlist[2]}`.repeat(5));
        document.getElementById("ratingMessage").style.cssText = "display:none;";
        document.getElementById('displayStarRating').insertAdjacentHTML('beforeend', `${norating[0]}`);
    }

}

getProductRating();