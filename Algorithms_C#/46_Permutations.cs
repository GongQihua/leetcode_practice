public class Solution {
    IList<IList<int>> permutations = new List<IList<int>>();
    IList<int> temp = new List<int>();
    int n;

    public IList<IList<int>> Permute(int[] nums) {
        foreach (int num in nums){
            temp.Add(num);
        }
        n = nums.Length;
        dfs(0);
        return permutations;
    }

    public void dfs(int index){
        if (index == n){
            permutations.Add(new List<int>(temp));
        }
        else{
            for (int i = index; i < n; ++i){
                Swap(temp, index, i);
                dfs(index + 1);
                Swap(temp, index, i);
            }
        }
    }

    public void Swap(IList<int> temp, int index1, int index2) {
        int curr = temp[index1];
        temp[index1] = temp[index2];
        temp[index2] = curr;
    }
}