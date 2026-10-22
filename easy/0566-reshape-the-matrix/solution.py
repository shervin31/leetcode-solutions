class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np

        if len(mat) * len(mat[0]) != r * c:
            return mat

        mat = np.array(mat)
        reshaped = mat.reshape(r, c)
        return reshaped.tolist()