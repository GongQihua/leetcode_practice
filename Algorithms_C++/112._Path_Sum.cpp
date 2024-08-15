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
    bool hasPathSum(TreeNode* root, int targetSum) {
        return dfs(root, targetSum, 0);
    }
    bool dfs(TreeNode* root, int targetSum, int s){
        if(!root){
            return false;
        }
        s += root->val;
        if(!root->left && !root->right && s == targetSum){
            return true;
        }
        return dfs(root->left, targetSum, s) || dfs(root->right, targetSum, s);
    }
};