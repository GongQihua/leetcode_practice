public class Solution {
    public string MinWindow(string s, string t) {
        int[] need = new int[128];
        int[] window = new int[128];
        int m = s.Length, n = t.Length;
        foreach (int c in t){
            ++need[c];
        }
        int cnt = 0, j = 0, k = -1, mi = 1 << 30;
        for (int i = 0; i < m; ++i){
            ++window[s[i]];
            if (need[s[i]] >= window[s[i]]){
                ++cnt;
            }
            while (cnt == n){
                if (i - j + 1 < mi){
                    mi = i -j + 1;
                    k = j;
                }
                if (need[s[j]] >= window[s[j]]){
                    --cnt;
                }
                --window[s[j++]];
            }
        }
        return k < 0 ? "" : s.Substring(k, mi);
    }
}