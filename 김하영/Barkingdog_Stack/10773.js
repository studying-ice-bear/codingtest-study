const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input.shift();
const inputArr = input.map((str) => Number(str.trim()));

class Stack {
  constructor() {
    this.arr = [];
  }

  push(num) {
    this.arr.push(num);
  }

  pop() {
    return this.arr.pop();
  }

  size() {
    return this.arr.reduce((acc, cur) => acc + cur, 0);
  }
}

const solution = (inputArr) => {
  const result = [];
  const stack = new Stack();

  for (let i = 0; i < inputArr.length; i++) {
    const num = inputArr[i];

    if (num === 0) {
      stack.pop();
    } else {
      stack.push(num);
    }
  }

  return stack.size();
};

console.log(solution(inputArr));
