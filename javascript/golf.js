function golfScore(stroks, par) {
    var result;
    if (stroks == 1) {
        return "Hole-in-one!";
    } else if (stroks <= par - 2) {
        return "Eagle";
    } else if (stroks == par - 1) {
        return "Birdie!";
    } else if (stroks == par - 1) {
        return "Par";
    } else if (stroks == par + 1) {
        return "Bogey";
    } else if (stroks == par + 2) {
        return "Double Bogey";
    } else
    return "Go Home!";
}

console.log(golfScore(99, 4))