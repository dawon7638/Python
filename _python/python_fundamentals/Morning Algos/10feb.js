/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @return {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(strA, strB) {

}

module.exports = { caseInsensitiveStringCompare };




// # Acronyms
// #   Create a function that, given a string, returns the string’s acronym 
// #   (first letter of each word capitalized). 
// #   Do it with .split first if you need to, then try to do it without
// # */

// # /**
// #  * Turns the given str into an acronym.
// #  * - Time: O(?).
// #  * - Space: O(?).
// #  * @param {string} str A string to be turned into an acronym.
// #  * @return {string} The given str converted into an acronym.
// #  */

// # // without using .split()
// # function acronymize(str) {

// # }

// # // Test cases
// # const str1 = " there's no free lunch - gotta pay yer way. ";
// # const expected1 = "TNFL-GPYW";

// # const str2 = "Live from New York, it's Saturday Night!";
// # const expected2 = "LFNYISN";

// # const str3 = "              ";
// # const expected3 = "";

// # const str4 = "LivefromNewYork,it'sSaturdayNight!";
// # const expected4 = "L";

// # const str5 = "     there's     no free lunch -     gotta pay yer way.    ";
// # const expected5 = "TNFL-GPYW";