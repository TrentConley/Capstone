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
	
//	public double find
	
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
