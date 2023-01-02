//백준 1753 최단 경로

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [V, E] = input
  .shift()
  .split(" ")
  .map((item) => +item);
const K = +input.shift();

const graph = Array.from(Array(V + 1), () => Array(V + 1).fill(Infinity));

class MinHeap {
  constructor() {
    this.nodes = [];
  }

  insert(value) {
    this.nodes.push(value);
    this.bubbleUp();
  }

  bubbleUp(index = this.nodes.length - 1) {
    if (index < 1) return;

    const currentNode = this.nodes[index];
    const parentIndex = Math.floor((index - 1) / 2);
    const parentNode = this.nodes[parentIndex];
    if (parentNode.cost <= currentNode.cost) return;

    this.nodes[index] = parentNode;
    this.nodes[parentIndex] = currentNode;
    index = parentIndex;
    this.bubbleUp(index);
  }

  extract() {
    const min = this.nodes[0];
    if (this.nodes.length === 1) {
      this.nodes.pop();
      return min;
    }
    this.nodes[0] = this.nodes.pop();
    this.trickleDown();
    return min;
  }

  trickleDown(index = 0) {
    const leftChildIndex = 2 * index + 1;
    const rightChildIndex = 2 * index + 2;
    const length = this.nodes.length;
    let minimum = index;

    if (!this.nodes[rightChildIndex] && !this.nodes[leftChildIndex]) return;
    if (!this.nodes[rightChildIndex]) {
      if (this.nodes[leftChildIndex].cost < this.nodes[minimum].cost) {
        minimum = leftChildIndex;
      }
      return;
    }

    if (this.nodes[leftChildIndex].cost > this.nodes[rightChildIndex].cost) {
      if (
        rightChildIndex <= length &&
        this.nodes[rightChildIndex].cost < this.nodes[minimum].cost
      ) {
        minimum = rightChildIndex;
      }
    } else {
      if (
        leftChildIndex <= length &&
        this.nodes[leftChildIndex].cost < this.nodes[minimum].cost
      ) {
        minimum = leftChildIndex;
      }
    }

    if (minimum !== index) {
      let t = this.nodes[minimum];
      this.nodes[minimum] = this.nodes[index];
      this.nodes[index] = t;
      this.trickleDown(minimum);
    }
  }
}

const dijkstra = (graph, start) => {
  const distance = Array(V + 1).fill(Infinity);
  distance[start] = 0;
  const pq = new MinHeap();
  pq.insert({ vertex: start, cost: 0 });

  while (pq.nodes.length) {
    const { vertex, cost } = pq.extract();

    if (distance[vertex] < cost) continue;

    for (let i = 1; i <= V; i++) {
      if (graph[vertex][i] === Infinity) continue;

      const dist = cost + graph[vertex][i];

      if (dist < distance[i]) {
        distance[i] = dist;
        pq.insert({ vertex: i, cost: dist });
      }
    }
  }
  return distance;
};

for (let i = 0; i < E; i++) {
  const [u, v, w] = input[i].split(" ").map((item) => +item);
  graph[u][v] = Math.min(graph[u][v], w);
}

const result = dijkstra(graph, K);

for (let i = 1; i <= V; i++) {
  if (result[i] === Infinity) {
    console.log("INF");
  } else {
    console.log(result[i]);
  }
}
