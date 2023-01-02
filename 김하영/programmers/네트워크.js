const input = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];

function solution(n, computers) {
  let answer = 0;
  const graph = new Map();
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) {
        continue;
      }
      if (computers[i][j] === 1) {
        graph.set(i, [...(graph.get(i) || []), j]);
      }
    }
  }
  let visited = new Array(n).fill(false);

  const dfs = (node) => {
    visited[node] = true;
    if (!graph.has(node)) {
      return;
    }
    const nodes = [...graph.get(node)];
    for (x of nodes) {
      if (!visited[x]) {
        dfs(x);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      dfs(i);
      answer++;
    }
  }

  return answer;
}

console.log(solution(3, input));
