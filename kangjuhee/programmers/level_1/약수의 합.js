function solution(n) {
  if (n <= 1) return n;
  else {
    let answer = n + 1;
    for (let i = 2; i < parseInt(n ** 0.5) + 1; i++) {
      if (n % i === 0) {
        answer += i === n / i ? i : i + n / i;
      }
    }
    return answer;
  }
}
