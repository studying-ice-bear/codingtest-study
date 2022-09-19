function solution(n) {
  let numList = n
    .toString()
    .split("")
    .map((num) => +num);
  let answer = [];
  while (numList.length > 0) {
    answer.push(numList.pop());
  }
  return answer;
}
