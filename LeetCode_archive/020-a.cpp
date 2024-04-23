#include <iostream>
#include <stack>
using std::stack;
using namespace std;

class Solution {
public:
  bool isValid(string s) {
    stack<char> st;
    for (auto c : s) // iterate over each and every elements
    {
      if (c == '(' or c == '{' or c == '[')
        st.push(c);
      else {
        // if (st.empty() or (st.top() == '(' and c != ')') or
        //     (st.top() == '{' and c != '}') or (st.top() == '[' and c != ']'))
        //   return false;
        if (st.empty())
          return false;
        if (c == ')' && st.top() != '(')
          return false;
        if (c == '}' && st.top() != '{')
          return false;
        if (c == ']' && st.top() != '[')
          return false;
        st.pop();
      }
    }
    return st.empty();
  }

  bool isValid_2(string s) {
    stack<char> paren;
    for (char &c : s) {
      switch (c) {
      case '(':
      case '{':
      case '[':
        paren.push(c);
        break;
      case ')':
        if (paren.empty() || paren.top() != '(')
          return false;
        else
          paren.pop();
        break;
      case '}':
        if (paren.empty() || paren.top() != '{')
          return false;
        else
          paren.pop();
        break;
      case ']':
        if (paren.empty() || paren.top() != '[')
          return false;
        else
          paren.pop();
        break;
      default:; // pass
      }
    }
    return paren.empty();
  }
};

int main() {
  Solution sol;
  string s = "[()]{}";

  bool result = sol.isValid(s);
  cout << result << endl;

  return 0;
};
