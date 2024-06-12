public class Solution {
    private void backtrack(List<string> ans, StringBuilder cur, int open, int close, int n) {
        if (cur.Length == n * 2) {
            ans.Add(cur.ToString());
            return;
        }
        if (open < n) {
            cur.Append('(');
            backtrack(ans, cur, open + 1, close, n);
            cur.Remove(cur.Length-1, 1);
        }
        if (close < open) {
            cur.Append(')');
            backtrack(ans, cur, open, close + 1, n);
            cur.Remove(cur.Length-1, 1);
        }
    }

    public IList<string> GenerateParenthesis(int n) {
        List<string> result = new List<string>();
        StringBuilder current = new StringBuilder();
        backtrack(result, current, 0, 0, n);
        return result;
    }
}