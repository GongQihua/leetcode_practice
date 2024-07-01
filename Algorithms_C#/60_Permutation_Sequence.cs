public class Solution {
    public string GetPermutation(int n, int k) {
        var ans = new StringBuilder();
        bool[] vis = new bool[10];
        for (int i = 0; i < n; ++i){
            int fact = 1;
            for (int j = 1; j < n-i; ++j) fact *= j;
            for (int j = 1; j <= n; ++j){
                if (vis[j]) continue;
                if (k > fact) k -= fact;
                else{
                    ans.Append(j);
                    vis[j] = true;
                    break;
                }
            }
        }
        return ans.ToString();
    }
}