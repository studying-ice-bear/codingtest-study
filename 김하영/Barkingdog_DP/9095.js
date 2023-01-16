const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v);
const numArray = input.slice(1);
const dp = Array.from({ length: 1000001 }, () => 0);
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;

const representaionAsSum = (num) => {
  for (let i = 4; i <= num; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]; // 1, 2, 3을 더하는 경우의 수
  }

  return dp[num];
};

const solution = (numArray) => {
  const result = numArray.map(representaionAsSum);

  console.log(result.join("\n"));
};

solution(numArray);

/* 3의 경우
1 + 1 + 1 3
1 + 2 3
2 + 1 3
3 3
*/

/* 4의 경우
1 + 1 + 1 + 1 
1 + 1 + 2 
1 + 2 + 1 
2 + 1 + 1 
2 + 2 
1 + 3 
3 + 1 
*/

/* 5의 경우
1 1 1 1 1 
1 1 1 2 1
1 1 2 1 1
1 2 1 1 1
2 1 1 1 1
1 2 2 
2 1 2 
2 2 1 
1 1 3 
1 3 1 
3 1 1 
2 3 
3 2 

*/

/* 6의 경우
1 1 1 1 1 1
1 1 1 1 2
1 1 1 2 1
1 1 2 1 1
1 2 1 1 1
2 1 1 1 1
1 1 1 3
1 1 3 1
1 3 1 1
3 1 1 1
1 1 2 2
1 2 1 2
1 2 2 1
2 1 1 2
2 1 2 1
2 2 1 1
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
*/
