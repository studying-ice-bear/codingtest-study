const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "김하영/input.txt";

const [N, M] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let output = [];
let result = "";
let visited = new Array(N);

const solution = (idx, cnt) => {
  if (cnt === M) {
    result += `${output.join(" ")}\n`;
    return;
  }

  for (let i = idx; i < N; i++) {
    if (visited[i] === true) continue;
    visited[i] = true;
    output.push(i + 1);
    solution(i, cnt + 1);
    output.pop();
    visited[i] = false;
  }
};

solution(0, 0);

console.log(result.trim());
