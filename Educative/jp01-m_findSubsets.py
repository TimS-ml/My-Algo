'''
# Code Explain:
- Time complexity: O(N * 2^N)
- Space complexity: O(N * 2^N)

'''

def find_subsets(nums):
    def backtrack(start, subset):
        ans.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    ans = []
    backtrack(0, [])
    return ans


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
