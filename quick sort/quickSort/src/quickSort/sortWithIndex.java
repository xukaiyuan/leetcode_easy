package quickSort;

public class sortWithIndex {
	public static void sortWithIndex(int[] nums, int[] index, int start, int end)
    {
        if(start < end)
        {
            int flag = nums[start];
            int i = start;
            for(int j = start + 1; j <= end; j++)
            {
                if(nums[j] > flag)
                {
                    int tmp = nums[j];
                    nums[j] = nums[i+ 1];
                    nums[i + 1] = tmp;
                    
                    int indexTmp = index[j];
                    index[j] = index[i + 1];
                    index[i + 1] = indexTmp;
                    
                    i++;
                }
                
            }
            nums[start] = nums[i];
            nums[i] = flag;
            int itmp = index[start];
            index[start] = index[i];
            index[i] = itmp;
            
            sortWithIndex(nums, index, start, i - 1);
            sortWithIndex(nums, index, i + 1, end);
        }
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {1,3,2,5,4};
		int[] index = new int[nums.length];
        for(int i = 0; i < nums.length; i++)
        {
            index[i] = i;
        }
        sortWithIndex(nums, index, 0, nums.length - 1);
        
        for(int i = 0; i < nums.length; i++)	
		{
			System.out.println(nums[i]);
		}
        
        for(int i = 0; i < index.length; i++)	
		{
			System.out.println(index[i]);
		}

	}

}
