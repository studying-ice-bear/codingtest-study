// charAt() 사용해서 다음에 풀어 볼 것
// 한줄 코드 참고 : s.split(' ').map(i => i.split('').map((j, key) => key % 2 === 0 ? j.toUpperCase() : j).join('')).join(' ')

function solution(s) {
  let answer = [];
  let array = s.split(" ");
  for (let i = 0; i < array.length; i++) {
    let word = array[i].split("");
    for (let j = 0; j < word.length; j++) {
      if (j % 2 === 1) {
        word[j] = word[j].toLowerCase();
      } else word[j] = word[j].toUpperCase();
    }
    answer.push(word.join(""));
  }
  return answer.join(" ");
}
