// 소트인사이드

let input = require("fs").readFileSync("../input.txt").toString().trim();
input = input.split("");
console.log(input.sort((a, b) => b - a).join(""));
