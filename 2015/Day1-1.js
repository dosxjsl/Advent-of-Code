//https://adventofcode.com/2015

// const input = "()(()()()()()()()()(((()())(()()()())()()(()()()()()())()()(((()))()()()";
const fs = require("fs");
const input = fs.readFileSync("D1.txt", "utf8");
const split_input = input.split("");
let floor = 0;

/*
split_input.forEach((p) => {
  if (p == "(") {
    floor++;
  } else if (p == ")") {
    floor--;
  }
});
*/

for (const string of input) {
  if (string == "(") {
    floor++;
  } else if (string == ")") {
    floor--;
  }
}

// for (let i = 0; i < input.length; i++) {
//   if (input[i] == "(") {
//     floor++;
//   } else if (input[i] == ")") {
//     floor--;
//   }
// }
console.log(floor);
