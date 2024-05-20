//6 연산

//1. variable, rw(read/write)
//let 
let globalName = 'global name';
{
  let name = 'ellie';
  console.log(name);
  name = 'hello';
  console.log(name);
  console.log(globalName);
}

//console.log(name);
console.log(globalName);

//2. Constant, only read
const name = 'yuni';

//------------------------
//1. String concatenation
console.log('my' + 'cat');
console.log('1' + 2);
console.log(`string literals: 

''''
  1+2 = ${1 + 2}`);

//2. Numeric operators
console.log(1 + 1);
console.log(1 - 1);
console.log(1 / 1);
console.log(1 * 1);
console.log(5 % 2);
console.log(2 ** 3);

//3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;
//counter = counter+1;
//preIncrement=counter;

console.log(preIncrement);

const postIncrement = counter++;
//postIncrement=counter;
//counter=counter+1;

console.log(postIncrement, counter);

//4. Assignment operators
let x = 3;
let y = 6;
x += y;
x -= y;
x *= y;
x /= y;

//5.comparision operators
console.log(10 < 6);
console.log(10 <= 6);
console.log(10 > 6);
console.log(10 >= 6);

//6. logical operators : ||, &&, !

//7. equality
const stringFive = '5';
const numberFive = 5;

console.log("********************")

// ==lose equality, with type conversion (똑같아)
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);

// === strict equality, no type conversion (타입이 다르니까 다르자나)
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

console.log("********************")

//object equality by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;

console.log(ellie1 == ellie2);
console.log(ellie1 === ellie2);
console.log(ellie1 === ellie3); //t


console.log("********************")

//equality - puzzler (correct!)
console.log(0 == false); //t
console.log(0 === false); //f
console.log('' == false); //t
console.log('' === false)//f
console.log(null == undefined); //t
console.log(null === undefined); //f


console.log("********************")
//8. conditional operators : if
//if,else if, else
const n = 'ellie';
if (n == 'ellie') {
  console.log('Welcome');
} else if (n === 'coder') {
  console.log('are you coder?');
} else {
  console.log('unknown');
}


console.log("********************")
//9. Ternary operator : ?
//condition ? value1 : value2;
console.log(n === 'ellie' ? 'yes' : 'no');

console.log("********************")
//10. switch statement
const browser = 'IE';
switch (browser) {
  case 'IE':
    console.log('go!');
    break;
  case 'Chrome':
    console.log('wowo');
    break;
  default:
    console.log('why?');
    break;
}

console.log("********************")
//11. loop
let i = 3;
while (i > 0) {
  console.log(`while: ${i}`);
  i--;
}

do {
  console.log(`do while : ${i}`)
  i--;
} while (i > 0);

console.log("********************")
//11. for loop

for (i = 3; i > 0; i--) {
  console.log(`for: ${i}`);
}

for (let i = 3; i > 0; i = i - 2) {
  console.log(`inline variable for : ${i}`);
}


//nested loops
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    console.log(`i: ${i}, j:${j}`)
  }
}







