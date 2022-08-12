// 좌표압축: 해당 좌표값보다 작은 좌표값들의 개수로 좌표값을 대체한다는 의미

// 시간초과 => indexOf() 메서드 사용하지말고, object로 처리하여 시간 복잡도 o(1)

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

input.shift();
input = input[0].split(" ").map((i) => +i);

let setArr = [...new Set(input)];
setArr = setArr.sort((a, b) => a - b);

const object = {};

setArr.forEach((el, index) => {
  object[el] = index;
});

input = input.map((i) => {
  return object[i];
});

console.log(input.join(" "));
