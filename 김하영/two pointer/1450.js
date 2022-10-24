const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, S] = input[0].split(" ").map(Number);

// const B = input[1].split(" ").map((v) => +v);
// const A = [];

// for (let i = 0; i < Math.ceil(N / 2); i++) {
//   A.push(B.shift())
// }

// function subsetSum(arr) {
//   let result = [];
//   let len = arr.length;
//   // << 연산자는 2진수로 표현했을 때 왼쪽으로 비트를 이동시키는 연산자입니다.
//   // 1 << 3 은 2진수로 1000이 되고, 8이 됩니다.
//   // 1 << 4 는 2진수로 10000이 되고, 16이 됩니다.
//   for (let i = 0; i < (1 << len); i++) {
//     let sum = 0;
//     for (let j = 0; j < len; j++) {
//       if (i & (1 << j)) {
//         sum += arr[j]
//       }
//     }
//     result.push(sum)
//   }
//   return result
// }

// const sumA = subsetSum(A).sort((a, b) => a - b)
// const sumB = subsetSum(B)

// let answer = 0;
// for (let i = 0; i < sumB.length; i++) {
//   if (sumB[i] > S) continue;
//   let min = 0;
//   let max = sumA.length;
//   while (min < max) {
//     let mid = Math.floor((min + max) / 2);
//     if (sumA[mid] + sumB[i] <= S) {
//       min = mid + 1;
//     } else {
//       max = mid;
//     }
//   }

//   answer += max;
// }

// console.log(answer);
