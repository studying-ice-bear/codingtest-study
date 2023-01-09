const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, K] = input
  .shift()
  .split(" ")
  .map((n) => +n);

const visited = Array(100001).fill(false);
const dx = [-1, 1, 2];
let answer = 0;

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

const solution = (N, K) => {
  const queue = new Queue();
  queue.enqueue([N, 0]);
  visited[N] = true;

  while (queue.length) {
    const [x, cnt] = queue.dequeue();
    if (x === K) {
      answer = cnt;
      break;
    }

    for (let i = 0; i < 3; i++) {
      let nx = x + dx[i]; // 걸을 때
      if (i === 2) {
        nx = x * dx[i]; // 순간이동 할 때
      }
      if (nx >= 0 && nx <= 100000 && !visited[nx]) {
        visited[nx] = true;
        queue.enqueue([nx, cnt + 1]);
      }
    }
  }
};

solution(N, K);
console.log(answer);
