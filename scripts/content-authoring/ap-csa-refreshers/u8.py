from common import code, finish

finish(8, [
("2d-array-creation", r"""
### The idea
A 2D array is an array whose elements are themselves arrays, which is how Java stores a grid, a table or a board. The first index picks a row and the second picks a column.

### Key facts
- Create one with the rows first: `int[][] grid = new int[3][4];` is `3` rows and `4` columns.
- Or list the values: `int[][] small = {{1, 2}, {3, 4}, {5, 6}};` (each inner pair of braces is one row).
- Access one element with `grid[row][col]`. Both indexes start at `0`.
- `grid.length` is the number of **rows**. `grid[0].length` is the number of **columns** (the length of one row).
- Elements start with the same default values as a 1D array: `0`, `0.0`, `false` or `null`.
- Each row is its own array, so in principle rows can have different lengths.

### Watch out for
Swapping the indexes. `grid[2][1]` is row `2`, column `1`. Mixing up row and column is the most common 2D mistake, so say it out loud as "row, then column".

### Worked example
""" + code('''
int[][] grid = new int[3][4];
grid[1][2] = 9;
int[][] small = {{1, 2}, {3, 4}, {5, 6}};
System.out.println(grid.length + " " + grid[0].length + " " + grid[1][2]);
System.out.println(small.length + " " + small[2][1]);
''', out="3 4 9\n3 6") + r"""

`grid` has `3` rows and `4` columns, and `grid[1][2]` is the `9` we set. It prints `3 4 9`. For `small`, there are `3` rows, and `small[2][1]` is the second value in the third row, which is `6`. It prints `3 6`.
"""),
("traversing-2d-arrays", r"""
### The idea
To visit every element of a 2D array, you nest two loops: one over the rows and one over the columns. The order of the loops decides how you move through the grid.

### Key facts
- **Row by row** (row-major): outer loop over rows with `r < grid.length`, inner loop over columns with `c < grid[r].length`.
- **Column by column**: swap the loops. The outer loop goes over `c < grid[0].length`, and the inner loop goes over `r < grid.length`.
- A row total is computed inside the inner loop and reset to `0` at the start of each row, in the outer loop.
- The main diagonal is the elements where `r == c`. You can use one loop for it, or test the condition inside the nested loops.
- An enhanced `for` works too: `for (int[] row : grid)` for each row, then `for (int v : row)` for each value.
- Use `grid[r].length` for the inner limit. It is safe even if rows have different lengths.

### Watch out for
Not resetting the total. If `rowSum = 0;` is declared outside the row loop, each row's sum keeps adding to the previous rows.

### Worked example
""" + code('''
int[][] m = {{1, 2, 3}, {4, 5, 6}};
for (int r = 0; r < m.length; r++) {
    int rowSum = 0;
    for (int c = 0; c < m[r].length; c++) {
        rowSum += m[r][c];
    }
    System.out.print(rowSum + " ");
}
System.out.println();
for (int c = 0; c < m[0].length; c++) {
    int colSum = 0;
    for (int r = 0; r < m.length; r++) {
        colSum += m[r][c];
    }
    System.out.print(colSum + " ");
}
''', out="6 15 \n5 7 9") + r"""

The row sums are `1 + 2 + 3 = 6` and `4 + 5 + 6 = 15`, so the first line is `6 15`. The column sums are `1 + 4 = 5`, `2 + 5 = 7` and `3 + 6 = 9`, so the second line is `5 7 9`.
"""),
])
