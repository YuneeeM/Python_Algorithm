package INF.april;

// study on 04/27/24
// Recursive Thinking (순환적으로 사고하기)

/*
 *배열의 합 구하기
 */

class code13 {

  public static void main(String[] args) {
    int[] datas = { 1, 2, 3, 4, 5 };
    System.out.println(sum(5, datas));
  }

  public static int sum(int n, int[] data) {
    if (n <= 0) {
      return 0;
    } else {
      return sum(n - 1, data) + data[n - 1];
    }
  }
}