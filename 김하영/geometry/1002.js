const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "김하영/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(input.shift());

const xyrarr = input.map((item) => item.split(" ").map(Number));

const solution = (T, xyrarr) => {
  const result = [];
  for (let i = 0; i < T; i++) {
    const [x1, y1, r1, x2, y2, r2] = xyrarr[i];
    const d = Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2); // 루트를 쓰지 않고 r1, r2를 제곱하여 넣어줘야 성공한다.
    if (x1 === x2 && y1 === y2) {
      // 두 원이 같은 위치에 있을 때
      if (r1 === r2) {
        result.push(-1);
      } else {
        result.push(0);
      }
    } else if ((r1 + r2) ** 2 < d || (r1 - r2) ** 2 > d) {
      // 두 원이 서로 겹치지 않을 때
      result.push(0);
    } else if ((r1 + r2) ** 2 === d || (r1 - r2) ** 2 === d) {
      // 두 원이 한 점에서 만날 경우
      result.push(1);
    } else if ((r1 + r2) ** 2 > d && (r1 - r2) ** 2 < d) {
      // 두 원이 교차할 경우
      result.push(2);
    }
  }
  return result.join("\n");
};

console.log(solution(T, xyrarr));
