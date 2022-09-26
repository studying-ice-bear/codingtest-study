function solution(x) {
  let eachSum = x
    .toString()
    .split("")
    .map((num) => +num)
    .reduce((a, b) => a + b);
  if (x % eachSum === 0) return true;
  else return false;
}
