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

/* prev refactor
const [N, K] = input.shift().split(" ").map(Number);

const solution = () => {
  const coins = input.map(Number).sort((a, b) => b - a);
  let index = 0;
  let result = 0;
  let remain = K;

  while (index !== N) {
    const selectCoin = coins[index];
    let value = remain - selectCoin;
    if (value < 0) {
      index++;
      continue;
    } else if (value > 0) {
      let selectCoinEA = 4;
      while (remain - selectCoin * selectCoinEA < 0) {
        selectCoinEA--;
      }
      result += selectCoinEA;
      remain -= selectCoin * selectCoinEA;
      if (remain === 0) {
        break;
      }
    } else {
      result++;
      break
    }
  }

  return result;
};
*/
