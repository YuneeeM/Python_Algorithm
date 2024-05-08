package INF.may;

// study on 05/08/24

// 분할정복법 (divide and conquer)
// 퀵정렬(quickSort)
// O(nlogn)

/*
 * 분할 : 해결하고자 하는 문제를 작은 크기의 동일한 문제들로 분할
 * 정복 : 각각의 작은 문제를 순환적으로 해결
 * 합병 : 작은 문제의 해를 합하여(merge) 원래 문제에 대한 해를 구함 
 */

public class code30 {

  public static void quickSort(int[] arr) {
    if (arr == null || arr.length == 0) {
      return;
    }
    sort(arr, 0, arr.length - 1);
  }

  private static void sort(int[] arr, int low, int high) {
    int i = low;
    int j = high;
    // 피벗을 중앙 값으로 선택
    int pivot = arr[low + (high - low) / 2];

    // 분할
    while (i <= j) {
      while (arr[i] < pivot) {
        i++;
      }
      while (arr[j] > pivot) {
        j--;
      }
      if (i <= j) {
        exchange(arr, i, j);
        i++;
        j--;
      }
    }

    // 재귀적으로 정렬
    if (low < j) {
      sort(arr, low, j);
    }
    if (i < high) {
      sort(arr, i, high);
    }
  }

  private static void exchange(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  public static void main(String[] args) {
    int[] arr = { 10, 7, 8, 9, 1, 5 };
    System.out.println("정렬 전 배열: ");
    printArray(arr);
    quickSort(arr);
    System.out.println("\n정렬 후 배열: ");
    printArray(arr);
  }

  private static void printArray(int[] arr) {
    for (int i : arr) {
      System.out.print(i + " ");
    }
    System.out.println();
  }
}
