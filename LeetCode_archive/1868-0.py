'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        dot_encoded = []

        # pair index
        e1_index = 0
        e2_index = 0

        while e1_index < len(encoded1) and e2_index < len(encoded2):
            e1_val, e1_freq = encoded1[e1_index]
            e2_val, e2_freq = encoded2[e2_index]

            dot_val = e1_val * e2_val
            dot_freq = min(e1_freq, e2_freq)

            encoded1[e1_index][1] -= dot_freq
            encoded2[e2_index][1] -= dot_freq

            if encoded1[e1_index][1] == 0:
                e1_index += 1

            if encoded2[e2_index][1] == 0:
                e2_index += 1

            if not dot_encoded or dot_encoded[-1][0] != dot_val:
                dot_encoded.append([dot_val, dot_freq])
            # !!! merge dupl
            else:
                dot_encoded[-1][1] += dot_freq

        return dot_encoded
