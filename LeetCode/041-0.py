'''
search -> hash set

[1] Build hash set
[2] Starting from assuming missing number = 1
    Search in hash set

The worse case: 
[1, 2, 3], missing 4 = len(arr) + 1
solution set = [1, len(arr) + 1], len(sol set) = len(arr)

Memory Optimization:
sol set and input arr mapping
'''

class Solution:
    def firstMissingPositive(self, A):
        # set neg num to 0
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0

        # use list as hash set
        # mimic checking from 1 to len(A)+1
        # if valid val in A => save the checking result to idx=val-1 by *= -1
        # case A0 = [2, 1]
        # val = 2, set idx=val-1=1 to *= -1
        #      A1 = [2, -1]
        # then loop to next value, abs(A1[1]) = A0[1], no info loss
        # val = 1, set idx=val-1=0 to *=-1
        #      A2 = [-2, -1]
        # then, check the '-' sing in An
        # if we found a '+' number A[i], means this i does not exsit in An
        # return this idx
        # the idx i matters, but we don't care about the value of abs(A[i])
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)

        for i in range(1, len(A) + 1):
            if A[i - 1] >= 0:
                return i
        return len(A) + 1
