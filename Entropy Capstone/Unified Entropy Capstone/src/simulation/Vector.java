package simulation;

// This class will store everything related to lines, and manipulations. 
public class Vector 
{
	private double magnitude;
	private double theta;
	
	public Vector (double magnitudeIn, double yInterceptIn)
	{
		magnitude = magnitudeIn;
		theta = yInterceptIn;
	}
	
//	returns the closest distance from this Line to the coordinates C
	public double findDistanceClosestApproach(Coordinates c)
	{
		Vector perp = createPerpendicular(c);
		return 0;
	}
	
	private Vector createPerpendicular(Coordinates c) 
	{
		
		return this;
	}
	
	public double getMagnitude()
	{
		return magnitude;
	}
	
	public double getTheta() 
	{
		return theta;
	}
	
	public void setMagnitude(double magnitudeIn)
	{
		magnitude = magnitudeIn;
	}
	
	public void setYIntercept(double yInterceptIn)
	{
		theta = yInterceptIn;
	}
}
