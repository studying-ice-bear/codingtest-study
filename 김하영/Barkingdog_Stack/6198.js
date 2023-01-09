const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input.shift();
const inputArr = input.map((str) => Number(str.trim()));

const solution = (inputArr) => {
  let result = 0;
  const stack = [];

  for (let i = 0; i < inputArr.length; i++) {
    while (stack.length && stack[stack.length - 1] <= inputArr[i]) {
      stack.pop();
    }
    stack.push(inputArr[i]);
    console.log(stack.length - 1);
    result += stack.length - 1;
  }

  return result;
};

console.log(solution(inputArr));
