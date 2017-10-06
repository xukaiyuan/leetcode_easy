package quickSort;

public class quickSort {
	
	public  static void Sort(int [] arr,int start, int end)
	{
		if(start < end)
		{
		
		int flag = arr[start];
		int i = start;
		for(int j = start + 1; j <= end; j++)
		{
			
			if(arr[j] < flag)
			{				
					int tmp = arr[j];
					arr[j] = arr[i+1];
					arr[i+1] = tmp;
				
				i++;
			}
		}
		
		arr[start] = arr[i];
		arr[i] = flag;
		
		Sort(arr, start, i - 1);
		Sort(arr, i + 1, end);
		
	}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] x = new int []{5,4,3,9,6,7,1,2};
		Sort(x, 0, x.length - 1);
		for(int i = 0; i < x.length; i++)	
		{
			System.out.println(x[i]);
		}
		

	}

}
