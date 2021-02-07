/*
 * 
 */
package simulation;
import java.math.*;

//This class will store everything related to lines, and manipulations. 
public class Vector 
{
	private double magnitude;
	private double theta;
	
	public Vector (double magnitudeIn, double thetaIn)
	{
		magnitude = magnitudeIn;
		theta = thetaIn;
	}
	
	
	public double getXvel()
	{
		return Math.cos(theta) * magnitude;
	}
	
	/*
	 * gets the y velocity component of the atom
	 */
	public double get_yvel()
	{
		return Math.sin(theta) * magnitude;
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
	
	public String toString()
	{
		return "magnitude is " + Double.toString(magnitude) + " theta is " + Double.toString(theta);
	}
}