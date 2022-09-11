var myObj = {
    "name" : "Jubaer",
    "job" : "tryingH",
    "the goal" : "remote",
    l4 : 55,
    55 : 110
}
var prop1 = "name";
var prop2 = 55;

console.log(myObj) ;
myObj["drawback"] = "spiral";
myObj.fun = "coding";
console.log(myObj) ;
delete myObj["the goal"];
// if (myObj.nom == undefined) {
//     console.log("!exists");
// }
var testProp = "nom";
if (myObj.hasOwnProperty(testProp)) {
    console.log(testProp + " exists");
} else {
    console.log(testProp + " !exists");
}