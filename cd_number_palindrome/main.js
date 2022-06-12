function palindrome(num) {
  if (typeof num == "string" || num < 0) return "Not valid";
  let check_array = [];

  String(num)
    .split("")
    .forEach((i) => {
      if (check_array.includes(i)) {
        let j = check_array.indexOf(i);
        check_array.splice(j, 1);
      } else {
        check_array.push(i);
      }
    });
  return String(num).length == 1 ? false : check_array.length <= 1;
}

console.log(palindrome("ACCDDCCA"));
