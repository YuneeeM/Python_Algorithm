package INF.april;

// study on 04/26/24

class code05 {

  public static void main(String[] args) {
    double result = power(2, 3);
    System.out.println(result);
  }

  public static double power(double x, int n) {
    if (n == 0) {
      return 1;
    } else {
      return x * power(x, n - 1);
    }
  }
}