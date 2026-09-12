class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        nums_sort = list(set([val for val in nums]))
        nums_sort.sort()

        def LCS(seq_1:List, seq_2:List):
            # here both have same length by design
            n = len(seq_1)
            m = len(seq_2)
            lcs = [[0]*(m+1)]*(n+1)
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if seq_1[i-1] == seq_2[j-1]:
                        lcs[i][j] = lcs[i-1][j-1] + 1
                    else:
                        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            return lcs[n][m]
        
        return LCS(nums, nums_sort)