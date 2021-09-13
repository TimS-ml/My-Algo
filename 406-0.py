'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

Usually sort the p[0] in ascending order and p[1] with decending order (or vice versa) is ok

首先对数对进行排序: 按照数对的元素 1 降序排序 and 按照数对的元素 2 升序排序
原因是, 按照元素 1 进行降序排序
- 对于每个元素 在其之前的元素的个数, 就是大于等于他的元素的数量
- 而按照第二个元素正向排序, 我们希望 k 大的尽量在后面

高个子先站好位, 矮个子插入到K位置上
前面肯定有K个高个子, 矮个子再插到前面也满足K的要求

- [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
- [7,0]
- [7,0], [7,1]
- [7,0], [6,1], [7,1]
- [5,0], [7,0], [6,1], [7,1]
- [5,0], [7,0], [5,2], [6,1], [7,1]
- [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]
'''


class Solution:
    def reconstructQueue(self, people):
        # queue = []
        # people = sorted(people,
        #                 key=lambda x: (x[0], x[1] and -x[1]),
        #                 reverse=True)
        # for p in people:
        #     # for p in sorted(people, key=lambda (h,k): (-h,k)):  # doesn't work
        #     queue.insert(p[1], p)
        # return queue

        ans = []
        people = sorted(people, 
                        key = lambda x: (-x[0], x[1]))
        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            elif len(ans) > p[1]:
                ans.insert(p[1], p)
        return ans

    def reconstructQueue_2(self, people):
        people = sorted(people, 
                        key=lambda x: (-x[0], x[1]))
        i = 0
        while i < len(people):
            if i > people[i][1]:
                people.insert(people[i][1], people[i])
                people.pop(i + 1)
            i += 1
        return people


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))
