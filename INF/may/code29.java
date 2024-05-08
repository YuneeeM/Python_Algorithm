package INF.may;

// study on 05/04/24

// 분할정복법 (divide and conquer)
// 합병정렬(mergeSort)
// O(nlogn)

/*
 * 분할 : 해결하고자 하는 문제를 작은 크기의 동일한 문제들로 분할
 * 정복 : 각각의 작은 문제를 순환적으로 해결
 * 합병 : 작은 문제의 해를 합하여(merge) 원래 문제에 대한 해를 구함 
 */

public class code29 {

  public static void mergeSort(int[] arr) {
    if (arr == null || arr.length < 2) {
      return;
    }
    int[] temp = new int[arr.length];
    mergeSort(arr, 0, arr.length - 1, temp);
  }

  private static void mergeSort(int[] arr, int left, int right, int[] temp) {
    if (left < right) {
      int mid = (left + right) / 2;
      mergeSort(arr, left, mid, temp);
      mergeSort(arr, mid + 1, right, temp);
      merge(arr, left, mid, right, temp);
    }
  }

  private static void merge(int[] arr, int left, int mid, int right, int[] temp) {
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
      if (arr[i] <= arr[j]) {
        temp[k++] = arr[i++];
      } else {
        temp[k++] = arr[j++];
      }
    }

    while (i <= mid) {
      temp[k++] = arr[i++];
    }

    while (j <= right) {
      temp[k++] = arr[j++];
    }

    for (i = left; i <= right; i++) {
      arr[i] = temp[i];
    }
  }

  public static void main(String[] args) {
    int[] arr = { 12, 11, 13, 5, 6, 7 };
    System.out.println("원래 배열:");
    printArray(arr);
    mergeSort(arr);
    System.out.println("합병 정렬 후 배열:");
    printArray(arr);
  }

  private static void printArray(int[] arr) {
    for (int num : arr) {
      System.out.print(num + " ");
    }
    System.out.println();
  }
}
