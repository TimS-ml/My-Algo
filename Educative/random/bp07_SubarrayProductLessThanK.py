'''
Find all of its contiguous subarrays whose product is less than the target number

# Code Explain:
- Time complexity: O(n^3)
they believe substr generation will cause n^2
- Space complexity: O(n^3)

# Pros and Cons and Notation:
same as bp06
this time we are calc sub arr product instead of sum
**contiguous** subarrays, so don't sort arr

remember to use copy!!!
'''


def find_subarrays(arr, target):
    ans = []
    for i in range(len(arr)):
        if arr[i] < target:
            temp_mul = arr[i]
            temp_li = [arr[i]]
            ans.append(temp_li.copy())
            # print(temp_li, ans)

            for j in range(i+1, len(arr)):
                temp_mul *= arr[j]
                if temp_mul < target:
                    temp_li.append(arr[j])
                    ans.append(temp_li.copy())
                    # print(temp_li, ans)
                else:
                    break

    return ans


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    # print(find_subarrays([2, 2, 5, 3, 10], 0))
    # print(find_subarrays([8, 2, 6, 5], 50))


main()
