const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

console.log(input);

function solution(msg) {
  let result = [];
  let dic = {};
  let index = 27;
  const keys = Object.keys(dic);

  for (let i = 0; i < 26; i++) {
    dic[String.fromCharCode(65 + i)] = i + 1;
  }

  for (let i = 0; i < msg.length; i++) {
    let w = msg[i];
    let c = msg[i + 1];

    while (dic[w + c] !== undefined) {
      w += c;
      i++;
      c = msg[i + 1];
    }

    result.push(dic[w]);
    dic[w + c] = index++;
  }

  return result;
}

console.log(solution(input[0]));
