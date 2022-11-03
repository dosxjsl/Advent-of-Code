const fs = require("fs");
const test = fs.readFileSync("D5.txt", "utf8");
let nice = 0;
//--------------Functions--------------//
//--------------Main Code--------------//
let cut = test.split(/\r?\n/);

for (let i = 0; i < cut.length; i++) {
  var repeat = 0;
  var doubles = 0;
  var s = cut[i];

  for (let j = 0; j < s.length; j++) {
    for (let k = 0; k < s.length - 1; k++) {
      for (let l = k + 1; l < s.length; l++) {
        let pair = s[k] + s[k + 1];
        if (pair == s[l + 1] + s[l + 2]) {
          doubles++;
        }
      }
    }
    if (s[j] == s[j + 2]) {
      repeat++;
    }
  }
  if (doubles >= 2 && repeat >= 1) {
    nice++;
  }
}
console.log(nice);
