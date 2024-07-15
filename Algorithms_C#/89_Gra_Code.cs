public class Solution {
    public IList<int> GrayCode(int n) {
        IList<int> ans = new List<int>();
        for(int i = 0; i < 1 << n; ++i){
            ans.Add(i ^ (i >> 1));
        }
        return ans;
    }
}