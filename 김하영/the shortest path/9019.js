const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

input.shift();
const answer = [];
const solution = (start, end) => {
  const visited = Array.from({ length: 10000 }, () => false);
  visited[start] = true;
  const queue = [[start, ""]];

  while (queue.length) {
    let [cur, path] = queue.shift();
    if (cur === end) {
      answer.push(path);
      return;
    }

    const nextD = (cur * 2) % 10000;
    if (!visited[nextD]) {
      visited[nextD] = true;
      queue.push([nextD, path + "D"]);
    }

    const nextS = cur === 0 ? 9999 : cur - 1;
    if (!visited[nextS]) {
      visited[nextS] = true;
      queue.push([nextS, path + "S"]);
    }

    const nextL = (cur % 1000) * 10 + Math.floor(cur / 1000);
    if (!visited[nextL]) {
      visited[nextL] = true;
      queue.push([nextL, path + "L"]);
    }

    const nextR = (cur % 10) * 1000 + Math.floor(cur / 10);
    if (!visited[nextR]) {
      visited[nextR] = true;
      queue.push([nextR, path + "R"]);
    }
  }
};

input.map((test) => {
  const [start, end] = test.split(" ").map(Number);
  solution(start, end);
});

console.log(answer.join("\n"));
