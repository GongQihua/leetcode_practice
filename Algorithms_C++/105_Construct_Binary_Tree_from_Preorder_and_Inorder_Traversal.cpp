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
    unordered_map<int, int> d;
    TreeNode* dfs(vector<int>& preorder, vector<int>& inorder, int i, int j, int n){
        if(n <= 0){
            return nullptr;
        }
        int v = preorder[i];
        int k = d[v];
        TreeNode* l = dfs(preorder, inorder, i + 1, j, k - j);
        TreeNode* r = dfs(preorder, inorder, i + 1 + k - j, k + 1, n - 1 - (k - j));
        return new TreeNode(v, l, r);
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        for(int i = 0; i < n; ++i){
            d[inorder[i]] = i;
        }
        return dfs(preorder, inorder, 0, 0, n);
    }
};