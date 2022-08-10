// 수 정렬하기

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

input.shift(); // 맨 앞에 있는 숫자를 제거한다.

input.sort((a, b) => a - b); // 오름차순으로 정렬한다.

console.log(input.join("\n")); // 정렬된 수들을 출력한다.
