class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        s = set(A)
        count = 0
        for i in A:
            if i - 1 not in s:
                orig = i
                while i in s:
                    i += 1
                count = max(i-orig, count)
        return count

