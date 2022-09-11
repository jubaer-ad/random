let myVar = {
    "fName": "jb",
    "places": [
        "A", "B", "C"
    ]
}
function makeList(arr) {
    const resultDisplayArr = [];
    let i = 0;
    while (i < arr.length) {
        resultDisplayArr.push(`<li class="text-warning">${arr[i]}</li>`);
        i++;
    }
    return resultDisplayArr;
}

console.log(makeList(myVar.places));
