const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [row, col] = input
  .shift()
  .split(" ")
  .map((n) => +n);
const map = input.map((n) => n.split(" ").map((n) => +n));

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null; // 제일 앞 노드
    this.rear = null; // 제일 뒤 노드
    this.length = 0; // 노드의 길이
  }

  enqueue(data) {
    // 노드 추가.
    const node = new Node(data); // data를 가진 node를 만들어준다.
    if (!this.head) {
      // 헤드가 없을 경우 head를 해당 노드로
      this.head = node;
    } else {
      this.rear.next = node; // 아닐 경우 마지막의 다음 노드로
    }
    this.rear = node; // 마지막을 해당 노드로 한다.
    this.length++;
  }

  dequeue() {
    // 노드 삭제.
    if (!this.head) {
      // 헤드가 없으면 한 개도 없는 것이므로 false를 반환.
      return false;
    }
    const data = this.head.data; // head를 head의 다음 것으로 바꿔주고 뺀 data를 return
    this.head = this.head.next;
    this.length--;

    return data;
  }
}

// 인덱스 검증
function isRange(dx, dy) {
  if (dx >= 0 && dy >= 0 && dx < col && dy < row) {
    return true;
  }
  return false;
}

function BFS(graph, queue) {
  // 상하좌우
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  let day = 0;

  while (queue.length) {
    let [col, row, cnt] = queue.dequeue();
    for (let k = 0; k < 4; k++) {
      let mx = col + dx[k];
      let my = row + dy[k];
      if (isRange(mx, my) && graph[mx][my] === 0) {
        graph[mx][my] = 1;
        queue.enqueue([mx, my, cnt + 1]);
      }
    }
    day = cnt;
  }
  let answer = day;

  // BFS 수행 후 0이 있을 경우 토마토가 익지 못하는 상황 발생
  graph.forEach((_, i) => {
    if (graph[i].includes(0)) {
      answer = -1;
    }
  });

  return answer;
}

function solution() {
  let answer = 0;
  const queue = new Queue();
  map.forEach((_, col) => {
    map[col].forEach((_, row) => {
      if (map[col][row] === 1) {
        queue.enqueue([col, row, 0]);
      }
    });
  });

  // BFS 함수 수행하고 나면 인접 토마토가 모두 익게 된다.
  answer = BFS(map, queue);

  return answer;
}

console.log(solution());
