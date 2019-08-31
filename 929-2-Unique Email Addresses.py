# https://leetcode-cn.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)


emails = ["test.email+alex@leetcode.com", 
        "test.e.mail+bob.cathy@leetcode.com", 
        "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))
