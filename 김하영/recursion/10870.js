// const fs = require("fs");

// const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

const solution = (num) => {
  if (num < 2) {
    return num;
  }

  return solution(num - 1) + solution(num - 2);
};

/* 
    꼬리재귀 방법으로 푸는법
const fibonacci = (num, lastlast=0, last=1) => {
    if (num === 0) {
        return lastlast;
    }
    if (num === 1) {
        return last;
    }
    return fibonacci(num - 1, last, lastlast + last);
}
    0 0 1
    1 0 1
    2 1 1
    3 1 2
    4 2 3
    5 3 5
    6 5 8
    7 8 13
    8 13 21
*/

console.log(solution(input));
