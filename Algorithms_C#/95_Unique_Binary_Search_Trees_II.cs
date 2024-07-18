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
    public IList<TreeNode> GenerateTrees(int n) {
        if (n == 0) {
            return new List<TreeNode>{};
        }
        return generateTrees(1, n);
    }

    public IList<TreeNode> generateTrees(int start, int end){
        if (start > end) {
            return new List<TreeNode>{null};
        }
        IList<TreeNode> allTrees = new List<TreeNode>();
        for (int i = start; i <= end; i++) {
            IList<TreeNode> leftTrees = generateTrees(start, i - 1);
            IList<TreeNode> rightTrees = generateTrees(i + 1, end);

            foreach (TreeNode left in leftTrees) {
                foreach (TreeNode right in rightTrees) {
                    TreeNode currTree = new TreeNode(i);
                    currTree.left = left;
                    currTree.right = right;
                    allTrees.Add(currTree);
                }
            }
        }
        return allTrees;
    }
}