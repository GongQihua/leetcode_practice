public class Solution {
    public bool Search(int[] nums, int target) {
        int l = 0, r = nums.Length - 1;
        while(l < r){
            int mid = (l + r) >> 1;
            if(nums[mid] > nums[r]){
                if(nums[l] <= target && target <= nums[mid]){
                    r = mid;
                }
                else{
                    l = mid + 1;
                }
            }
            else if(nums[mid] < nums[r]){
                if(nums[mid] < target && target <= nums[r]){
                    l = mid + 1;
                }
                else{
                    r = mid;
                }
            }
            else{
                --r;
            }          
        }
        return nums[l] == target;
    }
}