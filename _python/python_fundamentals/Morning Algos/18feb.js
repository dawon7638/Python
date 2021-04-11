/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
//create a function that returns a new dict with only the items that are not doubles.

// Inside of the function we will create a for loop that iterates through the dict and check each item.  We will add that item that is not a duplicate to the new dict.

//After gathering non-duplicates in dictionary, return string with all keys of the dictionary

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "banana";
const expected3 = "ban";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @return {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
  var output = '' //empty string for output
  var uniques = {} //empty dictionary to keep track of unique characters
  for(var i = str.length-1; i >= 0; i--) { //iterate through string
    if(!uniques[str[i]]) { //check if letter exists in dict
      uniques[str[i]] = 1; //if not, add it
      output = str[i] + output; //and add it to the output string
    }
  }
  console.log(output); //return output
  return output;
}

stringDedupe(str1)
stringDedupe(str2)
stringDedupe(str3)

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str4 = "hello";
const expected4 = "olleh";

const str5 = "hello world";
const expected5 = "olleh dlrow";

const str6 = "abc def ghi";
const expected6 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @return {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
  var output = ''
  for(i in str) {
    output = str[i] + output
  }
  console.log(output)
  return output
}

reverseWords(str4)
reverseWords(str5)
reverseWords(str6)