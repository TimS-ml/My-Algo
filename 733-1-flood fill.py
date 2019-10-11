# https://leetcode-cn.com/problems/flood-fill/


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if color!=newColor:
            self.dfs(sr, sc, image, color, newColor)
        return image


    def dfs(self, i, j,image,color,newColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=color:
            return
        image[i][j] = newColor
        self.dfs(i+1, j, image, color, newColor)
        self.dfs(i-1, j, image, color, newColor)
        self.dfs(i, j+1, image, color, newColor)
        self.dfs(i, j-1, image, color, newColor)


image1 = [
    [1,1,1],
    [1,1,0],
    [1,0,1]]
image2 = [
    [1,0,1],
    [0,1,0],
    [1,0,1]]
sr, sc = 1, 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))
