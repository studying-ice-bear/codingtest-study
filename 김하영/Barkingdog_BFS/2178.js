const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [col, row] = input
  .shift()
  .split(" ")
  .map((n) => +n);

const map = input.map((n) => n.split("").map((n) => +n));
const visited = Array.from(Array(col), () => Array(row).fill(-1));
const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];
let count = 1;

const bfs = (x, y) => {
  const queue = [];

  queue.push([x, y]);
  visited[x][y] = count;
  while (queue.length !== 0) {
    const [x, y] = queue.shift();
    count++;
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx >= 0 && nx < col && ny >= 0 && ny < row) {
        if (map[nx][ny] === 1 && visited[nx][ny] === -1) {
          queue.push([nx, ny]);
          visited[nx][ny] = visited[x][y] + 1;
        }
      }
    }
  }
};

const solution = () => {
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (map[i][j] === 1 && visited[i][j] === -1) {
        bfs(i, j);
      }
    }
  }
};

solution();

console.log(visited[col - 1][row - 1]);
