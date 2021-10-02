'''
# Code Explain:
- Time complexity: O(nlogn) for sort()
- Space complexity: O()

# Pros and Cons and Notation:
先对people 排序
然后用两个指针分别指向体重最轻和体重最重的人
'''


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans
