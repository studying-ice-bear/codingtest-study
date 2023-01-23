const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = JSON.parse(fs.readFileSync(filePath));

function solution(maps) {
  const visited = Array.from(Array(maps.length), () =>
    Array(maps[0].length).fill(0)
  );

  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  let x = 0;
  let y = 0;
  const queue = [[x, y]];
  visited[x][y] = 1;
  while (queue.length) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length) {
        if (maps[nx][ny] === 1 && visited[nx][ny] === 0) {
          visited[nx][ny] = visited[x][y] + 1;
          queue.push([nx, ny]);
        }
      }
    }
  }

  return visited[maps.length - 1][maps[0].length - 1] || -1;
}

console.log(solution(input));
