const myVar001 = (() => {
    return function sum(...args) {
        return args.reduce((a, b) => a + b, 0);
    };
})();
// console.log(myVar001(1,2,3,4));

const sumZ = (...args) => {
        return args.reduce((a, b) => a + b, 0);
};
console.log(sumZ(1,2,3,4));