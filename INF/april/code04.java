package INF.april;

// study on 04/26/24

/*
 * 정리 : factorial(int n)은 음이 아닌 정수 n에 대해서 n!을 올바로 계산함
 * 
 * 증명:
 * 1. n=0인 경우 : n=0인 경우 1을 반환함 - 올바르다
 * 2. 임의의 양의 정수 k에 대해서 n<k인 경우 n!을 올바르게 계산하야 반환한다고 가정
 * 3. n=k인 경우를 고려해보자. factorial은 먼저 factorial(k-1) 호출하는데 2번의 가정에 의해서 (k-1)!이 올바로 계산되어 반환된다.
 * 메서드 factorial은 k*(k-1)! = k! 반환한다.
 */

class code04 {

  public static void main(String[] args) {
    int result = factorial(4);
    System.out.println(result);
  }

  // 이 함수의 mission은 factorial(k)!을 구하는 것
  public static int factorial(int n) {
    if (n == 0) {
      // n=0이라면 1이다.
      return 1;
    } else {
      // n이 0보다 크다면 0에서 n까지의 곱은 0에서 n-1까지의 합에 n을 더한 것
      return n * factorial(n - 1);
    }
  }
}