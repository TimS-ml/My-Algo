# https://leetcode-cn.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            ans.add(local.replace('.', '') + '@' + domain)
        return len(ans)


emails = [
    "test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
print(Solution().numUniqueEmails(emails))
