class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        seen = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue
                
                row_key = (value, 'row', r)
                column_key = (value, 'col', c)
                box_key = (value, 'box', r // 3, c // 3)

                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)

        return True