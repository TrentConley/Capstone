package simulation;
import java.math.*;

// this class will store and manipulates x-y coordinates, and eventually z too. 
public class Coordinates 
{
	private BigDecimal x;
	private BigDecimal y;
	
	public Coordinates(BigDecimal xin, BigDecimal yin)
	{
		this.x = xin;
		this.y = yin;
	}
	
	public BigDecimal getX()
	{
		return this.x;
	}
	
	public BigDecimal getY()
	{
		return this.y;
	}
	
	public void setX(BigDecimal xIn)
	{
		this.x = xIn;
	}
	
	public void setY(BigDecimal yIn)
	{
		this.y = yIn;
	}
	
	public String toString()
	{
		return "X coordinate = " + x.toString() + " Y coordinate = " + y.toString();
	}
	
}