const fs = require("fs");
const test = fs.readFileSync("D5.txt", "utf8");
let nice = 0;
let naughty = 0;
//--------------Functions--------------//
//--------------Main Code--------------//
let cut = test.split(/\r?\n/);

for (let i = 0; i < cut.length; i++) {
  var naughty4Word = false;
  var vowels = 0;
  var repeat = 0;
  var s = cut[i];

  for (let j = 0; j < s.length; j++) {
    if (
      s[j] + s[j + 1] == "ab" ||
      s[j] + s[j + 1] == "cd" ||
      s[j] + s[j + 1] == "pq" ||
      s[j] + s[j + 1] == "xy"
    ) {
      naughty++;
      naughty4Word = true;
    } else {
      if (
        s[j] == "a" ||
        s[j] == "e" ||
        s[j] == "i" ||
        s[j] == "o" ||
        s[j] == "u"
      ) {
        vowels++;
      }
      if (s[j] == s[j + 1]) {
        repeat++;
      }
    }
  }
  if (vowels >= 3 && repeat >= 1 && naughty4Word != true) {
    nice++;
  }
}
console.log(nice);
