const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const rectangle = JSON.parse(input.shift());
const [characterX, characterY, itemX, itemY] = input.map(Number);

function solution(rectangle, characterX, characterY, itemX, itemY) {
  const max = rectangle.reduce((acc, cur) => Math.max(acc, ...cur), 0);
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  const visited = Array.from({ length: max }, () => Array(max).fill(0));
  const map = Array.from({ length: max }, () => Array(max).fill(0));
  for (let i = 0; i < rectangle.length; i++) {
    const [x1, y1, x2, y2] = rectangle[i];
    for (let j = x1; j < x2; j++) {
      for (let k = y1; k < y2; k++) {
        map[j][k] = 1;
      }
    }
  }
  const [...nums] = rectangle.flat();
  map.map((array, row) => {
    array.map((num, col) => {
      if (num === 1) {
        if (
          nums.includes(row + 1) &&
          nums.includes(col + 1) &&
          nums.includes(row - 1) &&
          nums.includes(col - 1)
        ) {
          map[row][col] = 0;
        }
      }
    });
  });
  console.log(map);

  const queue = [[characterX, characterY]];
  visited[characterX][characterY] = 1;

  while (queue.length) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx >= 0 && nx < max && ny >= 0 && ny < max) {
        if (map[nx][ny] === 1 && visited[nx][ny] === 0) {
          visited[nx][ny] = visited[x][y] + 1;
          queue.push([nx, ny]);
        }
      }
    }
  }

  return visited[itemX][itemY] - 1;
}

console.log(solution(rectangle, characterX, characterY, itemX, itemY));
