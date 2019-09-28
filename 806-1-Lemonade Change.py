# https://leetcode-cn.com/problems/lemonade-change/


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five, ten = five - 1, ten + 1
            elif ten > 0: five, ten = five - 1, ten - 1  # if 20, we try 10+5 first
            else: five -= 3
            if five < 0: return False
        return True



bills1 = [5,5,5,10,20]
bills2 = [5,5,10,10,20]