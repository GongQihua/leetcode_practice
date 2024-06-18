public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int first = binarySearch(nums, target, true);
        int last = binarySearch(nums, target, false) - 1;
        if (first <= last && last < nums.Length && nums[first] == target && nums[last] == target){
            return new int[] {first, last};
        }
        return new int[] {-1, -1};
    }
    
    public int binarySearch(int[] nums, int target, bool lower) {
        int left = 0, right = (int)nums.Length-1, ans = (int)nums.Length;
        while (left <= right){
            int mid = (left + right) >> 1;
            if (nums[mid] > target || (lower && nums[mid] >= target)){
                right = mid - 1;
                ans = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return ans;
    }
}