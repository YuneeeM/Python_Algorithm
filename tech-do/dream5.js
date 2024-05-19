//5. 함수 -- 함수 실행 (함수 호출)

//함수 표현식 방법 - 함수는 한번 선언을 하면 변경되는 경우가 작기때문에 const로 선언함
//변수에 함수를 할당하는 방식이니 세미클론을 붙이삼
//함수의 이름은 변경되도 상관없음 어차피 변수의 이름으로 할당되는 거니까
//함수의 이름이 없는 경우도 존재 그것은 익명 함수임 == 근데 당연함 어차피 변수이름으로 호출하니까 함수 이름 없어도 되겠지
const printHello = function printHello() {
  console.log("hello");
};

printHello();

//함수 선언식 방법 - 끝에 세미콜론 안붙여도 됨
function gugudan() {
  for (var dan = 1; dan <= 9; dan++) {
    console.log("2 * " + dan + " = " + (2 * dan))
  }

}

gugudan();