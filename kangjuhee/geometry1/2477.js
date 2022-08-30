// 참외밭 틀린 이유 찾을 것!!

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

const num = +input.shift();

const arr = input.map((i) => i.split(" ").map((j) => +j));
const numArr = arr.map((i) => i[1]);

// 직사각형 최대 높이/너비 구하기
const height = Math.max(
  ...arr.filter((i) => i[0] === 3 || i[0] === 4).map((i) => i[1])
);
const width = Math.max(
  ...arr.filter((i) => i[0] === 1 || i[0] === 2).map((i) => i[1])
);

const indexWidth = numArr.indexOf(width);
const indexHeight = numArr.indexOf(height);

const result = () => {
  if (indexWidth === 5 && indexHeight === 0) {
    return [...numArr.slice(indexWidth), ...numArr.slice(0, indexWidth)];
  } else if (indexWidth === 0 && indexHeight === 5) {
    return [...numArr.slice(indexHeight), ...numArr.slice(0, indexHeight)];
  } else if (indexWidth < indexHeight) {
    return [...numArr.slice(indexWidth), ...numArr.slice(0, indexWidth)];
  } else if (indexWidth > indexHeight) {
    return [...numArr.slice(indexHeight), ...numArr.slice(0, indexHeight)];
  }
  return [...numArr];
};

console.log((width * height - result()[3] * result()[4]) * num);
