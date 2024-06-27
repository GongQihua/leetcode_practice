class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int dir[5] = {0, 1, 0, -1, 0};
        vector<int> ans;
        int i = 0, j = 0, k = 0;
        for (int h = m * n; h; --h){
            ans.push_back(matrix[i][j]);
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
};