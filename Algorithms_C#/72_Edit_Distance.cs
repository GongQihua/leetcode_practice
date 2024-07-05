public class Solution {
    public int MinDistance(string word1, string word2) {
        int m = word1.Length, n = word2.Length;
        int[,] f = new int[m+1, n+1];
        for (int j = 0; j <= n; ++j){
            f[0, j] = j;
        }
        for (int i = 1; i <= m; ++i){
            f[i, 0] = i;
            for (int j = 1; j <= n; ++j){
                if (word1[i-1] == word2[j-1]){
                    f[i, j] = f[i-1, j-1];
                }
                else{
                    f[i, j] = Math.Min(f[i-1, j], Math.Min(f[i, j-1], f[i-1, j-1])) + 1;
                }
            }
        }
        return f[m, n];
    }
}