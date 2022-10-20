const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const babbling = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(babbling) {
  let answer = 0;
  const possiblePronunciation = ["aya", "ye", "woo", "ma"];

  function compare(str) {
    console.log(str);
    if (str.length === 0) {
      return true;
    }
    for (let j = 0; j < possiblePronunciation.length; j++) {
      if (str === possiblePronunciation[j]) {
        return true;
      }
      const isInclude = str.includes(possiblePronunciation[j]);
      if (!isInclude) {
        continue;
      } else {
        str.replace(possiblePronunciation[j], "");
        compare(str);
      }
    }
  }

  for (let i = 0; i < babbling.length; i++) {
    const str = babbling[i];
    const isInclude = compare(str);

    if (isInclude) {
      answer++;
    }
  }

  return answer;
}

console.log(solution(babbling));
