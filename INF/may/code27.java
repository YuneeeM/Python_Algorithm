package INF.may;

// study on 05/03/24

// 기본적인 정렬 알고리즘
// Bubble Sort 
// 시간복잡도 O(n^2)

public class code27 {
  public static void bubbleSort(int[] arr, int n) {

    for (int i = 0; i < n - 1; i++) {
      for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          // 두 원소의 위치를 바꿈
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }

  public static void main(String[] args) {
    int[] arr = { 64, 25, 12, 22, 11 };
    System.out.println("Original Array:");
    printArray(arr);

    bubbleSort(arr, arr.length);

    System.out.println("Sorted Array:");
    printArray(arr);
  }

  public static void printArray(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }
}
