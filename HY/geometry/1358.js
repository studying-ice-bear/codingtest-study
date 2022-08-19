const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [w, h, x, y, p] = input.shift().split(" ").map(Number);

const xyarr = input.map((item) => item.split(" ").map(Number));

const solution = (w, h, x, y, p, xyarr) => {
  let count = 0;
  // (x - a)2 + (y - b)2 = r2
  const circle = (x, y, a, b) => {
    return (x - a) ** 2 + (y - b) ** 2;
  };
  for (let i = 0; i < p; i++) {
    const [a, b] = xyarr[i];
    // 직사각형 안에 있을 때
    if (a >= x && a <= x + w && b >= y && b <= y + h) {
      count++;
    } else if (
      // 왼쪽 반원 안에 있을 때
      circle(x, y + h / 2, a, b) <=
      (h / 2) ** 2
    ) {
      count++;
    } else if (
      // 오른쪽 반원 안에 있을 때
      circle(x + w, y + h / 2, a, b) <=
      (h / 2) ** 2
    ) {
      count++;
    }
  }
  return count;
};
console.log(solution(w, h, x, y, p, xyarr));
