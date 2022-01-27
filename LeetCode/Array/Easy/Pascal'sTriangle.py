# Pascal'sTriangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1] for _ in range(numRows)]
        if numRows > 1:
            rows[1] += [1]

        for row_idx in range(1, len(rows) - 1):
            for col_idx in range(row_idx):
                rows[row_idx + 1] += [rows[row_idx]
                                      [col_idx] + rows[row_idx][col_idx + 1]]
            rows[row_idx + 1] += [1]

        return rows
