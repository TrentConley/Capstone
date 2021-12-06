package simulation;
import java.math.*;
public class Argon extends Atom
{

//	mass is in au.
	public static final double MASS = 39.948;
	
//	radius is in pm
	public static final double RADIUS = 188;
	
	public Argon(Vector vIn) 
	{
		super(vIn, RADIUS, MASS);
		// TODO Auto-generated constructor stub
	}
	
	public BigDecimal timeUntilCollision(Atom a)
	{
		return new BigDecimal ("-1");
	}
	 

}
