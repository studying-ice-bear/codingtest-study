const solution = (num) => {
  if (num === 0) {
    return 1;
  }
  if (num < 2) {
    return num;
  }

  return solution(num - 1) * num;
};

// reduce 방법으로 푸는법
const factorialReduce = (num) => {
  if (num < 2) {
    return num;
  }
  let arr = [];
  for (let i = 1; i <= num; i++) {
    arr.push(i);
  }
  return arr.reduce((a, b) => a * b);
};

console.log(factorialReduce(10));
