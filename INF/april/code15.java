package INF.april;

// study on 04/28/24
// Desgining Recursion (순환 알고리즘의 설계)
// 암시적 매개변수를 명시적 매개변수로 바꾸어라

/* 이 함수의 미션은 data[0]에서 data[n-1] 사이에서 target을 검색하는 것이다.
 * 하지만 검색 구간의 시작 인덱스 0은 보통 생략한다. 즉, 암시적 매개변수이다.
 */

public class code15 {

  public static void main(String[] args) {
    int[] numbers = { 4, 7, 2, 9, 1 };
    int target = 2;
    int result = search(numbers, numbers.length, target);
    if (result != -1) {
      System.out.println("찾은 숫자 " + target + "의 인덱스: " + result);
    } else {
      System.out.println("찾는 숫자 " + target + "가 배열에 없습니다.");
    }
  }

  public static int search(int[] data, int n, int target) {
    for (int i = 0; i < n; i++) {
      if (data[i] == target) {
        return i;
      }
    }
    return -1;
  }
}
