public class Solution {
    public string SimplifyPath(string path) {
        string[] names = path.Split("/");
        Stack<string> stk = new Stack<string>();
        foreach (string s in names){
            if (s == "" || s == "."){
                continue;
            }
            if (s == ".."){
                if (stk.Count > 0){
                    stk.Pop();
                }
            }
            else{
                stk.Push(s);
            }
        }
        StringBuilder ans = new StringBuilder();
        while (stk.Count > 0){
            ans.Insert(0, "/" + stk.Pop());
        }
        return ans.Length == 0 ? "/" : ans.ToString();
    }
}