/*
 * 
 */
package simulation;
import java.math.*;
//I don't need this class

//This class will store everything related to lines, and manipulations. 
public class Vector 
{
	/*
	 * I'm going to redesign this class. The following lines will help me think through this. 
	 * you need to keep the magnitude the same when it is generated by RNG
	 * If you assign a random varable to x, then i'm affraid that y will be affected so that
	 * there will be a skewed distribution
	 * however, if you keep the theta as an intermediary step, then you eliminate the risk of 
	 * potential skewing. All I would have to calculate is the acutal conversion from the theta
	 * to the vector coefficients. I dont think that will be too hard. However, applying that method
	 * to three dimentions is quite hard. However, I could simply add another RNG for the x-z plane
	 * and that should solve the problem. I think that is how I will impliment this class. 
	 * 
	 * 
	 * 
	 * 
	 */
 //the tail will be a tuple of the coordinates that the object starts at
//	also, when randomly generating the atoms, make sure that there are no collisions with the 
//	boundries of the syste. 
	
	private BigDecimal xMag;
	private BigDecimal yMag;
	private Coordinates tail;
	
	public Vector (BigDecimal xMagIn, BigDecimal yMagIn, Coordinates tailIn)
	{
		this.xMag = xMagIn;
		this.yMag = yMagIn;
		this.tail = tailIn;
	}
	
	public BigDecimal getXMag() 
	{
		return new BigDecimal (this.xMag.toString());
	}
	
	public BigDecimal getYMag()
	{
		return new BigDecimal (this.yMag.toString());
	}
	
	public Coordinates getTail()
	{
		return new Coordinates(this.tail.getX(), this.tail.getY());
	}

	
	public void setXMag(BigDecimal xMagIn)
	{
		this.xMag = new BigDecimal (xMagIn.toString());
	}
	
	public void setYMag(BigDecimal yMagIn)
	{
		this.yMag = new BigDecimal(yMagIn.toString());
	}
	 
	public void setTail (Coordinates tailIn)
	{
		this.tail = new Coordinates (tailIn.getX(), tailIn.getY());
	}
	
	public String toString()
	{
		return "X = " + xMag.toString() + ", Y = " + yMag.toString() + " " + tail.toString();
	}

	public void update(BigDecimal t, MathContext mc) 
	{
		// calculate the new position of the atoms
		BigDecimal additionX = this.xMag.multiply(t, mc);
		BigDecimal additionY = this.yMag.multiply(t, mc);
	
//		adds the addition of each position to the vector's tail. 
		this.tail.setX(this.tail.getX().add(additionX, mc));
		this.tail.setY(this.tail.getX().add(additionY, mc));
		// TODO Auto-generated method stub
		
	}
}