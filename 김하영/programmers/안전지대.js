function solution(board) {
  const danger = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];
  const newBoard = Array.from(Array(board.length), () =>
    Array(board.length).fill(0)
  );
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] === 1) {
        for (let k = 0; k < danger.length; k++) {
          const [x, y] = danger[k];
          if (
            i + x < 0 ||
            i + x >= board.length ||
            j + y < 0 ||
            j + y >= board.length ||
            board[i + x][j + y] === 1
          ) {
            continue;
          }
          newBoard[i + x][j + y] = 1;
        }
      }
    }
  }

  const answer = newBoard.reduce((acc, cur) => {
    return acc + cur.reduce((acc, cur) => acc + cur, 0);
  }, 0);

  return answer;
}
