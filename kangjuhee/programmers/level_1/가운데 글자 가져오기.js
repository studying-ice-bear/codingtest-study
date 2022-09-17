function solution(s) {
  let index = parseInt(s.length / 2);
  if (s.length % 2 === 0) {
    return s.slice(index - 1, index + 1);
  } else return s[index];
}
