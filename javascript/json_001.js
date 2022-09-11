var myObj = {
    "id000": {
        "fName": "fn000",
        "lName": "lname001",
        "dob": 1995,
        "hobby": "coding"
    },
    "id001": {
        "fName": "fn001",
        "lName": "lname001",
        "dob": 1996,
        "hobby": "roaming"
    },
    "id002": {
        "fName": "fn002",
        "lName": "lname002",
        "dob": 1997,
    },
    "id003": {
        "fName": "fn003",
        "lName": "lname003",
        "todo": [
            "mobile",
            "dual_curr_card"
        ]
    }
}

var myObjCopy = JSON.parse(JSON.stringify(myObj));
console.log(myObjCopy);
function update(id, prop, value) {
    if (myObj[id].hasOwnProperty(prop)) {
        if (value === "") {
            delete myObj[id][prop]
        } else if (myObj[id][prop].constructor === Array) {
            myObj[id][prop].push(value);
        }
    } else {
        if (prop.toLowerCase().startsWith("list") || prop.toLowerCase().endsWith("list")) {
            myObj[id][prop] = myObj[id][prop] || [];
            myObj[id][prop].push(value);
        }
        myObj[id][prop] = value;
    }
    return JSON.parse(JSON.stringify(myObj));
}

console.log(update("id003", "tobo", "curiosityStream"));
console.log(update("id003", "todo", "curiosityStream"));
console.log(update("id003", "Listtobo", "a"));
// console.log(update("id003", "Listtobo", "b"));








