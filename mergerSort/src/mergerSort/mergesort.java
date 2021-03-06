package mergerSort;

public class mergesort {

	public static void mergesort(int [] nums)
	{
		int [] tmp = new int[nums.length];
		sort(nums, tmp, 0, nums.length - 1);
	}
	private static void sort(int [] nums, int [] tmp, int start, int end)
	{
		if(start >= end) return;
		int mid = (end - start) / 2 + start;
		sort(nums, tmp, start, mid);
		sort(nums, tmp, mid + 1, end);
		merge(nums, tmp, start, mid, end);
	}
	private static void merge(int [] nums, int [] tmp, int start, int mid, int end)
	{
		int leftEnd = mid;
		int rightStart = mid + 1;
		int num = end - start + 1;
		int tmpN = start;
		
		while(start <= leftEnd && rightStart <= end)
		{
			if(nums[start] <= nums[rightStart])
			{
				tmp[tmpN++] = nums[start++];
			}
			else
			{
				tmp[tmpN++] = nums[rightStart++];
			}
		}
		while(start <= leftEnd)
			tmp[tmpN++] = nums[start++];
		while(rightStart <= end)
			tmp[tmpN++] = nums[rightStart++];
		for(int i = 0; i < num; i++, end--)
		{
			nums[end] = tmp[end];
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] nums = {8,4,13,7,10,29,1};
		mergesort(nums);
		for(int i = 0; i < nums.length; i++)
		{
			System.out.println(nums[i]);
		}
		

	}

}
