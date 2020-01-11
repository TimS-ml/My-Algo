# include <iostream>
# include <vector>
# include <unordered_map>
using namespace std;


class Solution {
    public:
        int dirs[2][2] = {{-1, 0}, {0, -1}}; // array init
        bool valid(int row, int col, int R, int C) {
            return row >= 0 && row < R && col >= 0 && col < C;
        }

        int surface(int height) {
            return 2 + 4 * height;
        }

        int surfaceArea(vector<vector<int>>& grid) {
            if (grid.empty()) return 0;
            int R = grid.size();
            int C = grid[0].size();
            int ans = 0;
            for (int i = 0; i < R; ++i) {
                for (int j = 0; j < C; ++j) {
                    if (grid[i][j] == 0) continue;
                    ans += surface(grid[i][j]);
                    for (int k =0; k < 2; ++k) {
                        int row = i + dirs[k][0];
                        int col = j + dirs[k][1];
                        if (!valid(row, col, R, C)) continue;
                        ans -= 2 * min(grid[i][j], grid[row][col]);  // deduct double counting
                    }
                }
            }
            return ans;
        }
};


int main(){
	vector<vector<int>> grid{{1, 2},
                             {3, 4}};
    int ans = Solution().surfaceArea(grid);
    cout << ans << endl;
    return 0;
}
