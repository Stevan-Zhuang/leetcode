class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = []
        for mm in matrix:
            m.extend(mm)
        m.sort()
        for i in range(0,len(m)-1,2):
            if m[i] <= 0 and m[i+1] <= 0 or (m[i] < 0 and m[i+1]>=0 and -m[i] > m[i+1]):
                m[i] *= -1
                m[i+1] *= -1
            else:
                break
        return sum(m)
