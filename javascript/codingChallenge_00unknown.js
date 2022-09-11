var myObj = [
    {
        "fName": "JuBaer",
        "email": "jubaer@gmail.com",
        "phone": "001",
        "todo": [
            "A",
            "B",
            "C"
        ]
    },
    {
        "fName": "jb",
        "email": "jb@gmail.com",
        "phone": "002",
        "todo": [
            "D",
            "E",
            "F"
        ]
    },
    {
        "fName": "AD",
        "email": "ad@gmail.com",
        "phone": "003",
        "todo": [
            "G",
            "H",
            "I"
        ]
    }
]

function runner(fname, prop) {
    var fNameF = false, propF = false;
    var fNameIndex = 0, propIndex = 0;
    for (var i = 0; i < myObj.length; i++) {
        if (myObj[i]["fName"] === fname) {
            fNameF = true;
            fNameIndex = i;
        }
        if (myObj[i].hasOwnProperty(prop)) {
            propF = true;
        }
    }
    if (fNameF === true && propF === true) {
        return myObj[fNameIndex][prop];
    } else if (fNameF === false && propF === false) {
        return "Both name and property not found!";
    } else if (fNameF === false) {
        return "Name not found!";
    } else {
        return "Property not found!";
    }
}

function rummer(fName, prop) {
    for (let i = 0; i < myObj.length; i++) {
        if (myObj[i]["fName"] === fName) {
            return myObj[i][prop] || "Property not found!";
        }
    }
    return "Name not found!";
}
console.log(rummer("jb", "todo"));
console.log((5 < 1) || 45);