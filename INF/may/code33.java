package INF.may;

import java.util.Arrays;

// study on 05/13/24

// 힙정렬 - extract max (우선순위)

public class code33 {
  private int[] heap;
  private int size;
  private int capacity;

  public code33(int capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.heap = new int[capacity];
  }

  // 부모 노드 인덱스를 반환하는 함수
  private int parent(int i) {
    return (i - 1) / 2;
  }

  // 왼쪽 자식 노드 인덱스를 반환하는 함수
  private int leftChild(int i) {
    return 2 * i + 1;
  }

  // 오른쪽 자식 노드 인덱스를 반환하는 함수
  private int rightChild(int i) {
    return 2 * i + 2;
  }

  // 최대 힙 속성을 유지하기 위해 요소를 상향식으로 재배치하는 함수
  private void heapifyUp(int i) {
    while (i > 0 && heap[parent(i)] < heap[i]) {
      // 부모 노드와 자식 노드를 교환
      int temp = heap[parent(i)];
      heap[parent(i)] = heap[i];
      heap[i] = temp;

      // 현재 노드 인덱스를 부모 노드 인덱스로 변경
      i = parent(i);
    }
  }

  // 새로운 요소를 힙에 추가하는 함수
  public void insert(int key) {
    if (size == capacity) {
      System.out.println("Heap is full. Cannot insert more elements.");
      return;
    }

    // 새로운 요소를 힙의 맨 끝에 추가
    size++;
    int i = size - 1;
    heap[i] = key;

    // 최대 힙 속성을 유지하기 위해 상향식으로 재배치
    heapifyUp(i);
  }

  // 최대값을 추출하고 삭제하는 함수
  public int extractMax() {
    if (size <= 0)
      return Integer.MIN_VALUE;
    if (size == 1) {
      size--;
      return heap[0];
    }

    // 최대값은 항상 힙의 루트 노드에 위치
    int maxVal = heap[0];

    // 힙의 마지막 노드를 루트 노드로 복사
    heap[0] = heap[size - 1];
    size--;

    // 최대 힙 속성을 유지하기 위해 하향식으로 재배치
    maxHeapify(0);

    return maxVal;
  }

  // 최대 힙 속성을 유지하기 위해 요소를 하향식으로 재배치하는 함수
  private void maxHeapify(int i) {
    int left = leftChild(i);
    int right = rightChild(i);
    int largest = i;

    // 왼쪽 자식과 비교하여 최대값을 찾음
    if (left < size && heap[left] > heap[largest])
      largest = left;

    // 오른쪽 자식과 비교하여 최대값을 찾음
    if (right < size && heap[right] > heap[largest])
      largest = right;

    // 최대값이 자기 자신이 아니라면 자식 노드와 교환 후 재귀 호출
    if (largest != i) {
      int temp = heap[i];
      heap[i] = heap[largest];
      heap[largest] = temp;
      maxHeapify(largest);
    }
  }

  // 현재 힙의 상태를 문자열로 반환하는 함수 (디버깅용)
  public String toString() {
    return Arrays.toString(heap);
  }

  public static void main(String[] args) {
    code33 pq = new code33(10);
    pq.insert(3);
    pq.insert(2);
    pq.insert(15);
    System.out.println(pq.toString()); // [15, 3, 2]
    System.out.println("Extracted max: " + pq.extractMax()); // 15
    System.out.println(pq.toString()); // [3, 2]
  }
}