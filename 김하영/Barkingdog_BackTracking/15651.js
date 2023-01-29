const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const [N, M] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const solution = () => {
  const result = [];
  const dfs = (depth, str) => {
    if (depth === M) {
      result.push(str);
    } else {
      for (let i = 1; i <= N; i++) {
        dfs(depth + 1, str + i + " ");
      }
    }
  };

  dfs(0, "");

  console.log(result.join("\n"));
};

solution(N, M);
