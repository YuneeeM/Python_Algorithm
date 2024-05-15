//1. 변수 - 데이터를 담고 있는 아이
//키워드 let를 사용

//primitive 타입 - 가장 작은 단위를 담을 수 있음
// number, string, boolean, null, undefined, symbol
let number = 2;
let num = '2';

let number2 = number; //값 복사
console.log(number);
console.log(number2);


number2 = 3;

console.log(number);
console.log(number2);

//object는 한 두개의 데이터를 묶어놓은 데이터 타입(key-value로 구성)
let obj = {
  name: 'ellie',
  age: 5
};

console.log(obj.name);
console.log(obj.age);

let obj2 = obj; //주소값 복사

console.log(obj2.name);
console.log(obj2.age);

obj.name = 'james';
console.log('-------------');
console.log(obj.name);
console.log(obj2.name); //주소값을 공유하니 변경되는게 당연함

//let은 변경이 가능하지만 const는 상수변수라서 한번 초기화시 변경이 불가능함
const a = 2;


const obj3 = {
  name: 'ellie',
  age: 5
};

obj3.name = 'James'; //자체 레퍼런스 공간은 변경이 불가능하나, obj3가 가르키는 값은 변경이 가능
//구조 변경 불가, 값(안의 값)은 변경 가능



