public class Solution {
    public double MyPow(double x, int n) {
        long N = n;
        return N >= 0 ? quickMul(x, N) : 1.0 / quickMul(x, -N);
    }
    private double quickMul(double x, long N){
        double ans = 1.0;
        double x_contribute = x;
        while (N > 0){
            if (N % 2 == 1){
                ans *= x_contribute;
            }
            x_contribute *= x_contribute;
            N >>= 1;
        }
        return ans;
    }
}