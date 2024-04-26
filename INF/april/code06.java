package INF.april;

// study on 04/26/24
// 피보나치 수열
class code06 {

  public static void main(String[] args) {
    int result = fibo(6);
    System.out.println(result);
  }

  public static int fibo(int n) {
    if (n < 2) {
      return n;
    } else {
      return fibo(n - 1) + fibo(n - 2);
    }
  }
}