// 숫자 카드
// 참고 : https://velog.io/@sozero/TIL-220307-Set.has-%EC%99%80-Array.includes-%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84
// arr.includes() 보다 Set.has() 메서드를 사용하는 것이 더 빠름

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

const cardSet = new Set(input[1].split(" ").map((i) => +i));
const cardArr = input[3].split(" ").map((i) => +i);
let result = [];
for (let i = 0; i < cardArr.length; i++) {
  if (cardSet.has(cardArr[i])) result.push(1);
  else result.push(0);
}
console.log(result.join(" "));
