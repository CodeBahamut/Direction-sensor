// Change the Grey up arrow to a white one then change it back after a second by using a refresh with a delay
function upArrow() {
    document.getElementById("up-img").src = "../static/images/White-Arrow-Up.png";
    setTimeout(() => {  document.location.reload(true); }, 1000);
}

// Change the Grey right arrow to a white one then change it back after a second by using a refresh with a delay
function rightArrow() {
    document.getElementById("right-img").src = "../static/images/White-Arrow-Right.png";
    setTimeout(() => {  document.location.reload(true); }, 1000);
}

// Change the Grey down arrow to a white one then change it back after a second by using a refresh with a delay
function downArrow() {
    document.getElementById("down-img").src = "../static/images/White-Arrow-Down.png";
    setTimeout(() => {  document.location.reload(true); }, 1000);
}

// Change the Grey left arrow to a white one then change it back after a second by using a refresh with a delay
function leftArrow() {
    document.getElementById("left-img").src = "../static/images/White-Arrow-Left.png";
    setTimeout(() => {  document.location.reload(true); }, 1000);
}

// This switch case choose between the previous methods depending on the value given to it.
function changeArrow(direction) {

    switch (direction){

        case "Up":
            upArrow();
            break;
        case "Right":
            rightArrow();
            break;
        case "Down":
            downArrow();
            break;
        case "Left":
            leftArrow();
            break;
        default:
            break;
    }
}


    
