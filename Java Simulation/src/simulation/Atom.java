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
//	The vector has a tail, thus it keeps track of the atom's location. 
	private Vector v;
	private final double radius;
	private final double mass;

//	private double size = 0; I will ignore the size of the atom for now because the math will
//	get really hard if I consider the atom as a sphere, I eventually will though. 
//	This is a constructor that will initiate all of the class scope variables.
	public Atom (Vector vIn, double radiusIn, double massIn)
	{	
//		creating copy will prevent errors from mixing addresses in the heap. 
		this.v = new Vector(vIn.getXMag(), vIn.getYMag(), vIn.getTail());
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
	
	public Vector getVector()
	{
		// used whitespace to make code clearer. 
		return new Vector(
				this.v.getXMag(), 
				this.v.getYMag(), 
				new Coordinates (
						this.v.getTail().getX(), 
						this.v.getTail().getY()
						)
				);
	
	}
	
	public void setVector(Vector vIn)
	{
//		creates new vector, sets at this vector
		this.v = new Vector(
				vIn.getXMag(), 
				vIn.getYMag(),
				new Coordinates (
						vIn.getTail().getX(),
						vIn.getTail().getY()
						)
				);
	}

//	Always include a toString method even if it's boring!

	public String toString()
	{
		return "Vector Information: " + this.v.toString() + "\n";
		
	}

	public void update(BigDecimal t, MathContext mc) 
	{
		this.v.update(t, mc);
		// TODO Auto-generated method stub
		
	}
}