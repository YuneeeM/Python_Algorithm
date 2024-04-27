package INF.april;

// study on 04/27/24
// Recursive Thinking (순환적으로 사고하기)

/*
 *문자열의 길이 계산 
 */

class code09 {

  public static void main(String[] args) {
    String s = "ace";
    System.out.println(length(s));

  }

  public static int length(String str) {
    if (str.equals("")) {
      return 0;
    } else {
      return 1 + length(str.substring(1));
    }

  }
}