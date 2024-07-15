public class Solution {
    public int LargestRectangleArea(int[] heights) {
        Stack<int> stk = new Stack<int>();
        int i = 0, result = 0;
        while(i < heights.Length || stk.Any()){
            if(!stk.Any() || (i < heights.Length && heights[stk.Peek()] < heights[i])){
                stk.Push(i);
                ++i;
            }
            else{
                var previousIndex = stk.Pop();
                var area = heights[previousIndex] * (stk.Any() ? (i - stk.Peek() - 1) : i);
                result = Math.Max(result, area);
            }
        }
        return result;
    }
}