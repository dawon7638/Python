/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
}

console.log(trim("      trim this or else   ")) // "trim this or else"

/*****************************************************************************/
[9:58 AM]
Algo 2 (option to do in python or JS for this one only)
/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @return {boolean} Whether s1 and s2 are anagrams.
 */

function isAnagram(s1, s2) {
}

console.log(isAnagram("listen", "silent"));
console.log(isAnagram("stop", "lots"));

/*****************************************************************************/

function trim(str) {
  var newString = "";
   for (i=0; i<str.length; i++){
     if (str[i] == " "){

     }
     else {
       console.log("this is I")
       console.log(i);
       break;
     }
   }
    for (j = str.length-1; j > 0; j--){
      if (str[j] == " "){
     }
     else {
       console.log("this is J")
       console.log(j);
       break;
     }
    }
     for (k = 0; k < str.length - 1; k++){
      if (k >= i && k <= j){
        newString = newString + str[k];
        
      }
     
   }
   return newString;
}

console.log(trim("      trim this or else   "))