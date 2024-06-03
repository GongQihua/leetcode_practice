class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i){
            int x = nums[i];
            int y = target - x;
            if (hashtable.count(y)){
                return {hashtable[y], i};
            }
           hashtable[x] = i; 
        }
        return{};
    }
};