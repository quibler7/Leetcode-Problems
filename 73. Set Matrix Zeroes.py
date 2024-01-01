class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # see which row and column we have to zero
        # go through and do zero

        rows, cols = len(matrix), len(matrix[0])
        rowZero = 1

        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == 0:
                    # make row and column zero
                    # if row is zeroth row then make 'rowZero' zero
                    if r == 0: rowZero = 0
                    else: matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # make row and col zero 
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # first row
        # first col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if not rowZero:
            for c in range(cols):
                matrix[0][c] = 0

        
        return matrix





