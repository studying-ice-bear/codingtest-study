// 피보나치 수 5
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const fibonacci = (n) => {
  if (n < 2) {
    return n;
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
};

rl.on("line", function (line) {
  // 입력 처리
  const answer = fibonacci(Number(line));
  console.log(answer);

  rl.close();
}).on("close", function () {
  process.exit();
});
