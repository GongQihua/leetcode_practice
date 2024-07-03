public class Solution {
    public int[] PlusOne(int[] digits) {
        int n = digits.Length;
        for (int i = n-1; i >= 0; --i){
            digits[i] += 1;
            digits[i] %= 10;
            if (digits[i] != 0){
                return digits;
            }
        }
        digits = new int[n + 1];
        digits[0] = 1;
        return digits;
    }
}