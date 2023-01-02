const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M, R] = input
  .shift()
  .split(" ")
  .map((v) => +v);

const edges = input.map((v) => v.split(" ").map((v) => +v));

const graph = new Map();
edges.forEach(([from, to]) => {
  if (graph.has(from)) {
    graph.get(from).push(to);
  } else {
    graph.set(from, [to]);
  }
  if (graph.has(to)) {
    graph.get(to).push(from);
  } else {
    graph.set(to, [from]);
  }
});
console.log(graph);

let count = 1;

const visited = new Array(N + 1).fill(false);
const answer = new Array(N).fill(0);

const dfs = (node) => {
  visited[node] = true;
  answer[node - 1] = count++;
  if (!graph.has(node)) {
    return;
  }
  const nodes = [...graph.get(node)].sort((a, b) => a - b);
  for (x of nodes) {
    if (!visited[x]) {
      dfs(x);
    }
  }
};

dfs(R);

console.log(answer.join(" "));
