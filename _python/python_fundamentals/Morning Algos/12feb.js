/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization

  // Create a functino that takes in a parameter of a (string) 
  Have a for loop that checks the string cascasding to the middle: comparing len of string of i to length of string -1 -i.
  // Check if the arr[i] is equal to arr[i], if not equal return false
 */



// const str1 = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected3 = false;

// const str4 = "oho!";
// const expected4 = false;


/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
    for(var i = 0; i<str.length/2; i++){
      if(str[i] != str[str.length - 1 -i]){
        return false;
      }
    }
    return true;
  }
  // console.log(isPalindrome(str4))
  // module.exports = { isPalindrome };
  
  /*****************************************************************************/
  //Ninja Bonus Algo:
  /* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
  
    Use isPalindrome Function 
    Have a  function that takes in 
    Declare variable subString 
    Create a for loop that iterates through the string, Starting at 0 
    
  */
  
  // const { isPalindrome } = require("./isPalindrome");
  
  const str1 = "what up, daddy-o?";
  const expected1 = "dad";
  
  const str2 = "uh, not much";
  const expected2 = "u";
  
  const str3 = "Yikes! my favorite racecar erupted!";
  const expected3 = "e racecar e";
  
  /**
   * Finds the longest palindromic substring in the given string.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @return {string} The longest palindromic substring from the given string.
   */
  function longestPalindromicSubstring(str) {
      var subString = "";
      var returnString = str[0];
      if(isPalindrome(str)) {
        return str;
      }
      for(var i = 0; i < str.length-1; i++) {
        for(var j = i+1; j < str.length; j++) {
          substring = str.substring(i, j-i);
          if(isPalindrome(substring)) {
            if(substring.length > returnString.length)
              returnString = substring;
          }
        }
      }
  
      return returnString;
  }
  console.log(longestPalindromicSubstring(str1), longestPalindromicSubstring(str1) == expected1);
  console.log(longestPalindromicSubstring(str2), longestPalindromicSubstring(str2) == expected2);
  console.log(longestPalindromicSubstring(str3), longestPalindromicSubstring(str3) == expected3);
  