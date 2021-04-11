/* 
    Given an arr and a separator string, output a string of every item in the array separated by the separator.

    No trailing separator at the end
    Default the separator to a comma with a space after it if no separator is provided
*/
const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";
/*
    iterate by for loop through the arr 1 by 1 by index, concatenate it to a new string.
    Target the start and end of the array(?)
*/

function join(arr, separator=", ") {
  new_string = "";
  for (var x=0; x<arr.length; x++){
    if (x == 0){
      new_string += arr[x]
    } else {
      new_string += (separator + arr[x])
    }
  }
  return new_string
}
console.log(join(arr1, separator1))


# /*****************************************************************************/
# Algo 2:
# /* 
#   Book Index
#   Given an arry of ints representing page numbers
#   return a string with the page numbers formatted as page ranges when the nums span a consecutive range
# */

# const nums1 = [1, 13, 14, 15, 37, 38, 70];
# const expected1 = "1, 13-15, 37-38, 70";

# /**
#  * Turns the given arr of page numbers into a string of comma hyphenated
#  * page ranges.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {Array<number>} nums Page numbers.
#  * @return {string} The given page numbers as comma separated hyphenated
#  *    page ranges.
#  */
# function bookIndex(nums) {}

# module.exports = { bookIndex };
