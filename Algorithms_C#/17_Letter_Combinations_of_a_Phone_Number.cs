public class Solution {
    private string[] d = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    private string digits;
    private List<string> ans = new List<string>();
    private StringBuilder t = new StringBuilder();

    public IList<string> LetterCombinations(string digits) {
        if (digits.Length == 0){
            return ans;
        }
        this.digits = digits;
        dfs(0);
        return ans;
    }

    public void dfs(int i){
        if (i >= digits.Length){
            ans.Add(t.ToString());
            return;
        }
        string s = d[digits[i] - '2'];
        foreach (char c in s){
            t.Append(c);
            dfs(i+1);
            t.Remove(t.Length-1,1);
        }
    }
}