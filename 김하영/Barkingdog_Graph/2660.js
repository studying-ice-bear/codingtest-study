const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = Number(input.shift());
const members = input.map((value) => {
  return value.split(" ").map(Number);
});
/* const members = input.map(([node1, , node2]) => {
   return [Number(node1), Number(node2)]
 }) 
처음에 이렇게 나눈 뒤 NaN으로 끝난걸 체크 했으나 계속 오답처리 됐었던 원인 이였음..
*/

const floyd = (graph) => {
  /* 플로이드 와샬 알고리즘
  각 노드에 접근했을 때, 최단 거리
  이 경우에는 친구의 친구의 친구의 ... 의 최단거리를 구하는 것
  graph[i][j] = min(i에서 j까지 걸리는 노드의 최단 거리, i에서 k까지의 노드거리 + k에서 j까지의 노드거리)
  */
  // 거쳐가는 노드
  for (let k = 1; k < N + 1; k++) {
    // 시작 노드
    for (let i = 1; i < N + 1; i++) {
      // 끝나는 노드
      for (let j = 1; j < N + 1; j++) {
        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
      }
    }
  }
  return graph;
};

const solution = (members) => {
  /*
  [
  [ 0, Infinity, Infinity, Infinity, Infinity, Infinity ],
  [ Infinity, 0, Infinity, Infinity, Infinity, Infinity ],
  [ Infinity, Infinity, 0, Infinity, Infinity, Infinity ],
  [ Infinity, Infinity, Infinity, 0, Infinity, Infinity ],
  [ Infinity, Infinity, Infinity, Infinity, 0, Infinity ],
  [ Infinity, Infinity, Infinity, Infinity, Infinity, 0 ]
  ]
  각 노드는 0, 노드 연결은 Infinity로 설정한 빈배열
  */
  const graph = Array.from({ length: N + 1 }, () =>
    new Array(N + 1).fill(Infinity)
  ).map((v1, i1) => {
    return v1.map((v2, i2) => (i1 === i2 ? 0 : v2));
  });

  /*
  [
  [ 0, Infinity, Infinity, Infinity, Infinity, Infinity ],
  [ Infinity, 0, 1, Infinity, Infinity, Infinity ],
  [ Infinity, 1, 0, 1, 1, Infinity ],
  [ Infinity, Infinity, 1, 0, 1, 1 ],
  [ Infinity, Infinity, 1, 1, 0, 1 ],
  [ Infinity, Infinity, Infinity, 1, 1, 0 ]
  ]
  각 노드 연결선 그리기
  */
  members.forEach(([node1, node2]) => {
    if (node1 === -1 && node2 === -1) return null;
    graph[node1][node2] = 1;
    graph[node2][node1] = 1;
  });

  let leaderScore = Infinity;

  // floyd 적용
  const newGraph = floyd(graph);
  newGraph.shift();

  const result = newGraph
    // leaderScore 및 Infinity 거르는 부분
    .reduce((acc, cur) => {
      let score = 0;
      cur.forEach((v) =>
        v !== Infinity ? (score = Math.max(score, v)) : null
      );
      acc.push(score);
      leaderScore = Math.min(leaderScore, score);
      return acc;
    }, [])
    // leaderScore에 따라서 값으로 만들어주는 부분
    .reduce((acc, cur, idx) => {
      if (cur <= leaderScore) {
        acc.push(idx + 1);
        return acc;
      }
      return acc;
    }, []);

  return `${leaderScore} ${result.length}\n${result.join(" ")}`;
};

console.log(solution(members));

// TODO 그래프의 반절은 쓸모 없음
