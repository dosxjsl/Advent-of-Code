const fs = require("fs");
const test = fs.readFileSync("D2.txt", "utf8");
var total = 0;

//--------------Functions--------------//
function bow(l, w, h) {
  return l * w * h;
}

function present(l, w, h) {
  let sides = [l, w, h];
  sides.sort(function (a, b) {
    return a - b;
  });

  return 2 * sides[0] + 2 * sides[1];
}

//--------------Main Code--------------//
let cut = test.split(/\r?\n/);

for (let i = 0; i < cut.length; i++) {
  var s = cut[i].split("x");
  for (let j = 0; j < s.length; j++) {
    s[j] = parseInt(s[j]);
  }
  p = present(s[0], s[1], s[2]);
  b = bow(s[0], s[1], s[2]);
  total = total + b + p;
}
console.log(`Total: ${total}`);
