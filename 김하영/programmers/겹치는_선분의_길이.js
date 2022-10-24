function compare(line1, line2) {
  // 겹치는 경우
  let a = Infinity;
  let b = Infinity;
  if (line1[1] < line2[1]) {
    // 온전히 겹칠 때
    if (line1[0] >= line2[0]) {
      a = line1[0];
      b = line1[1];
    } else if (line1[0] < line2[0]) {
      // 일부만 겹칠 때
      if (line1[1] > line2[0]) {
        a = line2[0];
        b = line1[1];
      }
    }
  } else {
    // 온전히 겹칠 때
    if (line2[0] >= line1[0]) {
      a = line2[0];
      b = line2[1];
    } else if (line2[0] < line1[0]) {
      // 일부만 겹칠 때
      if (line2[1] > line1[0]) {
        a = line1[0];
        b = line2[1];
      }
    }
  }

  return [a, b];
}

function solution(lines) {
  let answer = 0;
  const arr = Array(200).fill(0);
  const length = lines.length;
  lines = lines.map((line) => line.sort((a, b) => a - b));

  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      const overlay = compare(lines[i], lines[j]);
      for (let k = overlay[0]; k < overlay[1] + 1; k++) {
        arr[k + 100] = 1;
      }
    }
  }
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] === 1 && arr[i] === 1) {
      answer++;
    }
  }

  return answer;
}
