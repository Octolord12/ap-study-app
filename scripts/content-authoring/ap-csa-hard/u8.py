from common import *

B = bank(8, "unit-8-2d-array")
T_CRE, T_TRA = ("2d-array-creation", "traversing-2d-arrays")
Q = "What is printed as a result of executing the following code segment?"
G = "int[][] g = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n"

trace(B, T_CRE, Q, body="int[][] g = new int[3][4];\ng[1][2] = 7;\ng[2][3] = g[1][2] + 1;\nSystem.out.println(g.length + \" \" + g[0].length + \" \" + g[1][2] + \" \" + g[2][3] + \" \" + g[0][0]);",
      manual=[("4 3 7 8 0", "`g.length` is the number of rows (3) and `g[0].length` is the number of columns (4). `new int[3][4]` makes 3 rows of 4 elements."),
              ("3 4 7 7 0", "`g[2][3]` is set to `g[1][2] + 1`, which is 8."),
              ("3 3 7 8 0", "`g[0].length` is the length of a row, which is the number of columns, 4.")],
      correct_expl="`new int[3][4]` creates 3 rows with 4 columns each, so `g.length` is 3 and `g[0].length` is 4. `g[1][2]` is 7 and `g[2][3]` is 8. The untouched element `g[0][0]` is 0.",
      explanation="A 2D array is an array of rows: `g.length` counts rows, and `g[r].length` counts the columns in row `r`.")

trace(B, T_TRA, Q, body=G + "int sum = 0;\nfor (int r = 0; r < g.length; r++)\n    for (int c = 0; c < g[r].length; c++)\n        if ((r + c) % 2 == 0)\n            sum += g[r][c] * (r + 1);\nSystem.out.println(sum);",
      mutants=[("(r + c) % 2 == 0", "(r + c) % 2 == 1", "This sums the cells where r + c is odd. The code adds the cells where r + c is even: (0,0), (0,2), (1,1), (2,0) and (2,2)."),
               ("* (r + 1)", "* (c + 1)", "This weights each element by its column number. The weight in the code is the row number plus 1.")],
      manual=[("25", "This leaves out the weights. Each element is multiplied by (r + 1): 1*1 + 3*1 + 5*2 + 7*3 + 9*3.")],
      correct_expl="The cells with r + c even are g[0][0]=1, g[0][2]=3, g[1][1]=5, g[2][0]=7 and g[2][2]=9. With weights r + 1: 1(1) + 3(1) + 5(2) + 7(3) + 9(3) = 1 + 3 + 10 + 21 + 27 = 62.",
      explanation="Evaluate the condition for each (row, column) pair and apply the weight that depends on the row.")

trace(B, T_TRA, Q, body=G + "String s = \"\";\nfor (int c = 0; c < g[0].length; c++) {\n    for (int r = g.length - 1; r >= 0; r--)\n        s += g[r][c];\n    s += \"|\";\n}\nSystem.out.println(s);",
      mutants=[("int r = g.length - 1; r >= 0; r--", "int r = 0; r < g.length; r++", "This reads each column from top to bottom. The inner loop starts at the last row and moves up."),
               ("g[r][c]", "g[c][r]", "This swaps the roles of the row and column indexes, so each group reads a row (backward) instead of a column.")],
      manual=[("123|456|789|", "This reads the grid row by row. The outer loop here is over the columns, so each group is one column, read from the bottom up.")],
      correct_expl="The outer loop chooses a column (0, 1, 2). The inner loop reads that column from the bottom row up: column 0 gives 7, 4, 1; column 1 gives 8, 5, 2; column 2 gives 9, 6, 3.",
      explanation="In column-major traversal the outer loop is over columns and the inner loop is over rows.")

trace(B, T_TRA, Q, body="int[][] m = new int[4][4];\nfor (int r = 0; r < 4; r++)\n    for (int c = 0; c < 4; c++)\n        m[r][c] = r + 2 * c + r * c;\nint d1 = 0, d2 = 0;\nfor (int i = 0; i < 4; i++) {\n    d1 += m[i][i];\n    d2 += m[i][3 - i];\n}\nSystem.out.println(d1 + \" \" + d2);",
      mutants=[("m[i][3 - i]", "m[i][i]", "This adds the main diagonal twice. The second sum uses the anti-diagonal, `m[i][3 - i]`.")],
      manual=[("22 32", "This swaps the two sums. `d1` is the main diagonal (m[0][0], m[1][1], ...), which is 0 + 4 + 10 + 18 = 32, and `d2` is the anti-diagonal, 6 + 7 + 6 + 3 = 22."),
              ("32 26", "The anti-diagonal elements are m[0][3] = 6, m[1][2] = 7, m[2][1] = 6 and m[3][0] = 3, which sum to 22.")],
      correct_expl="The array holds r + 2c + rc. The main diagonal is 0, 4, 10, 18 (sum 32). The anti-diagonal elements m[i][3 - i] are 6, 7, 6, 3 (sum 22).",
      explanation="The main diagonal has `col == row`; the anti-diagonal of an n-by-n array has `col == n - 1 - row`.")

trace(B, T_CRE, Q, body="int[][] j = new int[3][];\nfor (int i = 0; i < j.length; i++)\n    j[i] = new int[i + 1];\nj[2][1] = 5;\nint total = 0;\nfor (int[] row : j)\n    total += row.length;\nSystem.out.println(total + \" \" + j[0].length + \" \" + j[2].length + \" \" + j[2][1]);",
      manual=[("9 3 3 5", "This assumes a rectangular array. The rows were created with lengths 1, 2 and 3, so `j[0].length` is 1 and the total is 6."),
              ("6 1 3 0", "`j[2][1] = 5` sets an element of row 2 (valid, because row 2 has 3 elements), so it prints 5."),
              ("6 3 1 5", "Row `i` has length `i + 1`, so `j[0].length` is 1 and `j[2].length` is 3.")],
      correct_expl="Row `i` is created with `i + 1` elements: lengths 1, 2 and 3 (total 6). `j[0].length` is 1, `j[2].length` is 3, and `j[2][1]` was set to 5.",
      explanation="In a 2D array, each row is its own array and may have a different length.")

trace(B, T_TRA, Q, body="int[][] g = {{4, 1, 7}, {2, 9}, {5, 5, 5, 1}};\nint best = -1, bestSum = -1;\nfor (int r = 0; r < g.length; r++) {\n    int s = 0;\n    for (int x : g[r])\n        s += x;\n    if (s > bestSum) {\n        bestSum = s;\n        best = r;\n    }\n}\nSystem.out.println(best + \" \" + bestSum);",
      manual=[("0 12", "This keeps the first row. Row 0 sums to 12, but row 2 sums to 5 + 5 + 5 + 1 = 16, which is larger."),
              ("1 11", "Row 1 ({2, 9}) sums to 11, which is less than 16."),
              ("2 21", "This adds elements that do not exist. Row 2 has four elements, summing to 16, and the array is not rectangular.")],
      correct_expl="The row sums are 12, 11 and 16. The row with the largest sum is row 2, with 16.",
      explanation="Each row can have a different length, so use `g[r].length` (or an enhanced `for` over the row) rather than a fixed number of columns.")

trace(B, T_TRA, Q, body=G + "for (int r = 0; r < 3; r++)\n    for (int c = 0; c < 3; c++) {\n        int t = g[r][c];\n        g[r][c] = g[c][r];\n        g[c][r] = t;\n    }\nSystem.out.println(g[0][1] + \" \" + g[1][0] + \" \" + g[0][2] + \" \" + g[2][0]);",
      mutants=[("int c = 0; c < 3; c++", "int c = r + 1; c < 3; c++", "This transposes the array by swapping each pair only once (for c > r). The code visits every pair twice, which swaps each pair back.")],
      manual=[("4 2 3 7", "The loops visit every (r, c) pair, so each pair is swapped twice and nothing changes; g[0][2] and g[2][0] are not changed either."),
              ("2 4 7 3", "The elements g[0][2] and g[2][0] are also swapped twice, so they keep their original values 3 and 7.")],
      correct_expl="Each off-diagonal pair is swapped twice: once as (r, c) and once as (c, r). The array ends in its original order, so g[0][1] is 2, g[1][0] is 4, g[0][2] is 3 and g[2][0] is 7.",
      explanation="To transpose in place, swap only the pairs above the diagonal (for example, `c > r`).")

trace(B, T_CRE, Q, body="int[][] g = new int[2][2];\nint[] row = g[0];\nrow[1] = 5;\ng[1] = row;\ng[1][0] = 9;\nint[][] h = new int[2][];\nh[0] = g[0];\nh[1] = new int[] {g[0][0], g[0][1]};\nh[1][1] = -1;\nSystem.out.println(g[0][0] + \" \" + g[0][1] + \" \" + g[1][1] + \" \" + h[0][0] + \" \" + h[1][1]);",
      manual=[("0 5 0 9 -1", "`g[1] = row` makes row 1 refer to the same array as row 0, so `g[1][0] = 9` also changes `g[0][0]` and `g[1][1]` is 5."),
              ("9 5 5 0 -1", "`h[0] = g[0]` makes `h`'s first row the same array as `g`'s first row, so `h[0][0]` is 9."),
              ("9 5 5 9 5", "`h[1]` is a *new* array (a copy of the values), so `h[1][1] = -1` does not change `g`, and `h[1][1]` is -1.")],
      correct_expl="`row` is `g[0]`. After `row[1] = 5` and `g[1] = row`, rows 0 and 1 of `g` are the same array, so `g[1][0] = 9` makes `g[0][0]` 9 as well, and `g[1][1]` is 5. `h[0]` also refers to that array (9). `h[1]` is a separate array whose second element is set to -1.",
      explanation="A row of a 2D array is a reference to an array; assigning rows makes them share the same data.")

trace(B, T_CRE, Q, body="int[][] g = new int[2][3];\nString out = \"\";\nint[][] pairs = {{1, 2}, {2, 0}, {0, 3}, {1, 3}};\nfor (int[] p : pairs) {\n    try {\n        g[p[0]][p[1]] = 1;\n        out += \"ok \";\n    } catch (ArrayIndexOutOfBoundsException e) {\n        out += \"bad \";\n    }\n}\nSystem.out.println(out.trim());",
      manual=[("ok ok bad bad", "`g` has only 2 rows (indexes 0 and 1), so `g[2][0]` is out of bounds."),
              ("ok bad ok bad", "`g[0][3]` is out of bounds: each row has 3 elements (indexes 0 through 2)."),
              ("ok bad bad ok", "`g[1][3]` is out of bounds because column 3 does not exist in a row of length 3.")],
      correct_expl="The array has 2 rows (indexes 0, 1) and 3 columns (0, 1, 2). `g[1][2]` is valid; `g[2][0]` has a bad row index; `g[0][3]` and `g[1][3]` have a bad column index.",
      explanation="Check the row index against `g.length` and the column index against `g[r].length`.")

trace(B, T_TRA, Q, body="int[][] g = {{5, 2, 9}, {1, 6, 3}, {8, 4, 7}};\nint r = 1, c = 1, greater = 0;\nfor (int dr = -1; dr <= 1; dr++)\n    for (int dc = -1; dc <= 1; dc++) {\n        if (dr == 0 && dc == 0) continue;\n        int nr = r + dr, nc = c + dc;\n        if (nr >= 0 && nr < g.length && nc >= 0 && nc < g[0].length && g[nr][nc] > g[r][c])\n            greater++;\n    }\nSystem.out.println(greater);",
      mutants=[("int r = 1, c = 1", "int r = 0, c = 0", "This looks at the corner cell (value 5), which has only three neighbors; the code examines the center cell, value 6.")],
      manual=[("5", "This counts the neighbors that are *smaller* than 6 (5, 2, 1, 3, 4). The condition is `g[nr][nc] > g[r][c]`, which counts the larger ones."),
              ("8", "This counts all eight neighbors. Only the ones greater than the center value 6 are counted.")],
      correct_expl="The center cell holds 6. Its eight neighbors are 5, 2, 9, 1, 3, 8, 4, 7. Those greater than 6 are 9, 8 and 7, so `greater` is 3.",
      explanation="Examine each neighbor, and check that its row and column are inside the array before reading it.")

trace(B, T_CRE, Q, body="int[][] g = new int[3][4];\nfor (int r = 0; r < g.length; r++)\n    for (int c = 0; c < g[r].length; c++)\n        g[r][c] = (r * c) % 3;\nfor (int[] row : g) {\n    String s = \"\";\n    for (int x : row)\n        s += x;\n    System.out.println(s);\n}",
      mutants=[("(r * c) % 3", "(r + c) % 3", "This fills each cell with `(r + c) % 3`. The code uses the product `r * c`, so the first row and first column are all 0.")],
      manual=[("0000\n0123\n0246", "This leaves out the `% 3`. The values are r * c reduced modulo 3, so 3 becomes 0, 4 becomes 1 and 6 becomes 0."),
              ("0000\n0120\n0120", "In row 2, the products are 0, 2, 4, 6, which modulo 3 are 0, 2, 1, 0.")],
      correct_expl="Row 0 is all 0 (0 * c). Row 1 is c % 3: 0 1 2 0. Row 2 is 2c % 3: 0 2 1 0.",
      explanation="Compute each cell from its row and column index. The first loop fills the array; the second prints it row by row.")

trace(B, T_TRA, Q, body="int[][] g = {{3, 8, 1}, {8, 2, 9}, {4, 8, 6}};\nint rr = -1, cc = -1;\nfor (int r = 0; r < 3 && rr == -1; r++)\n    for (int c = 0; c < 3; c++)\n        if (g[r][c] == 8 && rr == -1) {\n            rr = r;\n            cc = c;\n        }\nint r2 = -1, c2 = -1;\nfor (int c = 0; c < 3 && c2 == -1; c++)\n    for (int r = 0; r < 3; r++)\n        if (g[r][c] == 8 && c2 == -1) {\n            r2 = r;\n            c2 = c;\n        }\nSystem.out.println(rr + \",\" + cc + \" \" + r2 + \",\" + c2);",
      manual=[("0,1 0,1", "The second search goes column by column. Column 0 is checked first, and the first 8 in column 0 is at row 1."),
              ("1,0 0,1", "This swaps the two results. Row-major order finds the 8 at (0, 1) first; column-major order finds the 8 at (1, 0) first."),
              ("0,1 2,1", "Column 0 contains an 8 (at row 1), so the column-major search stops there, before reaching column 1.")],
      correct_expl="Row by row, the first 8 is at row 0, column 1. Column by column, column 0 contains 3, 8, 4, so the first 8 found is at row 1, column 0.",
      explanation="The first match depends on the traversal order: row-major and column-major can find different elements first.")

trace(B, T_CRE, Q, body="int[][] a = new int[3][];\nString out = \"\";\ntry {\n    a[0][0] = 1;\n    out += \"A\";\n} catch (NullPointerException e) {\n    out += \"N\";\n}\na[1] = new int[2];\ntry {\n    a[1][2] = 1;\n    out += \"B\";\n} catch (ArrayIndexOutOfBoundsException e) {\n    out += \"I\";\n}\nSystem.out.println(out + a.length + a[1].length);",
      manual=[("AB32", "`new int[3][]` creates only the outer array; the rows are `null`, so `a[0][0] = 1` throws a `NullPointerException`. And `a[1]` has only 2 elements, so `a[1][2]` is out of bounds."),
              ("NB32", "Row 1 has 2 elements (indexes 0 and 1), so `a[1][2]` is out of bounds and throws `ArrayIndexOutOfBoundsException`."),
              ("AI32", "`a[0]` is `null`: `new int[3][]` leaves the rows unassigned, so `a[0][0] = 1` throws a `NullPointerException`.")],
      correct_expl="`new int[3][]` creates 3 `null` rows, so `a[0][0] = 1` throws `NullPointerException` (N). After `a[1] = new int[2]`, `a[1][2]` is out of bounds (I). Then `a.length` is 3 and `a[1].length` is 2.",
      explanation="With `new int[3][]`, only the outer array exists. Each row must be created before its elements can be used.")

trace(B, T_CRE, Q, body="int[][] g = {{1, 2}, {3, 4}, {5, 6}};\nint[] t = g[0];\ng[0] = g[2];\ng[2] = t;\nint[] row = g[1];\nfor (int c = 0; c < 2; c++) {\n    int tmp = g[0][c];\n    g[0][c] = row[c];\n    row[c] = tmp;\n}\nSystem.out.println(g[0][0] + \" \" + g[1][0] + \" \" + g[2][0] + \" \" + g[0][1]);",
      manual=[("5 3 1 6", "This ignores the loop. The row swap alone gives g = {{5, 6}, {3, 4}, {1, 2}}, but the loop then swaps the *contents* of row 0 and row 1."),
              ("1 3 5 2", "This is the original array. Rows 0 and 2 are exchanged first, and then the contents of rows 0 and 1 are exchanged, so the array does change."),
              ("3 5 1 6", "The loop swaps both columns, not only the first: after the loop, row 0 is {3, 4}, so `g[0][1]` is 4.")],
      correct_expl="The first swap exchanges the row references of rows 0 and 2: {{5, 6}, {3, 4}, {1, 2}}. The loop then swaps the contents of row 0 and row 1: row 0 is {3, 4} and row 1 is {5, 6}. So g[0][0] = 3, g[1][0] = 5, g[2][0] = 1 and g[0][1] = 4.",
      explanation="Swapping two row references exchanges whole rows; swapping element by element exchanges their contents.")

trace(B, T_TRA, Q, body="int[][] g = {{1, 2, 3}, {4, 5, 6}};\nint[] cs = new int[g[0].length];\nfor (int r = 0; r < g.length; r++)\n    for (int c = 0; c < g[r].length; c++)\n        cs[c] += g[r][c] * (r + 1);\nSystem.out.println(cs[0] + \" \" + cs[1] + \" \" + cs[2]);",
      mutants=[("cs[c] += g[r][c] * (r + 1);", "cs[r] += g[r][c] * (r + 1);", "This accumulates into `cs[r]`, so the totals are per row rather than per column.")],
      manual=[("5 7 9", "This leaves out the weight (r + 1). Row 1's values are multiplied by 2: column 0 is 1 + 4 * 2 = 9."),
              ("4 5 6", "The weight is r + 1 (1 for row 0 and 2 for row 1), not r. Column 0 is 1 * 1 + 4 * 2 = 9.")],
      correct_expl="Column 0 is 1(1) + 4(2) = 9, column 1 is 2(1) + 5(2) = 12, and column 2 is 3(1) + 6(2) = 15.",
      explanation="A column total accumulates one element from every row, so the index of the totals array is the column.")

# ------------------------------------------------------------------ FRQs
grid = '''
class Grid {
    private int[][] cells;
    public Grid(int[][] c) { cells = c; }

    public int rowSum(int r) {
        int sum = 0;
        for (int value : cells[r]) {
            sum += value;
        }
        return sum;
    }

    public int largestRow() {
        int best = 0;
        for (int r = 1; r < cells.length; r++) {
            if (rowSum(r) > rowSum(best)) {
                best = r;
            }
        }
        return best;
    }

    public int[] columnSums() {
        int[] sums = new int[cells[0].length];
        for (int r = 0; r < cells.length; r++) {
            for (int c = 0; c < cells[r].length; c++) {
                sums[c] += cells[r][c];
            }
        }
        return sums;
    }
}
'''
gb = 'Grid g = new Grid(new int[][] {{4, 1, 7}, {2, 9, 0}, {5, 5, 5}, {1, 1, 1}});\nSystem.out.println(g.rowSum(1));\nSystem.out.println(g.largestRow());\nint[] cs = g.columnSums();\nSystem.out.println(cs[0] + " " + cs[1] + " " + cs[2]);\nGrid h = new Grid(new int[][] {{3, 3}, {3, 3}});\nSystem.out.println(h.largestRow());'
assert run(program(gb, classes=grid)) == "11\n2\n12 16 13\n0", run(program(gb, classes=grid))
B.frq(T_TRA,
      "A `Grid` object stores a rectangular array of integers in a two-dimensional array instance variable named `cells`. The array has at least one row and at least one column.\n\n```java\npublic class Grid {\n    private int[][] cells;\n\n    /** Returns the sum of the values in row r of cells. Precondition: 0 <= r < cells.length */\n    public int rowSum(int r)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the index of the row of cells with the greatest row sum. If more than one row\n     *  has the greatest sum, returns the smallest such index.\n     *  Precondition: cells has at least one row */\n    public int largestRow()\n    { /* to be implemented in part (b) */ }\n\n    /** Returns a new array in which element c is the sum of the values in column c of cells. */\n    public int[] columnSums()\n    { /* to be implemented in part (c) */ }\n}\n```\n\n**(a)** Write the method `rowSum`.\n\n**(b)** Write the method `largestRow`, using `rowSum` as appropriate.\n\n**(c)** Write the method `columnSums`. For example, if `cells` is {{4, 1, 7}, {2, 9, 0}, {5, 5, 5}, {1, 1, 1}}, then `columnSums` returns {12, 16, 13}.",
      [(1, "(a) Traverses the elements of the given row and accumulates the sum"),
       (1, "(a) Returns the correct sum"),
       (1, "(b) Calls `rowSum` for the rows and compares the sums"),
       (1, "(b) Tracks the index (not the sum) of the greatest row and uses a strict comparison so that ties keep the smaller index"),
       (1, "(b) Returns the correct row index"),
       (1, "(c) Creates a new array whose length is the number of columns"),
       (1, "(c) Traverses all elements and adds each one to the correct column total, then returns the array")],
      "```java\npublic int rowSum(int r) {\n    int sum = 0;\n    for (int value : cells[r]) {\n        sum += value;\n    }\n    return sum;\n}\n\npublic int largestRow() {\n    int best = 0;\n    for (int r = 1; r < cells.length; r++) {\n        if (rowSum(r) > rowSum(best)) {\n            best = r;\n        }\n    }\n    return best;\n}\n\npublic int[] columnSums() {\n    int[] sums = new int[cells[0].length];\n    for (int r = 0; r < cells.length; r++) {\n        for (int c = 0; c < cells[r].length; c++) {\n            sums[c] += cells[r][c];\n        }\n    }\n    return sums;\n}\n```\nIn `largestRow`, the strict `>` means that a later row with an equal sum does not replace the earlier one, which gives the smallest index for ties.")

board = '''
class Board {
    private int[][] spots;
    public Board(int[][] s) { spots = s; }

    public boolean hasFullRow(int player) {
        for (int r = 0; r < spots.length; r++) {
            boolean full = true;
            for (int c = 0; c < spots[r].length; c++) {
                if (spots[r][c] != player) {
                    full = false;
                }
            }
            if (full) {
                return true;
            }
        }
        return false;
    }

    public int countNeighbors(int row, int col, int player) {
        int count = 0;
        for (int r = row - 1; r <= row + 1; r++) {
            for (int c = col - 1; c <= col + 1; c++) {
                if (r >= 0 && r < spots.length && c >= 0 && c < spots[0].length
                        && !(r == row && c == col) && spots[r][c] == player) {
                    count++;
                }
            }
        }
        return count;
    }
}
'''
bb = 'Board b = new Board(new int[][] {{1, 2, 1}, {1, 1, 1}, {2, 1, 0}});\nSystem.out.println(b.hasFullRow(1));\nSystem.out.println(b.hasFullRow(2));\nSystem.out.println(b.countNeighbors(1, 1, 1));\nSystem.out.println(b.countNeighbors(0, 0, 1));\nSystem.out.println(b.countNeighbors(2, 2, 1));\nSystem.out.println(b.countNeighbors(2, 2, 0));'
assert run(program(bb, classes=board)) == "true\nfalse\n5\n2\n3\n0", run(program(bb, classes=board))
B.frq(T_TRA,
      "A `Board` object stores the contents of a rectangular game board in a two-dimensional `int` array named `spots`. Each element is 0 for an empty spot or the number of the player (1 or 2) who occupies it.\n\n```java\npublic class Board {\n    private int[][] spots;\n\n    /** Returns true if every spot in at least one row of spots is occupied by player;\n     *  otherwise returns false. */\n    public boolean hasFullRow(int player)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the number of spots adjacent to the spot at (row, col), including diagonal\n     *  neighbors, that are occupied by player. The spot (row, col) itself is not counted.\n     *  Spots outside the board are not counted.\n     *  Precondition: (row, col) is a valid position in spots. */\n    public int countNeighbors(int row, int col, int player)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `hasFullRow`.\n\n**(b)** Write the method `countNeighbors`. For example, if `spots` is {{1, 2, 1}, {1, 1, 1}, {2, 1, 0}}, then `countNeighbors(1, 1, 1)` returns 5 and `countNeighbors(0, 0, 1)` returns 2.",
      [(1, "(a) Traverses the rows and, within each row, examines every element"),
       (1, "(a) Determines correctly whether all elements of a row equal `player`"),
       (1, "(a) Returns true as soon as a full row is found and false otherwise"),
       (1, "(b) Visits the (up to) eight positions around the spot"),
       (1, "(b) Excludes positions outside the array (checks both row and column bounds before accessing)"),
       (1, "(b) Excludes the spot itself and counts only spots equal to `player`, returning the count")],
      "```java\npublic boolean hasFullRow(int player) {\n    for (int r = 0; r < spots.length; r++) {\n        boolean full = true;\n        for (int c = 0; c < spots[r].length; c++) {\n            if (spots[r][c] != player) {\n                full = false;\n            }\n        }\n        if (full) {\n            return true;\n        }\n    }\n    return false;\n}\n\npublic int countNeighbors(int row, int col, int player) {\n    int count = 0;\n    for (int r = row - 1; r <= row + 1; r++) {\n        for (int c = col - 1; c <= col + 1; c++) {\n            if (r >= 0 && r < spots.length && c >= 0 && c < spots[0].length\n                    && !(r == row && c == col) && spots[r][c] == player) {\n                count++;\n            }\n        }\n    }\n    return count;\n}\n```\nThe bounds tests come first in the condition, so `spots[r][c]` is evaluated only for valid positions (short-circuit evaluation).")

B.save()
B.brief()
