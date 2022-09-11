var myObj = [
    {
        "name": "A",
        "dob": 1995
    },
    {
        "name": "B",
        "dob": 1996
    },
    {
        "name": "C",
        "dob": 1997
    }
]

i = 0;
console.log(typeof(i))
var uName = "A";
while(i < myObj.length) {
    if (myObj[i].name === uName) {
        console.log(myObj[i].dob)
    }
    i++;

}