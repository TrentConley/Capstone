package testCodePackage;
import java.util.*;

public class Launcher 
{
	public static double AVERAGE_SPEED = 1;
	public static void main(String[] args) 
	{
//		list d = {};
		HashMap<String, Double> h = new HashMap<String, Double>(4);
		fill(h);
		print(h);
		
		// TODO Auto-generated method stub

	}
	public static void fill(HashMap<String, Double> h)
	{
		h.put("yeet", 0.0);
	}
	
	public static void print (double[] arr)
	{
		for (int i = 0; i < arr.length; i ++)
		{
			print(arr[i]);
		}
	}
	public static void print(double d)
	{
		System.out.println(d);
	}
	public static void print (String s)
	{
		System.out.println(s);
	}
	public static void print (int i)
	{
		System.out.println(i);
	}
	public static void print (HashMap h)
	{
		System.out.println(h);
	}

	/*
	 * the following spaces will be dedicated to finding a better approach to storing the time until
	 * collision. I think there needs to be some sort of dictionary that stores when the time until
	 * collision with the walls are stored as the first three elements. Also, we can't build a new 
	 * dictionary every time so they need to be mutable. I'll have to look that up to see how that 
	 * mechanism works. Alternatively, I could just store one dictionary with the wall time until 
	 * collisions then store another array YES! array, of sorted atoms of time until collisions. 
	 * hmm, should I sort the array or not? Sorting the array would take O(n*log(n)) time, but not 
	 * sorting the array will increase the finding time of the least element from O(log(n)) to O(n).
	 * I think the best best will just be to not sort the array. I can optimize it from there.  
	 * 
	 * 
	 * Ok, now I just have to figure out how dictionaries work in java. 
	 * 
	 * 
	 * 
	 * 
	 * 
	 * 
	 * 
	 * 
	 * 
	 */
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
