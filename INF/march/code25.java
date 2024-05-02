package INF.march;

// study on 05/02/24

// Recursion의 응용
// 멱집합 : powerset

/*
 * {a,b,c,d,e,f}의 모든 부분집합을 나열하려면
 * a를 제외한 {b,c,d,e,f}의 모든 부분집합들을 나열하고
 * {b,c,d,e,f}의 모든 부분집합에 {a}를 추가한 집합들을 나열한다. 
 */

public class code25 {

  private static char data[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
  private static int n = data.length;
  private static boolean[] include = new boolean[n];

  public static void powerSet(int k) {
    if (k == n) {
      for (int i = 0; i < n; i++) {
        if (include[i]) {
          System.out.print(data[i] + " ");
        }
      }
      System.out.println();
      return;
    }
    include[k] = false;
    powerSet(k + 1);
    include[k] = true;
    powerSet(k + 1);

  }

  public static void main(String[] args) {
    powerSet(0);
  }
}
