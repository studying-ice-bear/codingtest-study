// 분해합

const fs = require("fs");
const input = parseInt(fs.readFileSync("../input.txt").toString().trim());
const arr = [];

const d = (n) => {
  const N = n.toString().split(""); // 256 => ["2","5","6"]
  return n + N.reduce((acc, num) => (acc += parseInt(num)), 0);
};

for (let i = 1; i <= input; i++) {
  if (d(i) === input) {
    arr.push(i);
  }
}

if (arr.length) console.log(Math.min(...arr));
else console.log(0);
