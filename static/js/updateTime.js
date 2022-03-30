/* Function to update the time regulary on the checkout form */
/* This post helped me https://www.w3schools.com/jsref/met_win_setinterval.asp */

function getTime() {
    let now = new Date(); 
    let hours = now.getHours(); 
    let minutes = now.getMinutes(); 
    let seconds = now.getSeconds();
    let padding = '0';   
    
    if (seconds < 10){
        seconds = padding + seconds;
    }else if (minutes < 10){ 
        minutes = padding + minutes;
    }else if (hours < 10){
        hours = padding + hours;
    }
    document.getElementById("current-time").innerHTML=hours+":"+minutes+":"+seconds;
    timeInterval=setTimeout('getTime()',1000);
}

getTime();
