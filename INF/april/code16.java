package INF.april;

// study on 04/28/24
// Desgining Recursion (순환 알고리즘의 설계)
// 매개변수의 명시화 : 순차 탐색

/*
 * 이 함수의 미션은 data[begin]에서 data[end] 사이에 target을
 * 검색한다. 즉, 검색구간의 시작점을 명시적으로 지정한다.
 */

public class code16 {

  public static void main(String[] args) {
    int[] numbers = { 4, 7, 2, 9, 1 };
    int target = 2;
    int result = search(numbers, 0, numbers.length - 1, target);
    if (result != -1) {
      System.out.println("찾은 숫자 " + target + "의 인덱스: " + result);
    } else {
      System.out.println("찾는 숫자 " + target + "가 배열에 없습니다.");
    }
  }

  public static int search(int[] data, int begin, int end, int target) {
    if (begin > end) {
      return -1;
    } else if (target == data[begin]) {
      return begin;
    } else {
      return search(data, begin + 1, end, target);
    }

  }

}
