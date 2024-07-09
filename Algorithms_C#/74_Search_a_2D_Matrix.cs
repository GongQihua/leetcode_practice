public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int m = matrix.Length, n = matrix[0].Length;
        int left = 0, right = m * n - 1;
        while (left < right){
            int mid = (left + right) >> 1;
            int x = mid / n, y = mid % n;
            if (matrix[x][y] >= target){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return matrix[left / n][left % n] == target;
    }
}