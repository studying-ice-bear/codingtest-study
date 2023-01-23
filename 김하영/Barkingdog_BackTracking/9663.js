const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = Number(fs.readFileSync(filePath).toString().trim());

const solution = (input) => {
  const visited = Array.from({ length: input }, () => 0);
  let result = 0;
  const check = (x) => {
    for (let i = 0; i < x; i++) {
      if (visited[x] === visited[i]) return false; // 같은 열에 있는지
      if (Math.abs(visited[x] - visited[i]) === x - i) return false; // 대각선에 있는지
    }
    return true;
  };
  const dfs = (x) => {
    if (x === input) {
      result++;
      return;
    } else {
      for (let i = 0; i < input; i++) {
        visited[x] = i;
        if (check(x)) dfs(x + 1);
        visited[x] = 0;
      }
    }
  };

  dfs(0);

  return result;
};

console.log(solution(input));
