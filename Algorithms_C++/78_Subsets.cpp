class Solution {
public:
    vector<vector<int>> ans;
    vector<int> t;

    void dfs(int i, vector<int>& nums){
        if (i == nums.size()){
            ans.push_back(t);
            return;
        }
        t.push_back(nums[i]);
        dfs(i+1, nums);
        t.pop_back();
        dfs(i+1, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(0, nums);
        return ans;
    }
};