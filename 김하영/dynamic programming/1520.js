// 백준 1520번 내리막 길

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [M, N] = input[0].split(" ").map((v) => +v);
const map = input.slice(1).map((v) => v.split(" ").map((v) => +v));

const dp = Array.from(Array(M), () => Array(N).fill(-1));

const solution = (M, N, map, dp) => {
  let answer = 0;
  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  const dfs = (x, y) => {
    if (x === M - 1 && y === N - 1) {
      return 1;
    }

    if (dp[x][y] === -1) {
      // 방문하지 않은 경우
      dp[x][y] = 0;
      // 4방향 탐색
      for (let i = 0; i < 4; i++) {
        // 다음 좌표
        const nx = x + dx[i];
        const ny = y + dy[i];
        // 다음 좌표가 범위 내에 있고, 다음 좌표가 현재 좌표보다 작은 경우
        if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
          // 다음 좌표가 현재 좌표보다 작은 경우
          if (map[nx][ny] < map[x][y]) {
            dp[x][y] += dfs(nx, ny);
          }
        }
        console.log(dp);
      }
    }
    return dp[x][y];
  };

  answer = dfs(0, 0);
  return answer;
};

console.log(solution(M, N, map, dp));
