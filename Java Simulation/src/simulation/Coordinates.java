package simulation;
import java.math.*;

// this class will store and manipulates x-y coordinates, and eventually z too. 
public class Coordinates 
{
	private BigDecimal x;
	private BigDecimal y;
	
	public Coordinates(BigDecimal xin, BigDecimal yin)
	{
		x = xin;
		y = yin;
	}
	
	public BigDecimal getX()
	{
		return x;
	}
	
	public BigDecimal getY()
	{
		return y;
	}
	
	public void setX(BigDecimal xIn)
	{
		x = xIn;
	}
	
	public void setY(BigDecimal yIn)
	{
		y = yIn;
	}
	
	public String toString()
	{
		return "X coordinate = " + x.toString() + " Y coordinate = " + y.toString();
	}
	
}