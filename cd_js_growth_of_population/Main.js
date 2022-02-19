function nbYear(p0, percent, aug, p) {
    let counter = 0;
    while (p0 <= p){
        counter++;
        p0 += Math.round(p0 * percent/100 + aug);
    }
    return (counter == 50)? counter + 1: counter;
}

console.log(nbYear(1500, 5, 100, 5000));