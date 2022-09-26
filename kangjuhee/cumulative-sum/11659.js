// 구간 합 구하기 4
// 메모리 초과

// let input = require("fs")
//   .readFileSync("../input.txt")
//   .toString()
//   .trim()
//   .split("\n");

// input.shift();
// let arr = input
//   .shift()
//   .split(" ")
//   .map((i) => +i);

// input = input.map((i) => i.split(" ").map((j) => +j));

// let answer = [];
// for (let i = 0; i < input.length; i++) {
//   const newArr = arr.slice(input[i][0] - 1, input[i][1]);
//   const sum = newArr.reduce((acc, num) => (acc += parseInt(num)), 0);
//   answer.push(sum);
// }
// console.log(answer.join("\n"));

// ============================================================================================
// 정답

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

input.shift();
let arr = input
  .shift()
  .split(" ")
  .map((i) => +i);

let cumsum = new Array(arr.length + 1).fill(0);
arr.forEach((v, i) => {
  cumsum[i + 1] = cumsum[i] + v;
});

input = input.map((i) => i.split(" ").map((j) => +j));

let answer = [];
for (let i = 0; i < input.length; i++) {
  answer.push(cumsum[input[i][1]] - cumsum[input[i][0] - 1]);
}
console.log(answer.join("\n"));
