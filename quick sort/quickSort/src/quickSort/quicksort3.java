package quickSort;

public class quicksort3 {
	public static void Sort3(int [] nums, int start, int end)
	{
		if(start < end)
		{
			int i = start;
			int base = nums[i];
				for(int j = i + 1; j < nums.length; j++)
				{
					if(nums[j] < base)
					{
						int tmp = nums[i + 1];
						nums[i + 1] = nums[j];
						nums[j] = tmp;
						i++;
					}
				}
				int tmp = nums[i];
				nums[i] = nums[start];
				nums[start] = tmp;
				
				Sort3(nums, start, i  - 1);
				Sort3(nums,i + 1, end);
				
			
			
		}
	}

	public static void main(String[] args) {

		// TODO Auto-generated method stub
		
		int[] x = new int []{5,4,3,9,6,7,1,2};
		Sort3(x, 0, x.length - 1);
		for(int i = 0; i < x.length; i++)	
		{
			System.out.println(x[i]);
		}
		

	}

}
