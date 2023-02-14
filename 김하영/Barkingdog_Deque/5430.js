const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const T = Number(input.shift());
let answer = "";

console.log(input);

for (let i = 0; i < T; i++) {
  const instruction = input[3 * i];
  let start = 0,
    end = Number(input[3 * i + 1]);
  let arr = input[3 * i + 2].split(/\D/g).filter((v) => v !== "");
  let IsReverse = false;
  if (instruction.includes("D") && instruction.match(/[D]/g).length > end) {
    answer += "error\n";
    continue;
  }
  instruction.split("").forEach((item) => {
    if (item === "R") IsReverse = !IsReverse;
    else {
      if (IsReverse) end--;
      else start++;
    }
  });
  if (start >= end) {
    answer += "[]\n";
    continue;
  }
  if (IsReverse) {
    answer += "[";
    for (let j = end - 1; j > start; j--) answer += `${arr[j]},`;
    answer += `${arr[start]}]\n`;
  } else {
    answer += "[";
    for (let j = start; j < end - 1; j++) answer += `${arr[j]},`;
    answer += `${arr[end - 1]}]\n`;
  }
}
console.log(answer.trim());
