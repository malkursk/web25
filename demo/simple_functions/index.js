// step 1
function myPow(n, p) {
    r = 1
    while (--p >= 0) {
        r *= n
    }
    return r
}

a=-1.25
p=14 
console.log(`step 1: ${a}^${p} = ${myPow(a,p)}`)

// step 2

let counter;

function getCounter(v) {
    counter = v;
    return function() {
     return ++counter;
    }          
}

function reset() {
    counter = 0
    return counter;
} 


let count = getCounter(8);
count.reset = reset 
console.log(`step 2: counter`)
console.log(count());
console.log(count());
count.reset()
console.log(count());
console.log(count());


