package INF.may;

// study on 05/09/24

// 힙정렬

public class code31 {
  private int[] heap;
  private int size;
  private int capacity;

  public code31(int capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.heap = new int[capacity];
  }

  private int parent(int i) {
    return (i - 1) / 2;
  }

  private int leftChild(int i) {
    return 2 * i + 1;
  }

  private int rightChild(int i) {
    return 2 * i + 2;
  }

  private void swap(int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
  }

  private void heapifyUp(int i) {
    while (i > 0 && heap[i] > heap[parent(i)]) {
      swap(i, parent(i));
      i = parent(i);
    }
  }

  private void heapifyDown(int i) {
    int maxIndex = i;
    int left = leftChild(i);
    int right = rightChild(i);

    if (left < size && heap[left] > heap[maxIndex]) {
      maxIndex = left;
    }

    if (right < size && heap[right] > heap[maxIndex]) {
      maxIndex = right;
    }

    if (i != maxIndex) {
      swap(i, maxIndex);
      heapifyDown(maxIndex);
    }
  }

  public void insert(int value) {
    if (size >= capacity) {
      System.out.println("Heap is full!");
      return;
    }

    heap[size] = value;
    heapifyUp(size);
    size++;
  }

  public int extractMax() {
    if (size <= 0) {
      throw new IllegalStateException("Heap is empty!");
    }

    int max = heap[0];
    heap[0] = heap[size - 1];
    size--;
    heapifyDown(0);
    return max;
  }

  public void printHeap() {
    for (int i = 0; i < size; i++) {
      System.out.print(heap[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    code31 maxHeap = new code31(10);
    maxHeap.insert(10);
    maxHeap.insert(20);
    maxHeap.insert(15);
    maxHeap.insert(30);
    maxHeap.insert(25);
    maxHeap.insert(40);

    System.out.println("Max Heap:");
    maxHeap.printHeap();

    System.out.println("Extract Max: " + maxHeap.extractMax());
    System.out.println("Max Heap after extraction:");
    maxHeap.printHeap();
  }
}