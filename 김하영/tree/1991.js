const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const solution = (input) => {
  const N = +input[0];
  input = input.slice(1);
  const tree = {};
  for (let i = 0; i < N; i++) {
    const [node, left, right] = input[i]
      .split(" ")
      .map((node) => node.replace(/\n|\r|\s*/g, ""));
    tree[node] = [left, right]; // 객체에 key: node, value: [left, right]로 저장
  }
  let result = "";

  function preorder(node) {
    if (node === ".") return;
    const [lt, rt] = tree[node];
    result += node;
    preorder(lt);
    preorder(rt);
  }

  function inorder(node) {
    if (node === ".") return;
    const [lt, rt] = tree[node];
    inorder(lt);
    result += node;
    inorder(rt);
  }

  function postorder(node) {
    if (node === ".") return;
    const [lt, rt] = tree[node];
    postorder(lt);
    postorder(rt);
    result += node;
  }

  preorder("A");
  result += "\n";
  inorder("A");
  result += "\n";
  postorder("A");

  return result;
};

console.log(solution(input));
