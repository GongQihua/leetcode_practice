public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();
        int n = nums.Length;
        for (int i = 0; i < n; i++){
            int y = target - nums[i];
            if (dict.ContainsKey(y) && dict[y] != i){
                return new int[]{i, dict[y]};
            }
            if(!dict.ContainsKey(nums[i])){
                dict.Add(nums[i],i);
            }
        }
        return new int[]{0,0};
    }
}