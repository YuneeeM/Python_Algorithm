//변수
// var : 전역변수 지역변수 가능 this 사용가능, 재정의 가능
// let은 재정의 불가능

let num = 2;
let num2 = num; //값 복사

// const는 상수라서 초기화후 재변경 불가능


//---------------------------------------

//Boolean, Null, undefined, number, string, symbol, object

console.log(1 + 1);
console.log(2 - 1);
console.log(4 / 2);
console.log(4 * 2);

//문자열
console.log("Hello world");
console.log('Hello world');
//String.length - properties
console.log('Hello world'.length);
//toUpperCase - method (대문자 변환)
console.log('Hello world'.toUpperCase());
//indexof (데이터의 위치 변환)
console.log('Hello world'.indexOf('o'));

//문자열+문자열 = 문자열
console.log("2" + "1");

//----------------------------------

//배열
var con = ["a", "b"]

console.log(con[0]);
console.log(con.length);
console.log(con.push("c"));

//--------------------------------

//객체 - 값을 받는 그릇

var grades = { "ab": 100, "b": 200, "c": 300 };

console.log(grades["ab"]);
console.log(grades["a" + "b"]);

for (key in grades) {
  console.log("key : " + key + " value : " + grades[key]);
}

//함수 

const print = function print() {
  console.log("Hello");
};

print();

const pp = function () {
  console.log("H");
}

pp();



const a = ['김', '나', '박', '이'];
let b = a.pop()
b = a.pop()
console.log(b)