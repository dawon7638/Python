/* 
  Recursive Sigma
  Input: integer
  Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 */
function recursiveSigma(n) {
  // get rid of decimals
  const int = parseInt(n);

  // Termination Condition if it's bad data (not a number)
  if (isNaN(int)) {
    return null;
  }

  // base case
  if (int < 1) {
    return 0;
  }
  // if the return keyword is missing below, undefined will be returned because
  // the above return happens in a nested recursive call and doesn't make it all the way out
  return int + recursiveSigma(int - 1);
}

console.log(recursiveSigma(num1));
console.log(recursiveSigma(num2));
console.log(recursiveSigma(num3));
[11:02 AM]
Second algo exercise:
/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @return {number} The sum of the given nums.
 */
function sumArr(nums) {}

module.exports = { sumArr };

/*****************************************************************************/

Message #🏫cohort-sadie