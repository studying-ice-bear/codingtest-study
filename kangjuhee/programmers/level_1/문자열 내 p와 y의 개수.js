function solution(s) {
  let word = s.toLowerCase();
  let p_num = 0;
  let y_num = 0;
  if (!word.includes("p") && !word.includes("y")) return true;
  else {
    p_num = word.split("").filter((i) => i === "p").length;
    y_num = word.split("").filter((i) => i === "y").length;
    return p_num === y_num ? true : false;
  }
}
