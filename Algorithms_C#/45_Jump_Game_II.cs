public class Solution {
    public int Jump(int[] nums) {
        int mx = 0, last = 0, ans = 0;
        for (int i = 0; i < nums.Length - 1; ++i){
            mx = Math.Max(mx, i + nums[i]);
            if (last == i){
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
}