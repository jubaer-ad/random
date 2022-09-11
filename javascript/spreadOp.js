const arr001 = ['a', 'b', 'c'];
let arr002;
(() => {
    arr002 = [...arr001];
    arr001[0] = "A";
})();
console.log(arr002);