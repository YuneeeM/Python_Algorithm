package INF.april;

// study on 04/28/24

// Desgining Recursion (순환 알고리즘의 설계)
// 

public class code20 {

  public static void main(String[] args) {
    int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int index = findMax(arr, 0, arr.length - 1);
    System.out.println(index);
  }

  public static int findMax(int[] data, int begin, int end) {
    if (begin == end) {
      return data[begin];
    } else {
      return Math.max(data[begin], findMax(data, begin + 1, end));
    }
  }

}
