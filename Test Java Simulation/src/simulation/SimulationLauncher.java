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
	public static final int NUM_ATOMS = 2;
	public static final int AVERAGE_SPEED = 75; // must be above one

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
		double currentTime = 0;
		
		
		Atom[] atomArr = generateAtoms(NUM_ATOMS);
		
	
		while (currentTime < TIME)
		{
			HashMap<Atom, Double> collisionsWall = makeHashMapWall(atomArr);
			
//			paint(g);
			
			double timeCollision = findleastCollectiveAtoms(collisionsWall);
			update(timeCollision, atomArr, collisionsWall);
			currentTime = currentTime + timeCollision;
			print (atomArr);
		}
	
		// TODO Auto-generated method stub

	}
	
	public static Atom[] generateAtoms(int numAtoms)
	{
		Atom[] atomArr = new Atom[numAtoms];
		for (int i = 0; i < numAtoms; i++)
		{
			double xPos = Math.random()*SIZE_X;
			double yPos = Math.random()*SIZE_Y;
//			If i want to extend it to many atoms are in the simulation, I need to implement randomness.

			double n = Math.random()*Math.PI*2; //gets angle between 0 and 2pi
			double xMag = Math.cos(n)*AVERAGE_SPEED;
			double yMag = Math.sin(n)*AVERAGE_SPEED; // now both are scaled appropriately

			

			Coordinates c = new Coordinates (xPos, yPos);
			Atom a = new Atom(new Vector(xMag, yMag, c));
			atomArr[i] = a;
		}
		
		return atomArr;
	}
	
	public static HashMap<Atom, Double> makeHashMapWall(Atom[] atoms)
	{           
		double shortest = SIZE_X + SIZE_Y; //because speed will be above 1, this will be longer than any other distance time. 
		HashMap<Atom, Double> h = new HashMap<Atom, Double>(); //hashmap with each atom and their respective shortest times until collision.
		for (Atom a : atoms)
		{
			HashMap<String, Double> times = new HashMap<String, Double>();
			times.put("left", collisionLeftWall(a));
			times.put("right", collisionRightWall(a));
			times.put("top", collisionTopWall(a));
			times.put("base", collisionBaseWall(a));
			String side = findLeastIndivitualAtom(times);
			a.setCloseWall(side);
			h.put(a, times.get(side));
			if (times.get(side) < shortest)
			{
				shortest = times.get(side);
			}
		}
		return h;
	}
	
	public static double findleastCollectiveAtoms(HashMap<Atom, Double> h)
	{

		double shortestTime = SIZE_X + SIZE_Y; //dangerous setting it to 0
		for (Map.Entry<Atom, Double> entry : h.entrySet())
		{
			if (shortestTime > entry.getValue())
			{
				shortestTime = entry.getValue();
			}
		}
		return shortestTime;
	}
	
	// finds the shortest path to collision with particular wall. 
	public static String findLeastIndivitualAtom(HashMap<String, Double> h)
	{
//		returns the atom with the smallest time until collision with any wall
		String smallestKey = "left";
		if (h.get(smallestKey) <= 0)
		{
			smallestKey = "right";
//			ensures that it starts with a positive number
//			if it has already hit left, it will not have hit the right. 
		}
		for (Map.Entry<String,Double> entry : h.entrySet()) 
		{
//            System.out.println("Key = " + entry.getKey() +
//                             ", Value = " + entry.getValue());
			if (entry.getValue() > 0 && entry.getValue() < h.get(smallestKey))
			{
				smallestKey = entry.getKey();
			}
		}
		return smallestKey;
	}

//	
//    public void paint(Graphics g) {
//        g.fillOval(100, 100, 200, 200);
//    }
	public static void update(double timeElapsed, Atom[] arr, HashMap<Atom, Double> h)
	{
		double newXPos;
		double newYPos;
		for (Atom a : arr)
		{
			if (h.get(a) == timeElapsed)
			{ //collision case atom
				if (a.getCloseWall().equals("left"))
				{
					newYPos = a.getVector().getTail().getY() + timeElapsed*a.getVector().getYMag();
					newXPos = a.getSize();
					a.setVector(new Vector(
							-a.getVector().getXMag(), 
							a.getVector().getYMag(), 
							new Coordinates(newXPos, newYPos))); // sets the vector in opposite direction
				}
				else if (a.getCloseWall().equals("right"))
				{
					newYPos = a.getVector().getTail().getY() + timeElapsed*a.getVector().getYMag();
					newXPos = SIZE_X - a.getSize();
					a.setVector(new Vector(
							-a.getVector().getXMag(), 
							a.getVector().getYMag(), 
							new Coordinates(newXPos, newYPos))); // sets the vector in opposite direction
				}
				else if (a.getCloseWall().equals("base"))
				{
					newYPos = a.getSize();
					newXPos = a.getVector().getTail().getX() + timeElapsed*a.getVector().getXMag();
					a.setVector(
							new Vector(a.getVector().getXMag(), 
							-a.getVector().getYMag(), 
							new Coordinates(newXPos, newYPos)));
				}
				else if (a.getCloseWall().equals("top"))
				{
					newYPos = SIZE_Y - a.getSize();
					newXPos = a.getVector().getTail().getX() + timeElapsed*a.getVector().getXMag();
					a.setVector(
							new Vector(a.getVector().getXMag(), 
							-a.getVector().getYMag(), 
							new Coordinates(newXPos, newYPos)));
				}
				else
				{
					print("Houston we've got a problem");
					
				}	
						
			}
			else
			{
				//for all other atoms
				newXPos = a.getVector().getTail().getX() + timeElapsed*a.getVector().getXMag();
				newYPos = a.getVector().getTail().getY() + timeElapsed*a.getVector().getYMag();
				a.setVector(new Vector(
						a.getVector().getXMag(),
						a.getVector().getYMag(),
						new Coordinates (newXPos, newYPos)));
			}
		}

	}
	
	//these are times until collision with walls
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
	public static double collisionBaseWall(Atom a)
	{
		return (-a.getVector().getTail().getY() + a.getSize()) / a.getVector().getYMag();
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
	public static void print(Atom[] arr)
	{
		for (int i =0; i < arr.length; i ++)
		{
			print("This is atom number " + Integer.toString(i));
			print(arr[i]);
		}
	}
}
