# use set and hashMap for O(1) search
# first solve it for rows and cols . then for boxes.
# 0//3 =0 , 1//3 =0 , 2//3 =0
# 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #key = 0,1,2,...8 (row no.)
        cols= collections.defaultdict(set)  # key = 0,1,2,...8 (row no.)
        boxes = collections.defaultdict(set) # key  = (0,0), (0,1) ----(r//3 ,c//3)
        for r in range(9):
            for c in range(9):
                if board [r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3,c//3)]:
                    return False
                elif board[r][c] != ".":
                    if board[r][c] not in rows[r]:
                        rows[r].add(board[r][c])
                    if board[r][c] not in cols[c]:
                        cols[c].add(board[r][c])
                    if board[r][c] not in boxes[(r//3,c//3)]:
                        boxes[(r//3,c//3)].add(board[r][c])

        return True       

        
        