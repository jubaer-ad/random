function randomNum(from = 0, upto = 10) {
    if (from >= upto)
        return "Error in input!";
    return (Math.random() * (upto - from)) + from;
}
myList = [];
var i = 0;
// while(i < 100) {
//     myList.push(randomNum(1));
//     i++;
// }
console.log(myList);
console.log(randomNum(101.5, 103));