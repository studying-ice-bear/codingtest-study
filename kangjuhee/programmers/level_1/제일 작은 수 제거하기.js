// Math.max 혹은 min에는 배열이 아니라 배열 안에 있는 요소 그 자체만 들어간다.
// 스프레드 연산자를 사용하면 [1, 2, 3] => 1, 2, 3으로 들어간다.
// 배열을 넣고싶으면 => Math.min.apply(null,array)

function solution(arr) {
  let newArr = arr;
  if (arr.length > 1) {
    newArr.splice(newArr.indexOf(Math.min(...newArr)), 1);
    return newArr;
  } else return [-1];
}
