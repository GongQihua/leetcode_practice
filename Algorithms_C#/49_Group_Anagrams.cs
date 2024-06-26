public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        IDictionary<string, IList<string>> dictionary = new Dictionary<string, IList<string>>();
        foreach (string str in strs){
            char[] array = str.ToCharArray();
            Array.Sort(array);
            string key = new string(array);
            dictionary.TryAdd(key, new List<string>());
            dictionary[key].Add(str);
        }
        return new List<IList<string>>(dictionary.Values);
    }
}