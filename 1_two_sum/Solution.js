/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (const [x, i] of nums.entries()) {
    for (const [y, j] of nums.entries()) {
      if (i + j === target && x != y) return [x, y];
    }
  }
};

console.log(twoSum([3, 2, 4], 6));
