var myVar001 = function(val1, val2) { // this function is magic function
    return val1 + val2;
}
// they both are same
var myVar002 = (val1, val2) =>  val1 + val2;
console.log(myVar002(5,6));

var myVar003 = (val1, val2) => {
    let a = "Sum is: ";
    return a + (val1 + val2);
   }

console.log(myVar003(5, 9));