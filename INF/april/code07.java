package INF.april;

// study on 04/26/24
// 최대공약수 : Euclid Method

/*
 * m>=n인 두 양의 정수 m과 n에 대해서 m이 n의 배수이면 gcd(m,n)=n이고, 
 * 그렇지 않으면 gcd(m,n) = gcd(n,m%n)이다.
 */
class code07 {

  public static void main(String[] args) {
    int result = gcd(8, 4);
    System.out.println(result);
  }

  public static int gcd(int m, int n) {
    if (m < n) {
      int tmp = m;
      m = n;
      n = tmp; // swap m and n
    }

    if (m % n == 0) {
      return n;
    } else {
      return gcd(n, m % n);
    }
  }
}