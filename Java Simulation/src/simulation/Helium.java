package simulation;
import java.math.*;

public class Helium extends Atom
{
//	mass is in au.
//	232.47E-27 in kilograms
//	1.6605e-27 is the conversion for 1 amu to kilograms. 
	public static final double MASS = 4.002602;
	
//	radius is in pm, but since the velocity will be in meters, we might need to make it
//	into a bigdecimal because a double only has 15 digits whereas i need 18. 

//	when using the radius, we will need to do conversions 
	public static final double RADIUS = 140;
	
	public Helium(Coordinates cIn, Vector vIn) 
	{
		super(cIn, vIn, RADIUS, MASS);
		// TODO Auto-generated constructor stub
	}

}
