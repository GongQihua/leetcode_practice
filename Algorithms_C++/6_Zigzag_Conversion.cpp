class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.length(), r = numRows;
        if (r == 1 || r >= n){
            return s;
        }
        string ans;
        int t = 2 * r - 2;
        for (int i = 0; i < r; ++i){
            for (int j = 0; j+i < n; j += t){
                ans += s[j + i];
                if (0 < i && i < r - 1 && j + t - i < n){
                    ans += s[j + t - i];
                }
            }
        }
        return ans;
    }
};