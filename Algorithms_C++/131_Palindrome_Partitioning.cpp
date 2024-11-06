class Solution {
public:
    vector<vector<int>> f;
    vector<vector<string>> ans;
    vector<string> t;
    int n;

    void dfs(const string& s, int i) {
        if (i == n) {
            ans.push_back(t);
            return;
        }
        for (int j = i; j < n; ++j) {
            if (f[i][j]) {
                t.push_back(s.substr(i, j - i + 1));
                dfs(s, j + 1);
                t.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        n = s.size();
        f.assign(n, vector<int>(n, true));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 1; j < n; ++j) {
                f[i][j] = (s[i] == s[j]) && f[i + 1][j - 1];
            }
        }
        dfs(s, 0);
        return ans;
    }
};