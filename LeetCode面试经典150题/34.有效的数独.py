class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = set()
        col_has = set()
        box_has = set()

        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == '.':
                    continue
                if (i, x) in row_has or (j, x) in col_has or (i // 3, j // 3, x) in box_has:
                    return False
                row_has.add((i, x))
                col_has.add((j, x))
                box_has.add((i // 3, j // 3, x))
                
        return True