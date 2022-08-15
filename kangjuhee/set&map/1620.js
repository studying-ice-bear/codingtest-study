// 나는야 포켓몬 마스터 이다솜
// 해쉬(Hash)란 키(key)와 값(val) 짝을 이루는 dict 형태의 자료구조이다.
// Hash 함수를 통해 빠른 탐색이 가능하다. 시간복잡도 O(1).

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input
  .shift()
  .split(" ")
  .map((i) => +i);

let wordToNum = new Map();
let numToWord = new Map();
const dictionary = input.slice(0, N).map((i) => i.trimEnd());

for (let i = 0; i < dictionary.length; i++) {
  wordToNum.set(dictionary[i], i + 1);
  numToWord.set(i + 1, dictionary[i]);
}

const findArr = input.slice(N).map((i) => Number(i) || String(i).trimEnd());

for (let i = 0; i < findArr.length; i++) {
  if (wordToNum.has(findArr[i])) {
    console.log(wordToNum.get(findArr[i]));
  } else {
    console.log(numToWord.get(findArr[i]));
  }
}
