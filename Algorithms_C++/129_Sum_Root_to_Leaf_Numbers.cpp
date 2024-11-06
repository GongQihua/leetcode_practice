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
    int dfs(TreeNode* root, int s){
        if(root == nullptr){
            return 0;
        }
        s = s * 10 + root->val;
        if(root->left == nullptr && root->right == nullptr){
            return s;
        }
        return dfs(root->left, s) + dfs(root->right, s);
    }
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
};