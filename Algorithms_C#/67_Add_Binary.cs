public class Solution {
    public string AddBinary(string a, string b) {
        StringBuilder ans = new StringBuilder();
        int i = a.Length - 1, j = b.Length - 1;
        for (int carry = 0; i >= 0 || j >= 0 || carry > 0; --i, --j){
            carry += (i >= 0 ? a[i] - '0' : 0) + (j >= 0 ? b[j] - '0' : 0);
            ans.Append(carry % 2);
            carry /= 2;
        }
        StringBuilder ans2 = new StringBuilder();
        for (int k = ans.Length - 1; k >= 0; --k){
            ans2.Append(ans[k]);
        }
        return ans2.ToString();
    }
}