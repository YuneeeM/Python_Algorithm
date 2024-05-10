package INF.may;

// study on 05/10/24

// 힙정렬 - recursive 버전

public class code32 {
  // 주어진 배열에서 특정 위치의 노드를 Max-Heapify하는 함수
  // 인덱스 i에 있는 노드를 기준으로 왼쪽 서브트리와 오른쪽 서브트리가 모두 Max-Heap 속성을 갖도록 조정함
  // 전체 배열이 Max-Heap 속성을 유지하도록 함
  public static void maxHeapify(int[] arr, int i, int heapSize) {
    int left = 2 * i + 1; // 왼쪽 자식 노드의 인덱스
    int right = 2 * i + 2; // 오른쪽 자식 노드의 인덱스
    int largest = i; // 현재 노드, 왼쪽 자식, 오른쪽 자식 중 가장 큰 값을 가지는 노드의 인덱스

    // 왼쪽 자식과 비교하여 최대값 갱신
    if (left < heapSize && arr[left] > arr[largest])
      largest = left;

    // 오른쪽 자식과 비교하여 최대값 갱신
    if (right < heapSize && arr[right] > arr[largest])
      largest = right;

    // 현재 노드의 값이 자식 노드보다 크지 않으면, 자리를 바꿔야 함
    if (largest != i) {
      // 최대값을 가진 자식과 현재 노드의 값을 교환
      int temp = arr[i];
      arr[i] = arr[largest];
      arr[largest] = temp;

      // 교환한 자식 노드를 기준으로 다시 Max-Heapify 호출
      maxHeapify(arr, largest, heapSize);
    }
  }

  public static void main(String[] args) {
    int[] arr = { 4, 10, 3, 5, 1, 2 };
    int heapSize = arr.length;

    System.out.println("Original array:");
    printArray(arr);

    // 배열을 Max-Heap으로 만들기 위해 반복문을 통해 Max-Heapify 호출
    for (int i = (heapSize / 2) - 1; i >= 0; i--) {
      maxHeapify(arr, i, heapSize);
    }

    System.out.println("\nArray after Max-Heapify:");
    printArray(arr);
  }

  // 배열 출력을 위한 유틸리티 함수
  public static void printArray(int[] arr) {
    for (int num : arr) {
      System.out.print(num + " ");
    }
    System.out.println();
  }
}
