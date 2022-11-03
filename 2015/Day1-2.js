//https://adventofcode.com/2015

const fs = require("fs");
const input = fs.readFileSync("D1.txt", "utf8");
const split_input = input.split("");
let floor = 0;
let firstNeg;
let flag = false;

for (let i = 0; i < input.length; i++) {
  if (input[i] == "(") {
    floor++;
  } else if (input[i] == ")") {
    floor--;
  }

  if (floor == -1 && flag == false) {
    firstNeg = i + 1;
    flag = true;
  }
}
console.log(floor);
console.log(firstNeg);
