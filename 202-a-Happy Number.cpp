// 2 pointers, no need for hash
// because non-happy number will fall in loop:
// 4 16 37 58 89 145 42 20

# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int bitSquareSum(int n){
        int sum = 0;
        while(n > 0){
            int bit = n % 10;
            sum += bit * bit;
                n = n / 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow = n, fast = n;
        do{
            slow = bitSquareSum(slow);
            fast = bitSquareSum(fast);
            fast = bitSquareSum(fast);
        } while(slow != fast);
        return slow == 1;
    }
};

int main(){
	vector<int> nums;
    int n = 19;
	int target = 9;
    bool ans = Solution().isHappy(n);
    cout << ans << endl;
    return 0;
}
