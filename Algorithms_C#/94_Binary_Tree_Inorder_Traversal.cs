/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> InorderTraversal(TreeNode root) {
        IList<int> ans = new List<int>();
        dfs(root, ans);
        return ans;
    }

    private void dfs(TreeNode root, IList<int> ans){
        if(root == null){
            return;
        }
        dfs(root.left, ans);
        ans.Add(root.val);
        dfs(root.right, ans);
    }
}