/**
 * @param {string} sList
 * @return {number}
 */
var romanToInt = function (s) {
  let mapped_romans = {
    I: 1,
    V: 5,
    IV: 4,
    IX: 9,
    X: 10,
    XL: 40,
    L: 50,
    XC: 90,
    C: 100,
    CD: 400,
    D: 500,
    CM: 900,
    M: 1000,
  };
  let sum = 0,
    skip = false;
  sList = s.split("");
  for (const [x, i] of sList.entries()) {
    console.log(sList[x] + sList[x + 1]);
    if (skip) {
      console.log("skip");
      skip = false;
      continue;
    } else if (mapped_romans[sList[x] + sList[x + 1]] == null) {
      console.log("here");
      console.log(mapped_romans[i]);
      sum += mapped_romans[i];
    } else {
      sum += mapped_romans[sList[x] + sList[x + 1]];
      console.log(mapped_romans[sList[x] + sList[x + 1]]);
      skip = true;
    }
  }
  return sum;
};
console.log(romanToInt("DXXX"));
