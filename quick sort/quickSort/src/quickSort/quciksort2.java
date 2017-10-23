package quickSort;

public class quciksort2 {
	public static void Sort2(int [] nums, int left, int right)
	{
		
		if(left < right)
		{
			int tmp = nums[left];
			int i = left;
			for(int j = left + 1; j < right + 1; j++)
			{
				if(nums[j] < tmp)
				{
					int x = nums[i + 1];
					nums[i + 1] = nums[j];
					nums[j] = x;
					i++;
				}
			}
			nums[left] = nums[i];
			nums[i] = tmp;
			
			Sort2(nums, left, i - 1);
			Sort2(nums, i + 1, right);
		}
		
	}

	public static void main(String[] args) {

		// TODO Auto-generated method stub
		
		int[] x = new int []{5,4,3,9,6,7,1,2};
		Sort2(x, 0, x.length - 1);
		for(int i = 0; i < x.length; i++)	
		{
			System.out.println(x[i]);
		}
		

		// TODO Auto-generated method stub

	}

}