// 재귀함수가 뭔가요?

const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

const recursive = (n) => {
  const sign = "_".repeat((n - 1) * 4);
  const question =
    "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다." + "\n";
  const text = `${sign}"재귀함수가 뭔가요?"\n${sign}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n${sign}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n${sign}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."`;

  if (n < 2) {
    return question + text;
  }
  return recursive(n - 1) + "\n" + text;
};

const final_answer = (n) => {
  const sign = "_".repeat(n * 4);

  let talking = "";
  for (let i = n; i >= 0; i--) {
    const sign2 = "_".repeat(i * 4);
    if (i === 0) talking += `${sign2}라고 답변하였지.`;
    else talking += `${sign2}라고 답변하였지.\n`;
  }

  const text = `${sign}"재귀함수가 뭔가요?"\n${sign}"재귀함수는 자기 자신을 호출하는 함수라네"\n${talking}`;
  return text;
};

console.log(recursive(input) + "\n" + final_answer(input));
