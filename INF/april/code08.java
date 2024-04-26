package INF.april;

// study on 04/26/24
// 최대공약수 : Euclid Method - 좀 더 단순한 버전

/*
 * 만약 q가 0이면 p이다.
 * 그렇지 않으면 gcd(m,n) = gcd(n,m%n)이다.
 */

class code08 {

  public static void main(String[] args) {
    int result = gcd(8, 4);
    System.out.println(result);
  }

  public static int gcd(int p, int q) {

    if (q == 0) {
      return p;
    } else {
      return gcd(q, p % q);
    }
  }
}