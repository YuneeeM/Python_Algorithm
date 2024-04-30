package INF.april;

// study on 04/30/24

// Recursion의 응용
// Counting Cells in a Blob

public class code23 {

  private static int BACKGROUND_COLOR = 0;
  private static int IMAGE_COLOR = 1;
  private static int ALREADY_COUNTED = 2;
  private int[][] grid; // 그리드 배열을 클래스 내에 추가합니다.
  private int N; // 그리드 배열의 크기를 나타내는 변수를 추가합니다.

  public code23(int[][] grid) {
    this.grid = grid;
    this.N = grid.length;
  }

  public int countCells(int x, int y) {
    int result;
    if (x < 0 || x >= N || y < 0 || y >= N) {
      return 0;
    } else if (grid[x][y] != IMAGE_COLOR) {
      return 0;
    } else {
      grid[x][y] = ALREADY_COUNTED;
      return 1 + countCells(x - 1, y + 1) + countCells(x, y + 1)
          + countCells(x + 1, y + 1) + countCells(x - 1, y) + countCells(x + 1, y)
          + countCells(x - 1, y - 1) + countCells(x, y - 1) + countCells(x + 1, y - 1);
    }

  }

  public static void main(String[] args) {
    int[][] grid = {
        { 1, 0, 0, 0, 1 },
        { 0, 1, 1, 0, 0 },
        { 0, 0, 1, 1, 0 },
        { 0, 0, 0, 0, 0 },
        { 1, 1, 0, 0, 1 }
    };

    code23 counter = new code23(grid);

    int result = counter.countCells(2, 2);
    System.out.println("Number of cells: " + result);
  }
}
