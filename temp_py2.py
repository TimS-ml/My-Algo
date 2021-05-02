def romanToInt(s: str) -> int:
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    
    # Or return ans if you choose this
    # for i, n in enumerate(s):
    #     if i < len(s)-1 and dic[s[i]] < dic[s[i+1]]:
    #         ans -= dic[s[i]]
    #     else:
    #         ans += dic[s[i]]

    for i in range(len(s) - 1):
        if dic[s[i]] < dic[s[i+1]]:
            ans -= dic[s[i]]
        else:
            ans += dic[s[i]]

    return ans + dic[s[-1]]


def test_answer():
    t1 = "MCMXCI"
    t2 = "MCMXCIV"
    assert romanToInt(t1) == 1991
    # assert romanToInt(t1) == 1992  # rise error
    assert romanToInt(t2) == 1994
    print('Done')

test_answer()
