// old way
let myObj001 = {
    "fName": "jb",
    changeName: function(newName) {
        this.fName = newName;
    }
};
console.log(myObj001.fName);
myObj001.changeName("ad");
console.log(myObj001.fName);

// new way
let myObj002 = {
    "fName": "jubaer",
    changeName(newName) {
        this.fName = newName;
    }
};
console.log(myObj002.fName);
myObj002.changeName("JUBAER");
console.log(myObj002.fName);
