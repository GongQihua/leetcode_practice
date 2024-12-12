class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums[0] <= nums[nums.size() - 1]){
            return nums[0];
        }
        int left = 0, right = nums.size() - 1;
        while(left < right){
            int mid = (left + right) >> 1;
            if(nums[0] <= nums[mid]){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return nums[left];
    }
};