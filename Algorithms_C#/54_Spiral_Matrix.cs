public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;
        int[] dir = new int[] {0, 1, 0, -1, 0};
        IList<int> ans = new List<int>();
        int i = 0, j = 0, k = 0;
        for (int h = m * n; h > 0; --h){
            ans.Add(matrix[i][j]);
            matrix[i][j] += 300;
            int x = i + dir[k], y = j + dir[k+1];
            if (x<0 || x>=m || y<0 || y >=n || matrix[x][y]>100){
                k = (k+1) % 4;
            }
            i += dir[k];
            j += dir[k+1];
        }
        return ans;
    }
}