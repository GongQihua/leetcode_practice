public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        IList<int[]> ans = new List<int[]>();
        int st = newInterval[0], ed = newInterval[1];
        bool insert = false;
        foreach (var interval in intervals){
            int s = interval[0], e = interval[1];
            if (ed < s){
                if (!insert){
                    ans.Add(new int[]{st, ed});
                    insert = true;
                }
                ans.Add(interval);
            }
            else if(e < st){
                ans.Add(interval);
            }
            else{
                st = Math.Min(s, st);
                ed = Math.Max(ed, e);
            }
        }
        if (!insert){
            ans.Add(new int[]{st, ed});
        }
        return ans.ToArray();
    }
}