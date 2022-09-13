function solution(n) {
  let value = n - 1;
  let answer = 0;
  for (let i = 2; i <= n - 1; i++) {
    if (value % i === 0) {
      answer = i;
      break;
    }
  }

  return answer;
}
