package simulation;
import java.math.*;

/**
 * @author trentconley
 *
 */
//This is the class where I will design the attributes of each atom, and keep track of their
//position while they move in the simulation. 

public abstract class Atom 
{
	private Coordinates c;
	private Vector v;
	private final double radius;
	private final double mass;

//	private double size = 0; I will ignore the size of the atom for now because the math will
//	get really hard if I consider the atom as a sphere, I eventually will though. 
//	This is a constructor that will initiate all of the class scope variables.
	public Atom (Coordinates cIn, Vector vIn, double radiusIn, double massIn)
	{	
//		creating copy will prevent errors from mixing addresses in the heap. 
		Coordinates copyC = new Coordinates(cIn.getX(), cIn.getY());
		this.c = copyC;
		Vector copyV = new Vector(vIn.getMagnitude(), vIn.getTheta());
		this.v = copyV;
		this.radius = radiusIn;
		this.mass = massIn;
	}

	/*
	public void make_relative(Atom mov, Atom stat)
	{
//		going to make one atom stationary relative to the other. 
		return;
	}
	*/
	public double getRadius()
	{
		return this.radius;
	}
	
	public double getMass()
	{
		return this.mass;
	}
	
	public BigDecimal timeUntilCollision(MathContext mc, Atom a)
	{
		BigDecimal next = new BigDecimal ("0");
		
		
		
		
		return next;
	}

	
	

//	These four methods will allow the me to get all of the class scope variables.
	public Coordinates getCoordinates()
	{
		Coordinates copyC = new Coordinates(c.getX(), c.getY());
		return copyC;
	}
	

	public Vector getVector()
	{
		return new Vector(this.v.getMagnitude(), this.v.getTheta());
	
	}

//	These following four methods will allow me to set the values of the class scope variables

	public void setCoordinates(Coordinates cIn)
	{
		
//		Setting something equivalent to an address that you are using in the heap can cause 
//		errors later on in the future, but I will leave it for now. 
		this.c = new Coordinates(cIn.getX(), cIn.getY());
	}
	
	
	public void setVector(Vector vIn)
	{
		
		this.v = new Vector(vIn.getMagnitude(), vIn.getTheta());
	}

//	Always include a toString method even if it's boring!

	public String toString()
	{
		return "Coordinates Information: " + this.c.toString() + "\n" +
				"Vector Information: " + this.v.toString() + "\n";
		
	}
}