#------------------------------prevSmallest-----------------------------------------------

class Solution {
    public int[] prevSmallest(int[]heights)
    {
        int n=heights.length;
        
         Stack<Integer>stack = new Stack<>();
         int [] ans = new int[n];
       
         for(int i=0;i<n;i++)
         {
          while(!stack.isEmpty() && heights[stack.peek()]>=heights[i]) 
          {
            stack.pop();
          }
           if (stack.isEmpty()) {
                ans[i] = -1;
            } else {
              
                ans[i] = stack.peek();
            }
            
            stack.push(i);
         }
         
         return ans;
    }

#----------------------------------NextSmallest----------------------------------------------------


    public int[] NextSmallest(int[]heights)
    {
        int n=heights.length;
       
         Stack<Integer>stack = new Stack<>();
         int [] ans = new int[n];
       
         for(int i=n-1;i>=0;i--)
         {
          while(!stack.isEmpty() && heights[stack.peek()]>=heights[i]) 
          {
            stack.pop();
          }
            if (stack.isEmpty()) {
                ans[i] = n;
            } else {
               
                ans[i] = stack.peek();
            }
           
            stack.push(i);
         }
         return ans;
    }


#----------------------------------------------largestRectangleArea----------------------------


    public int largestRectangleArea(int[] heights) {
        int[] prev=prevSmallest(heights);
        int[] next=NextSmallest(heights);
        int n=heights.length;
        int ans=0;
        
        for(int i=0;i<n;i++)
        {
         ans=Math.max(ans,(next[i]-prev[i]-1)*heights[i]);
        }
        return ans;
    }
}
