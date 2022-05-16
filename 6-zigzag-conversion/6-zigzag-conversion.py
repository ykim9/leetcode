class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows <= 1:
            return s
        
        rows = [''] * numRows
        rowIdx = 1
        incr = 1
        for c in s:
            rows[rowIdx-1] += c
            if rowIdx == numRows:
                incr = -1
            elif rowIdx == 1:
                incr = 1
            
            rowIdx += incr
        
        return "".join(rows)
        
            
                
                        