/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  return (
    String(x) ==
    String(x)
      .split("")
      .map((i) => i)
      .reverse()
      .join("")
  );
};

isPalindrome(123);
