/**
 * @param {number[]} nums
 * @return {number[]}
 */
const runningSum = function (nums) {
  var sum = 0;
  const new_list = nums.map((x) => {
    sum += x;
    return sum;
  });
  return new_list;
};
