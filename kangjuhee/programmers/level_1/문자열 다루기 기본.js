// 정규표현식 사용해서 문제 푸는 것이 수월하다.
// 참고 링크 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jeongju02&logNo=221517177533

function solution(s) {
  return (s.length === 4 || s.length === 6) && /^[0-9]+$/.test(s);
}

// function solution(s) {
//   return s.search(/\D/g) < 0 && (s.length === 4 || s.length === 6);
// }
