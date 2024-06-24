class Solution {
public:
    int jump(vector<int>& nums) {
        int mx = 0, last = 0, ans = 0;
        for (int i = 0; i < nums.size()-1; ++i){
            mx = max(mx, i + nums[i]);
            if (last == i){
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
};