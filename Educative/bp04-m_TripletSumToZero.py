'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)


target = 0 = a + b + c

for i in xxx:
    a = arr[i]
    for j in xxx:
        # search pair in range j
        if -(c+b) == a:
            ans.append([a, b, c])  # a <= b <= c

[1] How to avoid duplicate?
- Make sure all elements in sub-list are in the same order
- Sort elements and skip duplicate one, search range should not be overlap
    - case: [-1, -1, -1, -1, 2]
[2] Convert to search pair
'''


def search_triplets(arr):
    def search_pair(target, subarr, ans):
        # find all x + y == target
        for i in range(len(subarr)-1):
            if i > 0 and subarr[i] == subarr[i - 1]:
                continue
            if target - subarr[i] in subarr[i+1:]:
                ans.append([-target, subarr[i], target - subarr[i]])
        return ans

    arr.sort()
    ans = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        ans = search_pair(-arr[i], arr[i+1:], ans)
    return ans


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    # print(search_triplets([-5, 2, -1, -2, 3]))


main()
