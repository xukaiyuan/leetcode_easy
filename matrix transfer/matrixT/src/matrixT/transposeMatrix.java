package matrixT;

public class transposeMatrix {

	
	
	public static void Transpose(double [][]Matrix,int Line,int List,double[][]MatrixC){  
		  for(int i=0;i<Line;i++)  
		  {  
		      for(int j=0;j<List;j++)  
		      {  
		          MatrixC[j][i]=Matrix[i][j];  
		      }  
		  }  
		}  
		public static void main(String[]args)//测试  
		{  
		    double[][] TestMatrix = {  
		               {1, 22, 34,22},   
		  
		               {1, 11,5,21} ,  
		                
		               {7,2,13,19}};      
		    double[][] TMatrix1={  
		            {1,2,3},{2,1,1},{2,2,2}   
		    };  
		    double[][]TMatrix2={  
		            {1,2},{2,3}   
		    };  
		    double[][] MatrixC=new double[4][3];  
		    Transpose(TestMatrix,3,4,MatrixC);  
		    String Strr=new String("");  
		    for(int i=0;i<4;i++)  
		    {  
		        for(int j=0;j<3;j++)  
		        {  
		            String str=String.valueOf(MatrixC[i][j]);//  
		            Strr+=str;  
		            Strr+=" ";  
		        }  
		          
		          
		        Strr+="\n";  
		      
		    }  
		      
		      
		   System.out.println(Strr);  
		      
		}  
		}  


