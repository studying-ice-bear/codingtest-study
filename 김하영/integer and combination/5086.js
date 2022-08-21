const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "김하영/input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map((x) => +x));

input.pop();

const solution = (arr) => {
  // factor mutiple neither
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i][0] < arr[i][1] && arr[i][1] % arr[i][0] === 0) {
      result.push("factor");
    } else if (arr[i][0] > arr[i][1] && arr[i][0] % arr[i][1] === 0) {
      result.push("mutiple");
    } else {
      result.push("neither");
    }
  }

  return result.join("\n");
};

console.log(solution(input));
