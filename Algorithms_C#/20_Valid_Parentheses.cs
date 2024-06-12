public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> pairs = new Dictionary<char,char>(){
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        int n = s.Length;
        if (n % 2 == 1){
            return false;
        }
        Stack<char> stk = new Stack<char>();
        foreach (char ch in s){
            if (pairs.ContainsKey(ch)){
                if (stk.Count == 0 || stk.Pop() != pairs[ch]){
                    return false;
                }
            }
            else{
                stk.Push(ch);
            }
        }
        return stk.Count == 0 ? true : false;
    }
}