public class Solution {
    public int[][] Merge(int[][] intervals) {
        intervals = intervals.OrderBy(a => a[0]).ToArray();
        IList<int[]> ans = new List<int[]>();
        ans.Add(intervals[0]);
        for (int i = 0; i < intervals.Length; ++i){
            if (ans[ans.Count - 1][1] < intervals[i][0]){
                ans.Add(intervals[i]);
            }
            else{
                ans[ans.Count - 1][1] = Math.Max(ans[ans.Count - 1][1], intervals[i][1]);
            }
        }
        return ans.ToArray();
    }
}