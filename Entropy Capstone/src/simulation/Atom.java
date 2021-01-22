/**
 * 
 */
package simulation;

/**
 * @author trentconley
 *
 */
//This is the class where I will design the attributes of each atom, and keep track of their

//position while they move in the simulation. I'm also using the snake style because I'm used

//to writing in python. 

public class Atom 

{

	private double xpos;

	private double ypos;

	private double magnitude;

	private double theta;

//	private double size = 0; I will ignore the size of the atom for now because the math will

//	get really hard if I consider the atom as a sphere, I eventually will though. 



//	This is a constructor that will initiate all of the class scope variables.

	public Atom (double xposin, double yposin, double magnitudein, double thetain)

	{	

		xpos = xposin;

		ypos = yposin;

		magnitude = magnitudein;

		theta = thetain;

			

	}

	

//	This method will return the collision time of the atom to a line

//	the line will be in the form y = m * x + b

//	I am just calculating the intersection point of two lines.



	public double collision_line(double m1, double b1)

	{

//		2 at the end of the letter refers to the atom, 1 refers to the boundary line

//		this function will be useful when computing the collisions between spheres I think.

		double m2 = magnitude * Math.tan(theta); 

		double b2 = m2 * (-xpos) + ypos;

		double a = 0;

		double xcolpos = (b2-b1)/(m1-m2);

		double ycolpos = m1 * xcolpos + b1;

		return 0;

/*		y = m * x + b

*		y  = m (x - x1)+ y1

*		y = m2 (-x2) + y2 because the x value is 0 on the y intercept and this is equal to b2

*		and if we have the mx+b form for the other, we can set them equal to each other

* 

*/

	}

//	for vertical or horizontal lines

	public double collision_line(boolean vert_horiz, double x,  double y)

	{

		if (vert_horiz)

		{

//			This will assume that the user inputs the double x as the 

//			slope and the double y as the y intercept

			return collision_line(x, y);

		}

		if (x == -1)

		{

			if (Math.cos(theta) < 0)

			{

				return -1;

	//			the negative 1 will mean that it will never happen, and such will be interpreted in

	//			the program. a cosine equaling 0 will result in an undefined function. 

			}

//			 we are returning the time time until collision, also all the particles will be 

//			inside the box

			return (x-xpos) / (magnitude * Math.cos(theta));

		}

		return (y - ypos)/ (magnitude * Math.sin(theta)); // numerator is distance to travel,

		//Denominator is the rate at which it is changing, thereby giving the seconds until

		//collision



	}

	

	

//	These four methods will allow the me to get all of the class scope variables.

	public double get_xpos()

	{

		return xpos;

	}

	

	public double get_ypos()

	{

		return ypos;

	}

	

	public double get_magnitude()

	{

		return magnitude;

	}

	

	public double get_theta()

	{

		return theta;

	}

	

//	These following four methods will allow me to set the values of the class scope variables

	public void set_xpos(double xposin)

	{

		xpos = xposin;

	}

	

	public void set_ypos(double yposin)

	{
		ypos = yposin;
	}

	

	public void set_magnitude(double magnitudein)

	{
		magnitude = magnitudein;
	}

	

	public void set_theta(double thetain)

	{
		theta = thetain;
	}



//	Always include a toString method even if it's boring!

	public String toString()

	{

		return "x pos = " + Double.toString(xpos) + ", y pos = " + Double.toString(ypos) + 

				", magnitude = " + Double.toString(magnitude) + ", theta = " + Double.toString(theta);

	}

}