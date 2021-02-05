package simulation;

public class Helium extends Atom
{
	private static final double MASS = 0;
	private static final double RADIUS = 0;
	
	public Helium(Coordinates cIn, Vector vIn) 
	{
		super(cIn, vIn);
		// TODO Auto-generated constructor stub
	}
	
//	I don't think that I need to get the stuff from above because the program will look up
	
	public double getMass()
	{
		return MASS;
	}
	
	public double getRadius()
	{
		return RADIUS;
	}

}
