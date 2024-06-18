public class Solution {
    public int LongestValidParentheses(string s) {
        int ans = 0;
        Stack<int> stk = new Stack<int>();
        stk.Push(-1);
        for (int i = 0; i < s.Length; ++i){
            if (s[i] == '('){
                stk.Push(i);
            }
            else{
                stk.Pop();
                if (stk.Count == 0){
                    stk.Push(i);
                }
                else{
                    ans = Math.Max(ans, i - stk.Peek());
                }
            }
        }
        return ans;
    }
}