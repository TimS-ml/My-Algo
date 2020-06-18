
import java.util.*;

class Solution {
  public String[] reorderLogFiles(String[] logs) {
    return logs;
  }
}

class Run {
  public static void main(String[] args) {
    String[] l =
        new String[] {
          "dig1 8 1 5 1"
        };
    Solution s = new Solution();
    String[] ans = s.reorderLogFiles(l);
    for (int i = 0; i < ans.length; i++) System.out.println(ans[i]);
  }
}
