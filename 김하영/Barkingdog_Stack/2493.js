// const fs = require("fs");
// const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

// const N = input.shift();
// const inputArr = input[0].split(" ").map(Number);

// const solution = (inputArr) => {
//   const stack = [];
//   const result = [];
//   for (let i = 0; i < inputArr.length; i++) {
//     const num = inputArr[i];
//     stack.push(num);
//     let index = stack.length - 1;
//     while (true) {
//       const compareNum = stack[index];
//       if (compareNum > num) {
//         result.push(index + 1);
//         break;
//       }
//       if (index === 0) {
//         result.push(0);
//         break;
//       }
//       index--;
//     }
//   }

//   return result.join(" ");
// };

console.log(solution(inputArr));

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N;

rl.on("line", function (line) {
  if (!N) {
    N = +line;
  } else {
    let tops = line.split(" ").map((n) => +n);
    let answer = [];
    let stack = [];

    for (let i = 0; i < N; i++) {
      let now = tops[i];

      // 현재 탑을 기준으로
      // 가장 근접한 탑인 스택(stack[stack.length - 1])과 비교하여
      // 현재 탑보다 높이가 낮다면 스택에서 제거해줍니다.
      while (stack.length && tops[stack[stack.length - 1]] < now) { 
        stack.pop();
      }

      if (stack.length === 0) {
        answer.push(0);
      } else {
        answer.push(stack[stack.length - 1] + 1);
      }
      stack.push(i);
    }

    console.log(answer.join(" "));
    rl.close();
  }
});

[6, 9, 5, 7, 4]

[6]
[1]
[0]

[6, 9]
[2]
[0, 0]

[6, 9, 5]
[2, 3]
[0, 0, 2]

[6, 9, 5, 7]
[2, 4]
[0, 0, 2, 2]

[6, 9, 5, 7, 4]
[2, 4, 5]
[0, 0, 2, 2, 4]
