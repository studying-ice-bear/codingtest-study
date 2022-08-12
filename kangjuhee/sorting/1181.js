// 단어 정렬

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input.map((i) => i.trimEnd());
input = [...new Set(input)]; // 중복 제거
input = input.sort((a, b) => a.localeCompare(b)); // 문자열과 문자열을 비교하여 오름차순으로 정렬한다.
input = input.sort((a, b) => a.length - b.length); // 단어 길이로 정렬
let result = "";
input.forEach((el) => {
  result += `${el}\n`;
});
console.log(result.trimEnd());
