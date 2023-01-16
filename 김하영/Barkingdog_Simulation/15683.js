const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [row, col] = input
  .shift()
  .split(" ")
  .map((n) => +n);
const map = input.map((n) => n.split(" ").map((n) => +n));
const temp = Array.from(Array(row), () => Array(col).fill(0));
const cctvs = [];

const printFive = (y, x) => {
  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  for (const [dy, dx] of directions) {
    let [y1, x1] = [y + dy, x + dx];

    while (y1 >= 0 && y1 < row && x1 >= 0 && x1 < col && map[y1][x1] !== 6) {
      temp[y1][x1] = 1;
      y1 += dy;
      x1 += dx;
    }
  }
};

const checkFive = () => {
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (map[i][j] < 6 && map[i][j] > 0) {
        temp[i][j] = 1;
        if (map[i][j] === 5) {
          printFive(i, j);
        } else {
          cctvs.push([i, j, map[i][j]]);
        }
      }
    }
  }
};

const solution = () => {
  checkFive();
  const directions = [
    [],
    [[0], [1], [2], [3]],
    [
      [0, 2],
      [1, 3],
    ],
    [
      [0, 1],
      [1, 2],
      [2, 3],
      [3, 0],
    ],
    [
      [0, 1, 2],
      [1, 2, 3],
      [2, 3, 0],
      [3, 0, 1],
    ],
    [[0, 1, 2, 3]],
  ];
};
