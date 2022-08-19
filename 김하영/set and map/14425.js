const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const strings = [];
const compareStrings = [];

for (let i = 0; i < N; i++) {
  strings.push(input.shift());
}
for (let i = 0; i < M; i++) {
  compareStrings.push(input.shift());
}
const set = new Set(strings);
let answer = 0;
for (let i = 0; i < M; i++) {
  if (set.has(compareStrings[i])) answer++;
}

console.log(answer);
