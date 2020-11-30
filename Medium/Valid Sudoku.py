class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                
                val = board[i][j]
                
                if val != '.':
                    num = int(val)
                    box_index = (i // 3) * 3 + j // 3
                    
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
                    
        return True
        