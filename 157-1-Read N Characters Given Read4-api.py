# https://leetcode-cn.com/problems/read-n-characters-given-read4/
# By using the read4 method, 
# implement the method read that reads n characters from the file 
# and store it in the buffer array buf. 
# Consider that you cannot manipulate the file directly


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        cnt = 0
        tmp = [""] * 4
        while cnt < n:
            r = read4(tmp)
            if r == 0:
                break
            for i in range(min(r, n - cnt)):
                buf[cnt] = tmp[i]
                cnt += 1
        return cnt


file = "abcdefg"
n = 5
