package INF.april;

// study on 04/29/24

// Recursion의 응용 : 미로찾기
// Maze 미로찾기 - Decision Problem (답이 yes or no)

/*
 * 현재 위치에서 출구까지 가는 경로가 있으려면
 * 1) 현재 위치가 출구이거나 혹은
 * 2) 이웃한 셀들 중 하나에서 현재 위치를 
 * 지나지 않고 출구까지 가는 경로가 있거나
 */

public class code22 {

  private static int N = 8;
  private static int[][] maze = {
      { 0, 0, 0, 0, 0, 0, 0, 1 },
      { 0, 1, 1, 0, 1, 1, 0, 1 },
      { 0, 0, 0, 1, 0, 0, 0, 1 },
      { 0, 1, 0, 0, 1, 1, 0, 0 },
      { 0, 1, 1, 1, 0, 0, 1, 1 },
      { 0, 1, 0, 0, 0, 1, 0, 1 },
      { 0, 0, 0, 1, 0, 0, 0, 1 },
      { 0, 1, 1, 1, 0, 1, 0, 0 }
  };

  private static final int PATHWAY_COLOR = 0; // white
  private static final int WALL_COLOR = 1; // blue

  // visited이며 출구까지의 경로상에 있지 않음이 밝혀진 cell
  private static final int BLOCKED_COLOR = 2; // red

  // visited이며 아직 출구로 가능 경로가 될 가능성이 있는 cell
  private static final int PATH_COLOR = 3; // orange

  public static boolean findMazePath(int x, int y) {
    if (x < 0 || y < 0 || x >= N || y >= N) {
      return false;
    } else if (maze[x][y] != PATHWAY_COLOR) {
      return false;
    } else if (x == N - 1 && y == N - 1) {
      maze[x][y] = PATH_COLOR;
      return true;
    } else {
      maze[x][y] = PATH_COLOR;
      if (findMazePath(x - 1, y) || findMazePath(x, y + 1)
          || findMazePath(x + 1, y) || findMazePath(x, y - 1)) {
        return true;
      }
      maze[x][y] = BLOCKED_COLOR; // dead end
      return false;
    }
  }

  public static void printMaze() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        switch (maze[i][j]) {
          case PATHWAY_COLOR:
            System.out.print("0 "); // white
            break;
          case WALL_COLOR:
            System.out.print("1 "); // blue
            break;
          case BLOCKED_COLOR:
            System.out.print("x "); // red
            break;
          case PATH_COLOR:
            System.out.print("* "); // orange
            break;
        }
      }
      System.out.println();
    }
    System.out.println();
  }

  public static void main(String[] args) {
    printMaze();
    findMazePath(0, 0);
    printMaze();
  }

}
