
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int minus[];
    	minus = new int[nums.length];
    	int indice[];
        indice = new int[2];
        int count = 0;
        for(int i = 0;i < nums.length;i++)
        {
            minus[i] = target - nums[i];
        }
        
        for(int i = 0;i < nums.length;i++)
        {
            if(count == 2) break;
            for(int j = 0;j < nums.length;j++)
            {
                if(i == j) continue;
                if(minus[i] == nums[j]) 
                {
                    count++;
                    if(count == 1) indice[0] = i;
                    if(count == 2) indice[1] = i;
                }
                
            }
        }
        return indice;
    }
    
    public static void main(String args[]){
    	int [] test = {3,2,4};
    	int target = 6;
    	Solution s = new Solution();
    	
    	int result[];
    	result = s.twoSum(test, target);
    	System.out.println("[" + result[0] + "," + result[1] + "]");
    	return;
    	
    } 

}
