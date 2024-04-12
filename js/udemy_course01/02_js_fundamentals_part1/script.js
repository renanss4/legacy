/*

// Introduction

let js = 'amazing';
if (js === 'amazing') alert('JavaScript is FUN!');

console.log(40+8+23-10);

// Values and Variables

let country = 'Portugal';
let continent = 'Europe';
let population = 10;

console.log(country);
console.log(continent);
console.log(population);

// Data Types

// Number: Floating point number -> Used for decimals and integers
let age = 23;

// String: Sequence of characters -> Used for text
let firstName = 'Jonas'

// Boolean: Logical type that can only be true or false -> Used for taking decisions
let fullAge = age;

// Undefined: Value taken by a variable that is not yet defined('empty value')
let children;

// Null: Also means 'empty value'

// Symbol (ES2015): Value that is unique and cannot be changed [Not useful for now]

// BigInt (ES2020): Larger integers than the Number type can hold

 * JavaScript has dynamic typing: We do not have to manyally define the data type of
 * the value stored in a variable. Instead, data types are determined automatically.


console.log(typeof true);
console.log(typeof 23);
console.log(typeof 'Jonas');
let year;
console.log(typeof year);
console.log(typeof null);


// let, const and var

let age = 30;
age = 31;
console.log(age);

const birthYear = 1991;
// birthYear = 1990; // It should not work. TypeError -> Assignment to constant variable

// Dubt: does this create a let, const or var?
// year = 1221
// console.log(year = 2024)
//
 * Response:
 * JavaScript treats it as a global variable if it's in the global
 * scope (outside of any function). If it's inside a function, it becomes a
 * variable in the function's scope.
 * 
 * It's best practice to always declare your variables explicitly using
 * let, const, or var to avoid potential issues with variable scoping and
 * unintended global variables
 //



// var is basically the old way of defining variables, prior to ES6
var job = 'programmer';
job = 'teacher';
console.log(job);


// Math operators

const now = 2037;
const ageJonas = now - 1991;
const ageSarah = now - 2022;
console.log(ageJonas, ageSarah);

console.log(ageJonas * 2, ageJonas / 10, 2 ** 3);
// 2 ** 3 means 2 to the power of 3 = 2 * 2 * 2

const firstName = 'Jonas';
const lastName = 'Schmedtmann';
console.log(firstName + ' ' + lastName)

let x = 10 + 5;
x += 10; // x = x + 10 = 25
x *= 4; // x = x * 4 == 100
x++; // x = x + 1
x--; // x = x - 1
x--; // x = x - 1
console.log(x);

// Comparison operators
console.log(ageJonas > ageSarah); // >, <, >=, <=
console.log(ageSarah >= 18);

const isFullAge = ageSarah >= 18;

console.log(now - 1991 > now - 2022);

CHALLENGE #1

// TEST DATA 1
let massMark = 78;
let heightMark = 1.69;
let massJohn = 92;
let heightJohn = 1.88;

const BMIMark = massMark / (heightMark * heightMark);
const BM1John = massJohn / (heightJohn * heightJohn);
console.log(BMIMark, BM1John);

// TEST DATA 2
massMark = 95;
heightMark = 1.88;
massJohn = 85;
heightJohn = 1.76;

console.log(BMIMark, BM1John);
*/

const firstName = 'Jonas';
const job = 'teacher';
const birthYear = 1991;
const year = 2037;

const jonas = "I'm " + firstName + ', a ' + (year -
birthYear) + ' years old' + job + '!';
console.log(jonas)

const jonasNew = `I'm ${firstName}, a ${year - birthYear} year old ${job}!`;
console.log(jonasNew);

console.log(`Just a regular string...`);

console.log('String with \n\
multiple \n\
lines');

console.log(`String
multiple
lines`);