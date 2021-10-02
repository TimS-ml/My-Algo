'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
[[1,1,0],
 [1,0,1],
 [0,0,0]]

step1
[[0,1,1],
 [1,0,1],
 [0,0,0]]

step2
[[1,0,0],
 [0,1,0],
 [1,1,1]]
'''


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if image[i][left] == image[i][right]:
                    image[i][left] ^= 1
                    image[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                image[i][left] ^= 1
        return image
