package INF.april;

// study on 04/28/24

// Desgining Recursion (순환 알고리즘의 설계)
// 최대값 찾기 : 다른 버전

public class code20 {

  public static void main(String[] args) {
    int[] arr = { 2, 8, 5, 4, 7, 9 };
    int index = findMax(arr, 0, arr.length - 1);
    System.out.println(index);
  }

  public static int findMax(int[] data, int begin, int end) {
    if (begin == end) {
      return data[begin];
    } else {
      int middle = (begin + end) / 2;
      int max1 = findMax(data, begin, middle);
      int max2 = findMax(data, middle + 1, end);
      return Math.max(max1, max2);
    }
  }

}
