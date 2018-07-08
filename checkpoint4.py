class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        ans = []
        for idx, val in enumerate(A):
            res = None
            for ele in A[idx+1:]:
                if ele > val:
                    res = ele
                    break
            if res is None:
                ans.append(-1)
            else:
                ans.append(res)
    
        return ans

