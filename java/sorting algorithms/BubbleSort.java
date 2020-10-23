import java.util.*;

public class BubbleSort {

	public static void main(String[] args) {


		int a[];
		
		System.out.println("Enter number of elements in array:-");
        n = sc.nextInt();
        arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            System.out.println("Enter element "+i);
            arr[i]= sc.nextInt();
        }
		
		for(int i = 0; i < n-1; i++) {
			
			boolean sorted = true;
			
			for (int j = 0; j < n-1-i; j++) {
				
				if(a[j+1] < a[j]) {
					int temp = a[j+1];
					a[j+1] = a[j];
					a[j] = temp;
					
					sorted = false;
				}
				
			}
			if(sorted) break;
			
		}
		
		for(int item: a) {
			System.out.print(item+" ");
		}
		

	}

}