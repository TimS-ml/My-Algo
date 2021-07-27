// https://leetcode-cn.com/problems/most-common-word/

import java.util.*;

class Solution {
  public String mostCommonWord(String paragraph, String[] banned) {
    paragraph += ".";

    Set<String> banset = new HashSet();
    for (String word : banned) banset.add(word);
    Map<String, Integer> count = new HashMap();

    String ans = "";
    int ansfreq = 0;

    StringBuilder word = new StringBuilder();
    for (char c : paragraph.toCharArray()) {
      if (Character.isLetter(c)) {
        word.append(Character.toLowerCase(c));
      } else if (word.length() > 0) {
        String finalword = word.toString();
        if (!banset.contains(finalword)) {
          count.put(finalword, count.getOrDefault(finalword, 0) + 1);
          if (count.get(finalword) > ansfreq) {
            ans = finalword;
            ansfreq = count.get(finalword);
          }
        }
        word = new StringBuilder();
      }
    }
    return ans;
  }
}

class Run {
  public static void main(String[] args) {
    String p = "Bob hit a ball, the hit BALL flew far after it was hit.";
    String[] b = {"hit"};
    Solution s = new Solution();
    String ans = s.mostCommonWord(p, b);
    System.out.println(ans);
  }
}
