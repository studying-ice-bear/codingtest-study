const fs = require("fs");

let input = fs.readFileSync("brute-force/input.txt").toString().split("\n");
const NumN = input[0].split(" ")[0];
const NumM = Number(input[0].split(" ")[1]);
const arr = input[1].split(" ").map(Number);

// const solution = (M, arr) => {
//   let sumArr = [];
//   for (let i = 0; i < arr.length - 2; i++) {
//     for (let j = i + 1; j < arr.length - 1; j++) {
//       for (let k = j + 1; k < arr.length; k++) {
//         const sum = arr[i] + arr[j] + arr[k];
//         if (sum <= M) {
//           sumArr.push(sum);
//         }
//       }
//     }
//   }

//   sumArr.sort((a, b) => a - b);

//   return sumArr[sumArr.length - 1];
// };

// console.log(solution(NumM, arr));

// 합 배열을 만들지 않고 푸는법

const solution2 = (M, arr) => {
  let max = 0;
  for (let i = 0; i < arr.length - 2; i++) {
    for (let j = i + 1; j < arr.length - 1; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        const sum = arr[i] + arr[j] + arr[k];
        if (sum > max && sum <= M) {
          max = sum;
        }
      }
    }
  }
  return max;
};

console.log(solution2(NumM, arr));
