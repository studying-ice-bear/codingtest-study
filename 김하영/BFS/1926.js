const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [col, row] = input
  .shift()
  .split(" ")
  .map((n) => +n);
const map = input.map((n) => n.split(" ").map((n) => +n));
const visited = Array.from(Array(col), () => Array(row).fill(false));
const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];
let paintingCount = 0;
let paintingSize = [];

const bfs = (x, y) => {
  let queue = [];

  queue.push([x, y]);
  let size = 1;
  visited[x][y] = true;
  while (queue.length !== 0) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx >= 0 && nx < col && ny >= 0 && ny < row) {
        if (map[nx][ny] === 1 && !visited[nx][ny]) {
          queue.push([nx, ny]);
          visited[nx][ny] = true;
          size++;
        }
      }
    }
  }
  paintingSize.push(size);
};

const solution = () => {
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (map[i][j] === 1 && !visited[i][j]) {
        bfs(i, j);
        paintingCount++;
      }
    }
  }
  paintingSize.sort((a, b) => b - a);
  if (paintingCount === 0) {
    paintingSize = [0];
  }

  return `${paintingCount}\n${paintingSize[0]}`;
};

console.log(solution());
