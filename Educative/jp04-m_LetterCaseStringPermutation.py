'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

def find_letter_case_string_permutations(S):
    def backtrack(subset, start):
        # at leaf
        if len(subset) == len(S):
            ans.append(subset)
        else:
            if S[start].isalpha():
                backtrack(subset + S[start].swapcase(), start + 1)
            backtrack(subset + S[start], start + 1)

    ans = []
    backtrack('', 0)
    return ans



def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
