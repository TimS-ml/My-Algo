'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

def find_permutations(nums):
    def backtracking(subset):
        if len(subset) == len(nums):
            ans.append(subset[:])

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            subset.append(nums[i])
            backtracking(subset)
            used[i] = False
            subset.pop()

    ans = []
    used = [False for _ in range(len(nums))]
    backtracking([])
    return ans


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 2, 3, 4])))


main()
