package simulation;

// this class will store and manipulates x-y coordinates, and eventually z too. 
public class Coordinates 
{
	private double x;
	private double y;
	
	public Coordinates(double xin, double yin)
	{
		x = xin;
		y = yin;
	}
	
	public double getX()
	{
		return x;
	}
	
	public double getY()
	{
		return y;
	}
	
	public void setX(double xIn)
	{
		x = xIn;
	}
	
	public void setY(double yIn)
	{
		y = yIn;
	}
	
	public String toString()
	{
		return "X coordinate = " + Double.toString(x) + " y coordinate = " + Double.toString(y);
	}
	
}

