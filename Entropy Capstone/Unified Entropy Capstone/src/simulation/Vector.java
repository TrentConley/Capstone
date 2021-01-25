package simulation;

// This class will store everything related to lines, and manipulations. 
public class Vector 
{
	private double magnitude;
	private double theta;
	
	public Vector (double magnitudeIn, double thetaIn)
	{
		magnitude = magnitudeIn;
		theta = thetaIn;
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
		return this.magnitude;
	}
	
	public double getTheta() 
	{
		return this.theta;
	}
	
	public void setMagnitude(double magnitudeIn)
	{
		this.magnitude = magnitudeIn;
	}
	
	public void setTheta(double thetaIn)
	{
		this.theta = thetaIn;
	}
}
