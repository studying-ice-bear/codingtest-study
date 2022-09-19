function solution(n) {
  return n
    .toString()
    .split("")
    .map((item) => +item)
    .reduce((a, b) => a + b);
}
