class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        def partition(A, low, high):
            i = low
            j = high
            v = A[low]
            while True:
                while A[i] <= v:
                    i = i + 1
                    if i > high:
                        break
                while A[j] > v:
                    j = j - 1
                    if j < low:
                        break
                
                if i >= j:
                    break
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                
            temp = A[low]
            A[low] = A[j]
            A[j] = temp
            return j
    
        low = 0
        high = len(A) - 1 
        while True:
            j = partition(A, low, high)
            if j < B - 1:
                low = j + 1
            elif j > B - 1:
                high = j - 1 
            else:
                break
        return A[j]

