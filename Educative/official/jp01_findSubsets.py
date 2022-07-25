'''
# Code Explain:
- Time complexity: O(N * 2^N)
- Space complexity: O(N * 2^N)

lc 78
input no dupl + element select once + subset / comb
'''

def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
