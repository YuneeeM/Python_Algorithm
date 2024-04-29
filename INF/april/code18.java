package INF.april;

// study on 04/28/24

// Desgining Recursion (순환 알고리즘의 설계)
// 순차탐색 : 다른 버전

public class code18 {

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
    } else {
      int middle = (begin + end) / 2;
      if (data[middle] == target) {
        return middle;
      }
      int index = search(data, begin, middle - 1, target);
      if (index != -1) {
        return index;
      } else {
        return search(data, middle + 1, end, target);
      }
    }

  }

}
