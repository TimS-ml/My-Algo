'''
https://leetcode.com/problems/merge-intervals/
https://leetcode.com/problems/insert-interval/
https://leetcode.com/problems/meeting-rooms-ii/
'''

# def check_interval(i1, i2):
#     # assert i1.start <= i1.end
#     # assert i2.start <= i2.end

#     # i1.start <= i2.start <= i1.start <= i2.end
#     if i1[0] <= i2[0] <= i1[1]:
#         return True
#     elif i2[0] <= i1[0] <= i0[1]:
#         return True

#     return False

# def check_interval_2(i1, i2):
#     # overlap
#     # now we know i1[0] <= i2[0]

#     if i1[0] > i2[0]:
#         i1, i2 = i2, i1

#     if i2[0] <= i1[0]:
#         return True
#     else:
#         return False

class Interval:
    def __init__(self, intvs):
        # self.intvs = intvs
        self.intvs = sorted(intvs, key=lambda x: x[0])

    @staticmethod
    def check_overlap(i1, i2):
        # assert i1[0] > i2[0]
        if i2[0] <= i1[0]:
            return True
        else:
            return False

    def check_has_overlap(self):
        start, end = self.intvs[0][0], self.intvs[0][1]

        for i in range(1, len(self.intvs)):
            # found overlap
            if self.check_overlap([start, end], self.intvs[i]):
                print(f'found overlap! {start}, {end} and {self.intvs[i][0]}, {self.intvs[i][1]}')
                # start = min(start, self.intvs[i][0])
                # end = max(end, self.intvs[i][1])
                return False
            else:
                start, end = self.intvs[i]
        return True

    def check_and_merge_overlap(self):
        start, end = self.intvs[0][0], self.intvs[0][1]

        merged = []
        for i in range(1, len(self.intvs)):
            # found overlap
            if self.check_overlap([start, end], self.intvs[i]):
                print(f'found overlap! {start}, {end} and {self.intvs[i][0]}, {self.intvs[i][1]}')
                start = min(start, self.intvs[i][0])
                end = max(end, self.intvs[i][1])
            else:
                merged.append([start, end])
                start, end = self.intvs[i]

        self.intvs = merged
        print(self.intvs)
        return self

    def append_pair(self, pair):
        for i in range(len(self.intvs)):
            if pair[0] <= self.intvs[i][0]:
                self.intvs.insert(i, pair)
                return self
        print('insert at end')
        # self.intvs.insert(len(self.intvs), pair)
        self.intvs.append(pair)
        return self

    def remove_pair(self, pair):
        if pair in self.intvs:
            self.intvs.remove(pair)
            return True
        else:
            print('not found')
            return False


# test = [[1,2],[3,5],[3,14]]
test = [[1,2],[3,5],[3,14],[3,10],[12,16],[4,8]]
test = Interval(test)
# test.check_has_overlap()
# print(test.check_overlap([3,5],[3,7]))
# test.check_and_merge_overlap()
test.append_pair([5,24])
test.remove_pair([3,14])
print(test.intvs)
