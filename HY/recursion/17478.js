// const fs = require("fs");

// const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
let tab = 0;
let boolean = false;
let str = "";
const solution = (num) => {
  if (num !== tab && boolean === false) {
    str += `${"____".repeat(tab)}"재귀함수가 뭔가요?"\n${"____".repeat(
      tab
    )}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n${"____".repeat(
      tab
    )}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n${"____".repeat(
      tab
    )}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n`;
    tab = tab + 1;
    if (num === tab) {
      boolean = true;

      str += `${"____".repeat(tab)}"재귀함수가 뭔가요?"\n${"____".repeat(
        tab
      )}"재귀함수는 자기 자신을 호출하는 함수라네"\n${"____".repeat(
        tab
      )}라고 답변하였지.\n`;
      tab = tab - 1;
      return solution(num);
    }
    return solution(num);
  }
  if (num !== tab && boolean === true) {
    str += `${"____".repeat(tab)}라고 답변하였지.\n`;
    tab = tab - 1;
    if (tab === 0 && boolean === true) {
      str += `라고 답변하였지.\n`;
      return;
    }
    return solution(num);
  }
};

console.log("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
solution(50);
console.log(str);

//  RangeError가 나옴