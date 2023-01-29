const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input.shift());
const inputArr = input[0].split(" ").map((str) => Number(str.trim()));

const solution = (inputArr) => {
  // let first = 0;
  // let last = 0;
  // let count = 0;

  // while (first < inputArr.length) {
  //   const newArr = inputArr.slice(first, last + 1);
  //   if (
  //     newArr.some((value) => value === inputArr[last + 1]) ||
  //     last === inputArr.length - 1
  //   ) {
  //     first++;
  //     last = first;
  //     count++;
  //   } else {
  //     last++;
  //     count++;
  //   }
  // }

  // return count;

  let first = 0;
  let last = 0;
  let count = 0;
  let set = new Set();

  while (first < inputArr.length) {
    console.log(set);
    if (!set.has(inputArr[first]) && last < inputArr.length) {
      set.add(inputArr[first]);
      first++;
      count += set.size;
    } else {
      set.delete(inputArr[last]);
      last++;
    }
  }

  return count;
};

console.log(solution(inputArr));
