const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = Number(input.shift());
const sortedArr = input.sort((a, b) => a - b);

const getAverage = (arr) => {
  const result = Math.round(arr.reduce((a, b) => (a += b), 0) / N);
  return result === -0 ? 0 : result;
};

const getCenter = (arr) => {
  return arr[Math.floor(N / 2)];
};

const getMode = (arr) => {
  const freq = arr
    .sort((a, b) => a - b)
    .reduce((acc, cur) => {
      acc[cur] = (acc[cur] || 0) + 1;
      return acc;
    }, {}); //빈도를 reduce로 구해서 객체로 저장

  let minArr = []; //빈도 높은 것 중에서 두번째로 작은 key를 구해야함

  //가장 빈도 높은 value 구함
  let freqMax = Math.max(...Object.values(freq));
  //key를 활용해서 각각의 key의 value가 freqMax에 해당하면 minArr에 key 넣기
  Object.keys(freq).forEach((key) => {
    if (freq[key] === freqMax) {
      minArr.push(key);
    }
  });

  //minArr 길이를 구해서 하나면 그대로 내보내고, 그 이상이면 sort해 두번째를 내보냄
  let most;
  if (minArr.length > 1) {
    minArr.sort((a, b) => a - b);
    most = minArr[1];
  } else {
    most = minArr[0];
  }
  return most;
};

const getRange = (arr) => {
  return Math.max(...arr) - Math.min(...arr);
};

const answer =
  getAverage(sortedArr) +
  "\n" +
  getCenter(sortedArr) +
  "\n" +
  getMode(sortedArr) +
  "\n" +
  getRange(sortedArr);

console.log(answer);
