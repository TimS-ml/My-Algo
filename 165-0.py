'''
- left to right
- preprocessing
    - ignore leading zeros

case:
2.5.33 vs 2.5
1.0.0 vs 1.0
1.0.0 vs 1.00
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def preprocessing(dig):
            return int(dig)

        l1, l2 = version1.split('.'), version2.split('.')
        while l1 and l2:
            dig1, dig2 = l1.pop(0), l2.pop(0)
            dig1 = preprocessing(dig1)
            dig2 = preprocessing(dig2)
            if dig1 > dig2:
                return 1
            elif dig1 < dig2:
                return -1

        # make sure it's a valid numbers
        # not like '['0', '00']'
        if l1 and preprocessing(''.join(l1)) != 0:
            return 1
        elif l2 and preprocessing(''.join(l2)) != 0:
            return -1
        else:
            return 0
