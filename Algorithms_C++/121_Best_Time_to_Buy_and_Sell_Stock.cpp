class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int mi = 1e9;
        for(int v : prices){
            ans = max(ans, v - mi);
            mi = min(mi, v);
        }
        return ans;
    }
};