public class Solution {
    public int Trap(int[] height) {
        int ans = 0;
        int left = 0, right = height.Length - 1;
        int leftMax = 0, rightMax = 0;
        while (left < right){
            leftMax = Math.Max(leftMax, height[left]);
            rightMax = Math.Max(rightMax, height[right]);
            if (height[left] < height[right]){
                ans += leftMax - height[left];
                ++left;
            }else{
                ans += rightMax - height[right];
                --right;
            }
        }
        return ans;
    }
}