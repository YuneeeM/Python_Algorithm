package INF.april;

// study on 04/27/24
// Recursive Thinking (순환적으로 사고하기)

/*
 *문자열의 프린트
 */

class code10 {

  public static void main(String[] args) {
    printChars("ace");

  }

  public static void printChars(String str) {
    if (str.length() == 0) {
      return;
    } else {
      System.out.println(str.charAt(0));
      printChars(str.substring(1));
    }

  }
}