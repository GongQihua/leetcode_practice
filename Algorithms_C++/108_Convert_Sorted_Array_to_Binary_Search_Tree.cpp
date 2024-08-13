/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return dfs(0, nums.size()-1, nums);
    }
    TreeNode* dfs(int l, int r, vector<int>& nums){
        if(l > r){
            return nullptr;
        }
        int mid = (l + r) >> 1;
        TreeNode* left = dfs(l, mid - 1, nums);
        TreeNode* right = dfs(mid + 1, r, nums);
        return new TreeNode(nums[mid], left, right);
    }
};