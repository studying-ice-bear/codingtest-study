//백준 11404 플로이드

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input.shift();
const M = +input.shift();

const graph = Array.from(Array(N), () => Array(N).fill(Infinity));

for (let i = 0; i < N; i++) {
  graph[i][i] = 0;
}

for (let i = 0; i < M; i++) {
  const [a, b, c] = input[i].split(" ").map((item) => +item);

  graph[a - 1][b - 1] = c;
}

const floyd = (graph) => {
  // 플로이드 와샬 알고리즘
  // k를 경유했을 때의 가중치
  // ex) k = 1, i = 4, j = 2일 때, 1을 경유해서 4에서 2로 가는 가중치
  // graph[4][2] = min(graph[4][2], graph[4][1] + graph[1][2])
  for (let k = 0; k < N; k++) {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
      }
    }
  }
  return graph;
};

const result = floyd(graph);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (result[i][j] === Infinity) {
      result[i][j] = 0;
    }
  }
}

for (let i = 0; i < N; i++) {
  console.log(result[i].join(" "));
}
