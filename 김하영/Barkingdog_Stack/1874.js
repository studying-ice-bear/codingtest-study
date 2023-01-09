const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input.shift();
const inputArr = input.map((str) => Number(str.trim()));

class Stack {
  constructor() {
    this.arr = [];
    this.result = [];
  }

  push(num) {
    this.result.push("+");
    this.arr.push(num);
  }

  pop() {
    this.result.push("-");
    return this.arr.pop();
  }

  size() {
    return this.arr.reduce((acc, cur) => acc + cur, 0);
  }
}

const solution = (inputArr) => {
  const stack = new Stack();
  let num = 1;

  for (let i = 0; i < inputArr.length; i++) {
    const target = inputArr[i];

    while (num <= target) {
      stack.push(num);
      num++;
    }

    if (stack.arr[stack.arr.length - 1] === target) {
      stack.pop();
    } else {
      return "NO";
    }
  }

  return stack.result.join("\n");
};

console.log(solution(inputArr));
