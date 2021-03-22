package simulation;
import java.util.*;

//graphics tools
//import java.awt.Canvas;
//import java.awt.Graphics;
//
//import javax.swing.JFrame;

public class SimulationLauncher  /*extends Canvas */
{
	/**
	 * 
	 */
//	private static final long serialVersionUID = 1L; //it just recommended me to add this
//	public static final int SIZE_ATOM = 0;
	public static final int SIZE_X = 1000;
	public static final int SIZE_Y = 1000;
	public static final double TIME = 999;
	public static final int NUM_ATOMS = 1;
	public static final int AVERAGE_SPEED = 75;

	public static void main(String[] args) 
	{

		
		
		
		//the following code will implement graphics for the simulation. 
//        JFrame frame = new JFrame("My Drawing");
//        Canvas canvas = new SimulationLauncher();
//        canvas.setSize(400, 400);
//        frame.add(canvas);
//        frame.pack();
//        frame.setVisible(true);
        // done
		
//		double xMag = 37;
//		double yMag = 76;
		double xPos = Math.random()*SIZE_X ;
		double yPos = 50;
//		If i want to extend it to many atoms are in the simulation, I need to implement randomness.

		double n = Math.random()*Math.PI*2; //gets angle between 0 and 2pi
		double xMag = Math.cos(n)*AVERAGE_SPEED;
		double yMag = Math.sin(n)*AVERAGE_SPEED; // now both are scaled appropriately
		double currentTime = 0;
		
		Coordinates c = new Coordinates (xPos, yPos);
		Atom a = new Atom(new Vector(xMag, yMag, c));
	
		while (currentTime < TIME)
		{
//			paint(g);
			double[] arr = new double[4];
			arr[0] = collisionLeftWall(a);
			arr[1] = collisionTopWall(a);
			arr[2] = collisionRightWall(a);
			arr[3] = collisionBottomWall(a);
			int pos = findLeast(arr);
			update(a, arr, pos);
			currentTime = currentTime + arr[pos];
			print (a);
		}
	
		// TODO Auto-generated method stub

	}
//	
//    public void paint(Graphics g) {
//        g.fillOval(100, 100, 200, 200);
//    }
	public static void update(Atom a, double[] arr, int pos)
	{

		if (pos%2 == 0) 
		{
//			going to hit the right or left wall
			double newXPos;
			double newYPos = a.getVector().getTail().getY() + arr[pos]*a.getVector().getYMag();
			
			
//			shouldn't it just be the same but in the other direction?
			
			if (pos == 0)
			{
//				collision with the left wall
				newXPos = a.getSize();
			}
			else
			{
				newXPos = SIZE_X - a.getSize();
			}
			a.setVector(new Vector(
					-a.getVector().getXMag(), 
					a.getVector().getYMag(), 
					new Coordinates(newXPos, newYPos))); // sets the vector in opposite direction
//			going to hit the right or the left 
			return;
		}
		double newY;
		if (pos == 3)
		{
			
			newY = a.getSize();
		}
		else
		{
			newY = SIZE_Y - a.getSize();
		}
		double newX = a.getVector().getTail().getX() + arr[pos]*a.getVector().getXMag();

		a.setVector(
				new Vector(a.getVector().getXMag(), 
				-a.getVector().getYMag(), 
				new Coordinates(newX, newY)));
		
		return;
	}
	
	public static double collisionLeftWall(Atom a)
	{
		return (-a.getVector().getTail().getX() + a.getSize())/ a.getVector().getXMag();
	}
	public static double collisionTopWall(Atom a)
	{
		return (SIZE_Y - a.getVector().getTail().getY() - a.getSize())/ a.getVector().getYMag();
	}
	public static double collisionRightWall(Atom a)
	{
		return (SIZE_X - a.getVector().getTail().getX() - a.getSize())/ a.getVector().getXMag();
	}
	public static double collisionBottomWall(Atom a)
	{
		return (-a.getVector().getTail().getY() + a.getSize()) / a.getVector().getYMag();
	} 
	public static int findLeast(double [] arr)
	{
		int smallestPos = 0;
		if (arr[smallestPos] <= 0)
		{
			smallestPos = 2;
//			ensures that it starts with a positive number
		}
		
		for (int i = 0; i < arr.length; i++) 
		{
			if (arr[i] > 0 && arr[i] < arr[smallestPos])
			{
				smallestPos = i;
			}
		}
		return smallestPos;
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
	public static void print (Atom a)
	{
		System.out.println(a);
	}
	public static void print (String s)
	{
		System.out.println(s);
	}
	public static void print (int i)
	{
		System.out.println(i);
	}
}
