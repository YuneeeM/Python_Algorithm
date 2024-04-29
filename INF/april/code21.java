package INF.april;

// study on 04/28/24

// Desgining Recursion (순환 알고리즘의 설계)
// Binary Search

public class code21 {

  public static void main(String[] args) {
    String[] items = { "apple", "banana", "cherry", "grape", "orange", "strawberry" };
    String target = "orange";
    int result = binarySearch(items, target, 0, items.length - 1);
    if (result != -1) {
      System.out.println("타겟 '" + target + "'은(는) 배열의 인덱스 " + result + "에 있습니다.");
    } else {
      System.out.println("타겟 '" + target + "'을(를) 찾을 수 없습니다.");
    }

  }

  public static int binarySearch(String[] items, String target, int begin, int end) {
    if (begin > end) {
      return -1;
    } else {
      int middle = (begin + end) / 2;
      int compResult = target.compareTo(items[middle]);
      if (compResult == 0) {
        return middle;
      } else if (compResult < 0) {
        return binarySearch(items, target, begin, middle - 1);
      } else {
        return binarySearch(items, target, middle + 1, end);
      }
    }
  }

}
