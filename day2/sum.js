function sum(start, end) {
  let temp = [];
  for (let i = start; i < end + 1; i += 1) {
    temp.push(i);
  }

  let answer = temp.reduce((acc, cur) => acc + cur);
  return console.log(answer);
}

sum(1, 100);
