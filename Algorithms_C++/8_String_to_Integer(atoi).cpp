class Solution {
public:
    int myAtoi(string s) {
        unsigned long len = s.length();
        int index = 0;
        while (index < len){
            if (s[index] != ' '){
                break;
            }
            ++index;
        }
        if (index == len){
            return 0;
        }
        int sign = 1;
        if (s[index] == '+'){
            ++index;
        }
        else if(s[index] == '-'){
            sign = -1;
            ++index;
        }

        int res = 0;
        while (index < len){
            char curChar = s[index];
            if (curChar < '0' || curChar > '9'){
                break;
            }
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && (curChar - '0') > INT_MAX % 10)) {
                return INT_MAX;
            }
            if (res < INT_MIN / 10 || (res == INT_MIN / 10 && (curChar - '0') > -(INT_MIN % 10))) {
                return INT_MIN;
            }
            res = res * 10 + sign * (curChar - '0');
            index++;
        }
        return res;
    }
};