const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : "recursion/input.txt";

let input = Number(fs.readFileSync("recursion/input.txt").toString());

let count = 0;
const result = [];

const solution = (num, from, other, to) => {
  if (num === 0) {
    return;
  } else {
    solution(num - 1, from, to, other);
    result.push([from, to]);
    count++;
    solution(num - 1, other, from, to);
  }
};
solution(input, 1, 2, 3);
console.log(count);
console.log(result.map((item) => item.join(" ")).join("\n"));
