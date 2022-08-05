const readline = require("readline");

const factorial = (n) => {
  if (n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  // 입력 처리
  const answer = factorial(Number(line));
  console.log(answer);

  rl.close();
}).on("close", function () {
  process.exit();
});
