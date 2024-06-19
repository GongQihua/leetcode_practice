public class Solution {
    public string CountAndSay(int n) {
        string prev = "1";
        for (int i = 2; i <= n; ++i){
            StringBuilder curr = new StringBuilder();
            int start = 0, pos = 0;

            while(pos < prev.Length){
                while(pos < prev.Length && prev[pos] == prev[start]){
                    pos++;
                }
                curr.Append(pos - start);
                curr.Append(prev[start]);
                start = pos;
            }
            prev = curr.ToString();
        }
        return prev;
    }
}