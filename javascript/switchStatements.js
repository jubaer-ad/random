function switchFunc(val) {
    switch(val) {
        case 1:
            return 'alpha';
            break;
        case '2':
            return 'beta';
            break;
        case 3:
            return 'gamma';
            break;
        default:
            return 'returning default';
    }

}

console.log(switchFunc('1'));
