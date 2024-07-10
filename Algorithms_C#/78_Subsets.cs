public class Solution {
    private IList<IList<int>> ans = new List<IList<int>>();
    private List<int> t = new List<int>();

    public IList<IList<int>> Subsets(int[] nums) {
        dfs(0, nums);
        return ans;
    }

    private void dfs(int i, int[] nums){
        if(i == nums.Length){
            ans.Add(new List<int>(t));
            return;
        }
        t.Add(nums[i]);
        dfs(i+1, nums);
        t.RemoveAt(t.Count - 1);
        dfs(i+1, nums);
    }
}