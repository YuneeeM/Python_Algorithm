package INF.may;

// study on 05/03/24

// 기본적인 정렬 알고리즘
// Selection Sort 
// 시간복잡도 O(n^2)

public class code26 {
  public static void selectionSort(int[] arr, int n) {

    for (int i = n - 1; i > 0; i--) {
      int maxIndex = i;
      for (int j = 0; j < i; j++) {
        if (arr[j] > arr[maxIndex]) {
          maxIndex = j;
        }
      }
      // Swap arr[i] and arr[maxIndex]
      int temp = arr[i];
      arr[i] = arr[maxIndex];
      arr[maxIndex] = temp;
    }
  }

  public static void main(String[] args) {
    int[] arr = { 64, 25, 12, 22, 11 };
    System.out.println("Original Array:");
    printArray(arr);

    selectionSort(arr, arr.length);

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
