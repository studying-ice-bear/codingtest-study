// 프로그래머스 조이스틱
const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim();

const solution = (name) => {
  let answer = 0;
  let count = 0;
  let index = 0;
  let nameArr = name.split("");
  let nameArrLen = nameArr.length;
  let nameArrCheck = Array.from({ length: nameArrLen }, () => false);
  while (count < nameArrLen) {
    let right = 1;
    let left = 1;
    if (nameArr[index] !== "A") {
      if (nameArr[index].charCodeAt() - 65 > 13) {
        answer += 26 - (nameArr[index].charCodeAt() - 65);
      } else {
        answer += nameArr[index].charCodeAt() - 65;
      }
      nameArr[index] = "A";
      nameArrCheck[index] = true;
      count++;
    }
    if (count === nameArrLen) {
      break;
    }
    while (nameArrCheck[index + right]) {
      right++;
    }
    while (nameArrCheck[index - left]) {
      left++;
    }
    if (right > left) {
      answer += left;
      index -= left;
    } else {
      answer += right;
      index += right;
    }
  }
  return answer;
};

console.log(solution(input));
