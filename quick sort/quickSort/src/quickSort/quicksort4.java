package quickSort;

public class quicksort4 {
	public static void Sort4(int[] nums, int start, int end)
	{
		if(start < end)
		{
			int i = start;
			int base = nums[start];
			for(int j = i + 1;j < nums.length; j++)
			{
				if(nums[j] <= base)
				{
					int tmp = nums[i + 1];
					nums[i + 1] = nums[j];
					nums[j] = tmp;
					i++;
				}
				
			}
			nums[start] = nums[i];
			nums[i] = base;
			
			Sort4(nums, start, i - 1);
			Sort4(nums, i + 1, end);
			
			
		}
	}

	public static void main(String[] args) {

		// TODO Auto-generated method stub
		
		int[] x = new int []{5,4,3,9,6,7,1,2};
		Sort4(x, 0, x.length - 1);
		for(int i = 0; i < x.length; i++)	
		{
			System.out.println(x[i]);
		}

	}

}
