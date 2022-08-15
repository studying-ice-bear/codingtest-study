// 직각삼각형
// 정렬 필수!

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((i) =>
    i
      .split(" ")
      .map((j) => (+j) ** 2)
      .sort((a, b) => a - b)
  );

console.log(input);
for (let i = 0; i < input.length - 1; i++) {
  let [a, b, c] = input[i];
  if (a + b === c) {
    console.log("right");
  } else {
    console.log("wrong");
  }
}
