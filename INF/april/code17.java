package INF.april;

// study on 04/28/24
// Desgining Recursion (순환 알고리즘의 설계)
// 순차탐색 : 다른 버전

/*
 * 이 함수의 미션은 data[begin]에서 data[end] 사이에 target을
 * 검색한다. 즉, 검색구간의 시작점을 명시적으로 지정한다.
 */

public class code17 {

  public static void main(String[] args) {
    int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int target = 6;
    int index = search(arr, 0, arr.length - 1, target);
    if (index != -1) {
      System.out.println("Target found at index: " + index);
    } else {
      System.out.println("Target not found in the array.");
    }
  }

  public static int search(int[] data, int begin, int end, int target) {
    if (begin > end) {
      return -1;
    } else if (target == data[end]) {
      return end;
    } else {
      return search(data, begin, end - 1, target);
    }

  }

}
