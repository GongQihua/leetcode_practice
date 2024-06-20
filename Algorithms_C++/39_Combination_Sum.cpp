class Solution {
public:
    void dfs(vector<int>& candidates, int target, vector<vector<int>>& ans, vector<int>& t, int i){
        if (i == candidates.size()){
            return;
        }
        if (target == 0){
            ans.emplace_back(t);
            return;
        }
        dfs(candidates, target, ans, t, i+1);
        if (target - candidates[i] >= 0){
            t.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], ans, t, i);
            t.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> t;
        dfs(candidates, target, ans, t, 0);
        return ans;
    }
};