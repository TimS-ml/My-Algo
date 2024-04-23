# https://leetcode-cn.com/problems/string-compression/
# 2 pointers, inplace


class Solution:
    def compress(self, chars):
        anchor = left = 0  # anchor at the start point of the block
        for key, value in enumerate(chars):
            # remember limit of len(chars)
            # chars[key + 1] != value means end of this block, use left pointer to write
            if key + 1 == len(chars) or chars[key + 1] != value:
                # overwrite
                chars[left] = chars[anchor]
                left += 1
                if key > anchor:
                    # count 12 -> "1", "2"
                    for digit in str(key - anchor + 1):
                        chars[left] = digit
                        left += 1
                anchor = key + 1
        return chars[:left]
        # return left


chars = ["a", "a", "a", "b", "c", "c", "c", "a"]
print(Solution().compress(chars))
