// 블랙잭
const readline = require("readline");

let input = [];
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  input.push(line);

  if (input.length === 2) {
    const N = input[0].split(" ").map((x) => Number(x));
    const M = input[1].split(" ").map((x) => Number(x));
    let answer = [];
    for (let i = 0; i < M.length; i++) {
      for (let j = i + 1; j < M.length; j++) {
        for (let k = j + 1; k < M.length; k++) {
          if (M[i] + M[j] + M[k] === N[1]) {
            console.log(M[i] + M[j] + M[k]);
            rl.close();
          } else if (M[i] + M[j] + M[k] < N[1]) {
            answer.push(M[i] + M[j] + M[k]);
          }
        }
      }
    }
    console.log(Math.max(...answer));
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
