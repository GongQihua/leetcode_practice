class Solution {
    void backtrack(vector<string>& ans, string& cur, int left, int right, int n){
        if (cur.size() == n * 2){
            ans.push_back(cur);
            return;
        }
        if (left < n){
            cur.push_back('(');
            backtrack(ans, cur, left+1, right, n);
            cur.pop_back();
        }
        if (right < left){
            cur.push_back(')');
            backtrack(ans, cur, left, right+1, n);
            cur.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current;
        backtrack(result, current, 0, 0, n);
        return result;
    }
};