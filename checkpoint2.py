class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        ans = [] # contains final rows, that need to be printed 
        start = [A] * (2*A -1) # starting row with all As
        for i in xrange(A):
            row = start[:]
            for j in xrange(i+1): # loop needs to run i+1 times
                row[j:2*A - j - 1] = [A-j] * (2*A - 2*j - 1)
            ans.append(row)
        ans = ans + ans[:-1][::-1]
        return ans
