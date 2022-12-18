// 구구단
for (let i = 1; i <= 9; i++) {
  if (i % 4 === 0) continue;
  let str = "";
  for (let j = 2; j <= 5; j++) {
    const blank = i * j < 10 ? "   " : "  ";
    str += `${j} * ${i} = ${i * j}${blank}`;
  }
  console.log(str);
}
console.log("\n");
for (let i = 1; i <= 9; i++) {
  if (i % 4 === 0) continue;
  let str = "";
  for (let j = 6; j <= 9; j++) {
    const blank = i * j < 10 ? "   " : "  ";
    str += `${j} * ${i} = ${i * j}${blank}`;
  }
  console.log(str);
}
