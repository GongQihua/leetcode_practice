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
    vector<TreeNode*> dfs(int start, int end){
        if(start > end){
            return {nullptr};
        }
        vector<TreeNode*> allTrees;

        for(int i = start; i <= end; ++i){
            vector<TreeNode*> leftTrees = dfs(start, i-1);
            vector<TreeNode*> rightTrees = dfs(i+1, end);
            for(auto& left : leftTrees){
                for(auto& right : rightTrees){
                    TreeNode* curTree = new TreeNode(i);
                    curTree->left = left;
                    curTree->right = right;
                    allTrees.push_back(curTree);
                }
            }
        }
        return allTrees;
    }
    vector<TreeNode*> generateTrees(int n) {
        if(!n){
            return {};
        }
        return dfs(1, n);
    }
};