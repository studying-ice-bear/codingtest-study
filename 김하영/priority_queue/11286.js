//백준 11286번 절댓값 힙

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const [length, ...nums] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

class absolute_heap {
  constructor() {
    this.heap = [];
  }

  empty() {
    return this.heap.length === 0;
  }

  insert(x) {
    this.heap.push(x);
    let idx = this.heap.length - 1;
    //bubble up
    while (idx > 0) {
      let parent = Math.floor((idx - 1) / 2);
      if (Math.abs(this.heap[parent]) > Math.abs(this.heap[idx])) {
        [this.heap[parent], this.heap[idx]] = [
          this.heap[idx],
          this.heap[parent],
        ];
        idx = parent;
      } else if (Math.abs(this.heap[parent]) === Math.abs(this.heap[idx])) {
        if (this.heap[parent] > this.heap[idx]) {
          [this.heap[parent], this.heap[idx]] = [
            this.heap[idx],
            this.heap[parent],
          ];
          idx = parent;
        } else {
          break;
        }
      } else {
        break;
      }
    }
  }

  pop() {
    if (this.empty() === true) {
      return 0;
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    let result = this.heap[0];
    this.heap[0] = this.heap.pop();

    let idx = 0;

    //bubble down
    while (idx < this.heap.length) {
      let left = idx * 2 + 1;
      let right = idx * 2 + 2;
      let min = idx;

      if (
        left < this.heap.length &&
        Math.abs(this.heap[left]) < Math.abs(this.heap[min])
      ) {
        min = left;
      } else if (
        left < this.heap.length &&
        Math.abs(this.heap[left]) === Math.abs(this.heap[min])
      ) {
        if (this.heap[left] < this.heap[min]) {
          min = left;
        }
      }
      if (
        right < this.heap.length &&
        Math.abs(this.heap[right]) < Math.abs(this.heap[min])
      ) {
        min = right;
      } else if (
        right < this.heap.length &&
        Math.abs(this.heap[right]) === Math.abs(this.heap[min])
      ) {
        if (this.heap[right] < this.heap[min]) {
          min = right;
        }
      }
      if (min !== idx) {
        [this.heap[min], this.heap[idx]] = [this.heap[idx], this.heap[min]];
        idx = min;
      } else {
        break;
      }
    }

    return result;
  }
}

const solution = (length, nums) => {
  let answer = "";
  let heap = new absolute_heap();
  for (let i = 0; i < length; i++) {
    if (nums[i] === 0) {
      answer += heap.pop() + "\n";
    } else {
      heap.insert(nums[i]);
    }
  }
  return answer;
};

console.log(solution(length, nums));
