const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(+input[0]);
const hasCards = new Set(input[1].split(" ").map(Number));
const M = Number(+input[2]);
const compareCards = input[3].split(" ").map(Number);

let answer = "";
for (let i = 0; i < M; i++) {
  if (hasCards.has(compareCards[i])) answer += 1 + " ";
  else answer += 0 + " ";
}

console.log(answer);
