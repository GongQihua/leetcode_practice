/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nums;
        while(head != nullptr){
            nums.push_back(head->val);
            head = head->next;
        }
        return dfs(nums, 0, nums.size()-1);
    }
    TreeNode* dfs(vector<int>& nums, int l, int r){
        if(l > r){
            return nullptr;
        }
        int mid = (l + r) >> 1;
        TreeNode* left = dfs(nums, l, mid - 1);
        TreeNode* right = dfs(nums, mid + 1, r);
        return new TreeNode(nums[mid], left, right);
    }
};