class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # result array to return later

        row_start = 0
        row_end = len(matrix)-1
        col_start = 0
        col_end = len(matrix[0])-1

        while (row_start <= row_end) and (col_start <= col_end):

            # left to right
            for i in range(col_start, col_end+1):
                res.append(matrix[row_start][i])
            # increment the row start
            row_start += 1

            # top to bottom
            for i in range(row_start, row_end+1):
                res.append(matrix[i][col_end])
            # decrement the col end
            col_end -= 1

            # right to left
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    res.append(matrix[row_end][i])
                # decrement the row end
                row_end -= 1

            # bottom to top
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    res.append(matrix[i][col_start])
                # increment the col_start
                col_start += 1

        # return res array 
        return res
        