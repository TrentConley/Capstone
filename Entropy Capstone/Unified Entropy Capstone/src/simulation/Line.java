package simulation;

// This class will store everything related to lines, and manipulations. 
public class Line 
{
	private double slope;
	private double yIntercept;
	
	public Line (double slopeIn, double yInterceptIn)
	{
		slope = slopeIn;
		yIntercept = yInterceptIn;
	}
	
//	returns the closest distance from this Line to the coordinates C
	public double findDistanceClosestApproach(Coordinates c)
	{
		Line perp = createPerpendicular(c);
		return 0;
	}
	
	private Line createPerpendicular(Coordinates c) 
	{
		
		return this;
	}
	
	public double getSlope()
	{
		return slope;
	}
	
	public double getYIntercept() 
	{
		return yIntercept;
	}
	
	public void setSlope(double slopeIn)
	{
		slope = slopeIn;
	}
	
	public void setYIntercept(double yInterceptIn)
	{
		yIntercept = yInterceptIn;
	}
}
