/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const max = nums.reduce((acc, cur) => Math.max(acc, cur), -Infinity);
  const min = nums.reduce((acc, cur) => Math.min(acc, cur), Infinity);
  const dp = Array(nums.length).fill(0);
  dp[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
  }
  return Math.max(...dp);
};

console.log(maxSubArray([10, -1, 2, 3, -4, 5, 6, -7, 8, 9]));
