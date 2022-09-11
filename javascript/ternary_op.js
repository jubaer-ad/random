function runner001(val1, val2) {
    return val1 > val2 ? val1 + " is greater than " + val2 : val1 + " is less than " + val2;
}

// console.log(runner001(50, 6));


function runner002(val) {
    return val > 0 ? "positive": val < 0 ? "negative" : "zero";
}

// console.log(runner002(0));

function grader(mark) {
    return mark >= 50 ? mark >= 60 ? mark >= 70 ? mark >= 80 ? mark > 100 ? "Unreal Mark!" : "A+" : "A" : "B" : "C"  : "Fail";
}
// console.log(grader(101));

let a = 0;
console.log(a);
if (true) {
    a = "5";
    console.log(a);
}
console.log(a);

