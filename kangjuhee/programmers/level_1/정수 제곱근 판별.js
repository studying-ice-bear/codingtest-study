function solution(n) {
  const squareNum = n ** 0.5;
  if (squareNum === parseInt(squareNum)) return (squareNum + 1) ** 2;
  else return -1;
}
