const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
let total = input.shift().split(" ").map(Number)[1];

const solution = () => {
  const coins = input.map(Number).sort((a, b) => b - a);

  let result = 0;

  for (let i = 0; i < coins.length; i++) {
    const coin = coins[i];
    result += Math.floor(total / coin);
    total %= coin;
  }

  return result;
};

console.log(solution());
