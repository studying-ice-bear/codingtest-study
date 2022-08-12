// 하노이 탑 이동 순서

const fs = require("fs");

const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
const result = [];

const hanoi = (n, from, via, to) => {
  if (n === 1) {
    result.push(`${from} ${to}`);
    return;
  }
  hanoi(n - 1, from, to, via);
  result.push(`${from} ${to}`);
  hanoi(n - 1, via, from, to);
};

hanoi(input, 1, 2, 3);
console.log(result.length);
console.log(result.join("\n"));
