const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const [length, ...nums] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

class max_priority_heap {
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
      if (this.heap[parent] < this.heap[idx]) {
        [this.heap[parent], this.heap[idx]] = [
          this.heap[idx],
          this.heap[parent],
        ];
        idx = parent;
      } else {
        break;
      }
    }
  }

  pop() {
    if (this.heap.length === 0) return 0;
    if (this.heap.length === 1) return this.heap.pop();

    let result = this.heap[0];
    this.heap[0] = this.heap.pop();
    let idx = 0;
    //bubble down
    while (idx < this.heap.length) {
      let left = idx * 2 + 1;
      let right = idx * 2 + 2;
      let max = idx;
      if (left < this.heap.length && this.heap[left] > this.heap[max]) {
        max = left;
      }
      if (right < this.heap.length && this.heap[right] > this.heap[max]) {
        max = right;
      }
      if (max !== idx) {
        [this.heap[max], this.heap[idx]] = [this.heap[idx], this.heap[max]];
        idx = max;
      } else {
        break;
      }
    }

    return result;
  }
}

const solution = (length, nums) => {
  let result = "";
  let heap = new max_priority_heap();
  for (let i = 0; i < length; i++) {
    if (nums[i] === 0) {
      result += heap.pop() + "\n";
    } else {
      heap.insert(nums[i]);
    }
  }
  return result;
};

console.log(solution(length, nums));
