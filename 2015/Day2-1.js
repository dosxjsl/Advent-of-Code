const fs = require("fs");
const test = fs.readFileSync("D2.txt", "utf8");
var total = 0;

function boxSurfaceArea(length, width, height) {
  return 2 * length * width + 2 * width * height + 2 * height * length;
}

function findSmallestArea(l, w, h) {
  let area1 = l * w;
  let area2 = l * h;
  let area3 = w * h;
  return Math.min(area1, area2, area3);
}

let cut = test.split(/\r?\n/);
for (let i = 0; i < cut.length; i++) {
  var s = cut[i].split("x");
  for (let j = 0; j < s.length; j++) {
    s[j] = parseInt(s[j]);
  }
  BSA = boxSurfaceArea(s[0], s[1], s[2]);
  FSA = findSmallestArea(s[0], s[1], s[2]);
  total = total + BSA + FSA;
}
console.log(`Total: ${total}`);
