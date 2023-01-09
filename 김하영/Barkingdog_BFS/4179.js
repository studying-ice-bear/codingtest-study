const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, M] = input
  .shift()
  .split(" ")
  .map((n) => +n);

const graph = input.map((n) => n.split(""));
const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
let answer = Infinity;
let visited = Array.from(Array(N), () => Array(M).fill(false));

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
  if (dx >= 0 && dy >= 0 && dx < M && dy < N) {
    return true;
  }
  return false;
}

function findJH() {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] == "J") {
        return [i, j];
      }
    }
  }
}

function findFire() {
  const fire = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] == "F") {
        fire.push([i, j]);
      }
    }
  }
  return fire;
}

function isExit(i, j) {
  if (i == 0 || i == N - 1 || j == 0 || j == M - 1) {
    return true;
  }
  return false;
}

const [jx, jy] = findJH();
graph[jx][jy] = ".";
let fire = findFire();
let f = new Queue();
let j = new Queue();

let jh = [[jx, jy, 1]];
visited[jx][jy] = true;

let flag = true;
while (jh.length > 0 && flag) {
  while (jh.length > 0) {
    const [jx, jy, cnt] = jh.shift();
    if (graph[jx][jy] == "F") continue;
    if (isExit(jx, jy)) {
      answer = cnt;
      flag = false;
    } else {
      j.enqueue([jx, jy, cnt]);
    }
  }
  if (!flag) break;

  while (fire.length > 0) {
    f.enqueue(fire.shift());
  }
  while (f.length > 0) {
    const [fx, fy] = f.dequeue();
    for (let i = 0; i < 4; i++) {
      const nfx = fx + dx[i];
      const nfy = fy + dy[i];
      if (
        nfx >= 0 &&
        nfy >= 0 &&
        nfx < N &&
        nfy < M &&
        graph[nfx][nfy] == "."
      ) {
        graph[nfx][nfy] = "F";
        fire.push([nfx, nfy]);
      }
    }
  }

  while (j.length > 0) {
    const [jx, jy, cnt] = j.dequeue();
    for (let i = 0; i < 4; i++) {
      const njx = jx + dx[i];
      const njy = jy + dy[i];
      if (
        njx >= 0 &&
        njy >= 0 &&
        njx < N &&
        njy < M &&
        !visited[njx][njy] &&
        graph[njx][njy] == "."
      ) {
        jh.push([njx, njy, cnt + 1]);
        visited[njx][njy] = true;
      }
    }
  }
}

if (answer == Infinity) console.log("IMPOSSIBLE");
else console.log(answer);

// 다시 풀어보기
