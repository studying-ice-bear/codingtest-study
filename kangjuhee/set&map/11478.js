// 서로 다른 부분 문자열의 개수

let input = require("fs").readFileSync("../input.txt").toString().trim();

let result = new Set();

// 완전탐색
for (let i = 0; i < input.length; i++) {
  for (let j = i + 1; j < input.length + 1; j++) {
    result.add(input.substring(i, j));
  }
}

console.log(result.size);
