package INF.april;

import java.util.Scanner;

// study on 04/27/24
// Recursive Thinking (순환적으로 사고하기)
//데이터파일로 부터 n개의 정수 읽어오기

/*
 모든 순환함수는 반복문으로 변경이 가능(그 역도 성립함)
 순환함수는 복잡한 알고리즘을 단수하게 하지만 - 함수 호출에 따른 오버헤드 존재
 (매개변수 전달, 액티베이션-프레임 생성)
 */

public class code14 {

  public static void main(String[] args) {
    code14 instance = new code14(); // code14 클래스의 객체 생성
    int[] data = new int[5]; // 데이터 배열 생성
    Scanner scanner = new Scanner(System.in); // Scanner 객체 생성

    instance.readFrom(5, data, scanner); // readFrom 메소드 호출

    // 입력된 데이터 출력
    System.out.print("입력된 데이터: ");
    for (int i = 0; i < data.length; i++) {
      System.out.print(data[i] + " ");
    }
    System.out.println();
  }

  public void readFrom(int n, int[] data, Scanner in) {
    if (n == 0) {
      return;
    } else {
      readFrom(n - 1, data, in);
      data[n - 1] = in.nextInt();
    }
  }
}