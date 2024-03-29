'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero

# Code Explain:
- Time complexity: O(n^2)
Sorting the array will take O(n * logn)
The searchPair() function will take O(n)
  As we are calling searchPair() for every number in the input array,
    this means that overall searchTriplets() will take O(n * logn + n^2),
    which is asymptotically equivalent to O(n^2)
- Space complexity: O(n)


same as bp01
element may be used multiple times
- sorted first, 2 pointers from left and right move to middle
- !! skip same element to avoid duplicate triplets

case: [-1, -1, -1, 2]
    add [-1, -1, 2] at arr[0]
case: [-3, -2, -1, 0, 1, 1, 2]
    if arr[i] is -3 (x=-3)
    find y+z = 0-(-3)


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
    arr.sort()
    ans = []
    for i in range(len(arr) - 2):  # -2 is not necessary but good to have
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, ans)  # search from i+1 to len-1
    return ans


# 2 pointers from left and right move to middle
def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            # target_sum is arr[i], left starts at i+1
            # so the triplets is ascending order
            triplets.append([-target_sum, arr[left], arr[right]])
            # avoid duplicate triplets
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def search_triplets_my(arr):
    def search_pair(target, subarr, ans):
        # find all x + y == target
        for i in range(len(subarr) - 1):
            if i > 0 and subarr[i] == subarr[i - 1]:
                continue
            # subarr[i + 1:] is O(n) which is slow
            # also not using the 'sorted' condition
            if target - subarr[i] in subarr[i + 1:]:
                ans.append([-target, subarr[i], target - subarr[i]])
        return ans

    arr.sort()
    ans = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        ans = search_pair(-arr[i], arr[i + 1:], ans)
    return ans


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets_my([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets_my([-5, 2, -1, -2, 3]))


main()
