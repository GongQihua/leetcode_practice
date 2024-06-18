class Solution {
public:
    int binarySearch(vector<int>& nums, int target, bool lower) {
        int left = 0, right = (int)nums.size()-1, ans = (int)nums.size();
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
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = binarySearch(nums, target, true);
        int last = binarySearch(nums, target, false) - 1;
        if (first <= last && last < nums.size() && nums[first] == target && nums[last] == target){
            return vector<int> {first, last};
        }
        return vector<int> {-1, -1};
    }
};