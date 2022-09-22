function solution(n) {
  let q = parseInt(n / 2);
  if (n % 2 === 0) return "수박".repeat(q);
  else return "수박".repeat(q) + "수";
}
