// 수 정렬하기 2 => 수 정렬하기랑 문제 같음

// const fs = require("fs");
// const input = fs.readFileSync("../input.txt").toString().trim().split("\n");

// input.shift(); // 맨 앞에 있는 숫자를 제거한다.

// input.sort((a, b) => a - b); // 오름차순으로 정렬한다.

// console.log(input.join("\n")); // 정렬된 수들을 출력한다.

// ---------------------------------------------------------------------------------------------------------------------

// 시간 단축 코드
const fs = require("fs");
let input = fs.readFileSync("../input.txt").toString().trim().split("\n");
let result = "";
input.shift();
input = input.sort((a, b) => a - b);
input.forEach((el) => {
  result += `${el}\n`;
});

console.log(result.trimEnd());
