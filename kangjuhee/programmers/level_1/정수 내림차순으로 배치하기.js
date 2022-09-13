function solution(n) {
  let array = n
    .toString()
    .split("")
    .map((num) => +num);
  array = array.sort((a, b) => b - a);
  return Number(array.join(""));
}
