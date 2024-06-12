class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        int n = s.size();
        if (n % 2 == 1){
            return false;
        }
        stack<char> stk;
        for (char ch : s){
            if (pairs.count(ch)){
                if (stk.empty() || stk.top() != pairs[ch]){
                    return false;
                }
                stk.pop();
            }
            else{
                stk.push(ch);
            }
        }
        return stk.empty();
    }
};