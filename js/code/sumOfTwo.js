/*
Given two lists of integers, is there a set of numbers — one from each list — whose sum is equal to a specified value
*/

function sumOfTwo(arrayA, arrayB, value) {
  for (let i = 0; i < arrayA.length; i++) {
    let diff = value - i;
    if (diff in arrayB) {
      return true;
    }
  }
  return false;
}
