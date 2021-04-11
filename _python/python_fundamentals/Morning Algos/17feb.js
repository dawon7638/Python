
 /* 
  Given an array of strings
  return an object with sums to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/
// create new dictionary
// loop through array
// have conditional that checks if arry(i) is in the new dictionary, if it is, it adds to the value, if noyt, it creates a new key value pair.
// function frequencyTableBuilder(arr) {
//   var new_dictionary = {}
//   for(var i = 0; i<arr.length; i++){
//     if ( new_dictionary.hasOwnProperty(arr[i])) {
//       new_dictionary[arr[i]] += 1
//     }
//     else {
//       new_dictionary[arr[i]] = 1  
//     }  
//   }
//   return new_dictionary
// }


// const arr1 = ["a", "a", "a"];
// const expected1 = {
//   a: 3,
// };

// const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// const expected2 = {
//   a: 2,
//   b: 1,
//   c: 3,
//   B: 1,
//   d: 1,
// };

// const arr3 = [];
// const expected3 = {};

// console.log(frequencyTableBuilder(arr3))

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @return {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
//function frequencyTableBuilder(arr) {
//  var i = 0;
//}

//module.exports = { frequencyTableBuilder };

// Syntax
// DictionaryObject.Exists(key)

// <%
// dim d
// set d=Server.CreateObject("Scripting.Dictionary")
// d.Add "n","Norway"
// d.Add "i","Italy"
// d.Add "s","Sweden"

// if d.Exists("n")=true then
//   Response.Write("Key exists!")
// else
//   Response.Write("Key does not exist!")
// end if

// set d=nothing
// %>

// Output:

// Key exists!

/*****************************************************************************/

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

//Create a new string that will display previous string in reverse order.
//newstr=""


//const str1 = "This is a test";
//const expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @return {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
//function reverseWordOrder(wordsStr) {}

//module.exports = { reverseWordOrder };

/*****************************************************************************/


// #  Given an array of strings
// #  return an object with sums to represent how many times each array item is found (a frequency table)
// #  Useful methods:
// #    Object.hasOwnProperty("keyName")
// #      - returns true or false if the object has the key or not
// #    Python: key in dict
// #*/


// # const arr1 = ["a", "a", "a"];
// # const expected1 = {
// #   a: 3,
// # };

// arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// expected2 = {
//   "a": 2,
//   "b": 1,
//   "c": 3,
//   "B": 1,
//   "d": 1,
// };

// # const arr3 = [];
// # const expected3 = {};


// def frequencyTableBuilder(arr):
//   new_dict = {}
//   for i in range(len(arr)):
//     if str(arr[i]) in new_dict:
//       new_dict[str(arr[i])] +=1
//     else:
//       new_dict[str(arr[i])] = 1
//   return new_dict

// print(frequencyTableBuilder(arr2))


    





// # /**
// #  * Builds a frequency table based on the given array.
// #  * - Time: O(?).
// #  * - Space: O(?).
// #  * @param {Array<string>} arr
// #  * @return {Object<string, number>} A frequency table where the keys are items
// #  *    from the given arr and the values are the amnt of times that item occurs.
// #  */
// # function frequencyTableBuilder(arr) {
// #   var i = 0;
// # }

// # module.exports = { frequencyTableBuilder };
