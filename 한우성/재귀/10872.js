let fs = require('fs')

const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim();

function ans(num) {
    let result = 1
    for(let i = 1; i <= num; i++) {
        result = result * i
    }
    return result
}  

console.log(ans(input))