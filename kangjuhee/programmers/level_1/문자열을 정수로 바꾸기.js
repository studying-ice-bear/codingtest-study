function solution(s) {
  if (s.startsWith("-")) {
    let array = s.split("");
    array.shift();
    return -Number(array.join(""));
  }
  return Number(s);
}
