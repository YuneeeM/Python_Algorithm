package INF.may;

// study on 05/03/24

// 기본적인 정렬 알고리즘
// Insertion Sort 
// 시간복잡도 O(n^2)

public class code28 {
  public static void insertionSort(int arr[], int n) {

    for (int i = 1; i < n; ++i) {
      int key = arr[i];
      int j = i - 1;

      /* key보다 큰 원소는 key보다 오른쪽으로 한 칸씩 이동 */
      while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j = j - 1;
      }
      arr[j + 1] = key;
    }

  }

  public static void main(String[] args) {
    int[] arr = { 64, 25, 12, 22, 11 };
    System.out.println("Original Array:");
    printArray(arr);

    insertionSort(arr, arr.length);

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
