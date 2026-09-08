class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ch = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box].add(ch)

        def solve(i, j):

            if i == 9:
                return True

            if j == 9:
                return solve(i + 1, 0)

            if board[i][j] != ".":
                return solve(i, j + 1)

            box = (i // 3) * 3 + (j // 3)

            for ch in "123456789":

                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box]:

                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box].add(ch)

                    if solve(i, j + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[box].remove(ch)

            return False

        solve(0, 0)