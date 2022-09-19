function solution(num) {
  let number = num;
  let count = 0;
  while (number !== 1) {
    if (count >= 500) {
      count = -1;
      break;
    } else if (number === 0) {
      break;
    } else if (number % 2 === 0) {
      number = number / 2;
      count += 1;
    } else {
      number = number * 3 + 1;
      count += 1;
    }
  }
  return count;
}
