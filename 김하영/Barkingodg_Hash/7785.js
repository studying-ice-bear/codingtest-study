const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input.shift());
const inputArr = input.map((str) => str.trim());

const solution = (inputArr) => {
  const hash = {};
  for (let i = 0; i < inputArr.length; i++) {
    const [name, status] = inputArr[i].split(" ");

    if (status === "enter") {
      hash[name]++;
    } else {
      delete hash[name];
    }
  }
  const result = [];

  for (const key of Object.keys(hash).sort((a, b) => b.localeCompare(a))) {
    result.push(key);
  }

  return result.join("\n");
};

console.log(solution(inputArr));
