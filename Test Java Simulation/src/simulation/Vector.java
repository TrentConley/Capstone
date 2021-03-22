package simulation;

public class Vector 
{
	private Coordinates tail;
	private double xMag;
	private double yMag;
	public Vector (double xMag, double yMag, Coordinates tail)
	{
		this.xMag = xMag; 
		this.yMag = yMag; 
		this.tail = tail;
	}
	public double getXMag()
	{
		return this.xMag;
	}
	public double getYMag()
	{
		return this.yMag;
	}
	public Coordinates getTail()
	{
//		return this.tail;
		return new Coordinates(this.tail.getX(), this.tail.getY());
	}
	public void setXMag(double xMag)
	{
		this.xMag = xMag;
	}
	public void setYMag(double yMag)
	{
		this.yMag = yMag;
	}
	public void setTail(Coordinates c)
	{
//		this.tail = c;
		this.tail = new Coordinates (c.getX(), c.getY());
	}
	public String toString() {
		return "xMag: " + Double.toString(this.xMag) + " yMag " + Double.toString(yMag) +
				" tail info: " + this.tail.toString();
	}
}
