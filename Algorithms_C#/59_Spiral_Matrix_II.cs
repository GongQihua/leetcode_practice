public class Solution {
    public int[][] GenerateMatrix(int n) {
        int[][] ans = new int[n][];
        for (int a = 0; a < n; ++a){
            ans[a] = new int[n];
        }
        int[][] dirs = {new int[]{0, 1}, new int[]{1, 0}, new int[]{0, -1}, new int[]{-1, 0}};
        int i = 0, j = 0, k = 0;
        for (int v = 1; v <= n * n; ++v){
            ans[i][j] = v;
            int x = i + dirs[k][0], y = j + dirs[k][1];
            if (x < 0 || y < 0 || x >= n || y >= n || ans[x][y] != 0){
                k = (k + 1) % 4;
                x = i + dirs[k][0];
                y = j + dirs[k][1];
            }
            i = x;
            j = y;
        }
        return ans;
    }
}