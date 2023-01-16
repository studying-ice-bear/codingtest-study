function solution(priorities, location) {
  const newMap = priorities.map((priority, index) => ({
    priority,
    index,
  }));
  while (true) {
    const first = newMap.shift();
    if (newMap.some((item) => item.priority > first.priority)) {
      newMap.push(first);
    } else {
      if (first.index === location) {
        return priorities.length - newMap.length;
      }
    }
  }
}
