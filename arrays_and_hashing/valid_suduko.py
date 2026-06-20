class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
            
                if val==".":
                    continue
                
                box_idx = (row//3,col//3)

                if (val in rows[row] or val in cols[col] or val in box[box_idx]):
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                box[box_idx].add(val)
        return True