// 통계학
// 계속 시간초과 나온 이유 => 계속 사용되는 함수를 변수에 담아서 사용하는 것이 좋다.

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

input = input.map((i) => +i);
const N = input.shift();

let average = Math.round(input.reduce((a, b) => a + b) / N);
// -0으로 나오는 것 방지
average = average === -0 ? 0 : average;

input = input.sort((a, b) => a - b);
const median = input[Math.floor(N / 2)];
const range = input[N - 1] - input[0];

// const mode = input.reduce((a, b) => ((a[b] = (a[b] || 0) + 1), a));
const mode = (arr) => {
  const counts = {};
  arr.forEach((el) => {
    counts[el] = (counts[el] || 0) + 1; // null, undefined, 비어있는 값이면 0 + 1
  });
  return counts;
};
const modeArr = mode(input);
let hitMaxNum = Math.max.apply(null, Object.values(modeArr));
let hitMaxResult = 0;
const hitMaxArr = Object.keys(modeArr).filter(
  (el) => modeArr[el] === hitMaxNum
);

if (hitMaxArr.length === 1) hitMaxResult = +hitMaxArr[0];
else hitMaxResult = hitMaxArr.sort((a, b) => a - b)[1];

console.log(`${average}\n${median}\n${hitMaxResult}\n${range}`);
