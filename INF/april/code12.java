package INF.april;

// study on 04/27/24
// Recursive Thinking (순환적으로 사고하기)

/*
 *2진수로 변환하여 출력
 */

class code12 {

  public static void main(String[] args) {
    printInBinary(10);

  }

  public static void printInBinary(int n) {
    if (n < 2) {
      System.out.print(n);
    } else {
      printInBinary(n / 2);
      System.out.print(n % 2);
    }
  }
}