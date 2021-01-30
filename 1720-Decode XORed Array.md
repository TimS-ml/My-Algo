# Links
https://leetcode-cn.com/problems/decode-xored-array/

# Thought Process
Since that encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].
Iterate on i from beginning to end, and set arr[i+1] = encoded[i] XOR arr[i].

# Test Cases

