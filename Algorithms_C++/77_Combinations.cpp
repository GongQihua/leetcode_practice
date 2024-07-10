class Solution {
public:
    vector<vector<int>> ans;
    vector<int> t;

    void dfs(int i, int n, int k){
        if (t.size() == k){
            ans.emplace_back(t);
            return;
        }
        if (i > n){
            return;
        }
        t.emplace_back(i);
        dfs(i+1, n, k);
        t.pop_back();
        dfs(i+1, n, k);
    }

    vector<vector<int>> combine(int n, int k) {
        dfs(1, n, k);
        return ans;
    }
};