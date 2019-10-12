# https://leetcode-cn.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails) -> int:
        for i in range(len(emails)):
            # print(emails[i])
            punctuate1 = emails[i].find('+')
            punctuate2 = emails[i].find('@')
            emails[i] = emails[i][0:punctuate1] + emails[i][punctuate2:]

            count = 0
            punctuate2 = emails[i].find('@')
            for j in range(len(emails[i])):
                if (emails[i][j] == '.') and (j < emails[i].find('@')):
                    count += 1
            emails[i] = emails[i].replace('.', '', count)

        emails = list(set(emails))
        print(emails)
        return len(emails)


emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))
