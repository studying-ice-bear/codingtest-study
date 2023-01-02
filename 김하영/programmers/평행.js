function solution(dots) {
  let answer = 0;
  for (let i = 1; i < dots.length; i++) {
    let slopeA = 0;
    let slopeB = 0;
    const firstDots = dots[0];
    const partnerDots = dots[i];
    const compareDots = dots.filter((_, index) => index !== i && index !== 0);
    console.log(compareDots);

    slopeA = Math.abs(
      (firstDots[1] - partnerDots[1]) / (firstDots[0] - partnerDots[0])
    );
    slopeB = Math.abs(
      (compareDots[0][1] - compareDots[1][1]) /
        (compareDots[0][0] - compareDots[1][0])
    );
    if (slopeA === slopeB) {
      answer = 1;
    }
  }

  return answer;
}
