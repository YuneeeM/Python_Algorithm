package INF.april;

// study on 04/26/24
// 순환함수와 수학적 귀납법

/*
 * 정리 : func(int n)은 음이 아닌 정수 n에 대해서 0에서 n까지의 합을 올바로 계산함
 * 
 * 증명:
 * 1. n=0인 경우 : n=0인 경우 0을 반환함 - 올바르다
 * 2. 임의의 양의 정수 k에 대해서 n<k인 경우 0에서 n까지의 합을 올바르게 계산하야 반환한다고 가정
 * 3. n=k인 경우를 고려해보자. func은 먼저 func(k-1) 호출하는데 2번의 가정에 의해서 0에서 k-1까지의 합이 올바로 계산되어 반환된다.
 * 메서드 func은 그 값에 n을 더해서 반환한다. 따라서 메서드 func은 0에서 k까지의 합을 올바로 계산하여 반환한다.
 */

class code03 {

  public static void main(String[] args) {
    int result = func(4);
    System.out.println(result);
  }

  // 이 함수의 mission은 0~n까지의 합을 구하는 것
  public static int func(int n) {
    if (n == 0) {
      // n=0이라면 합은 0이다.
      return 0;
    } else {
      // n이 0보다 크다면 0에서 n까지의 합은 0에서 n-1까지의 합에 n을 더한 것
      return n + func(n - 1);
    }
  }
}