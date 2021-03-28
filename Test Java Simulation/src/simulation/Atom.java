package simulation;

public class Atom 
{
	private final int SIZE = 5; //radius
	private Vector v;
	private String closeWall; // wall that it will impact the soonest
	public Atom (Vector v)
	{
		this.v = new Vector(v.getXMag(), v.getYMag(), v.getTail());
	}
	public Vector getVector()
	{
//		return this.v;
		return new Vector(this.v.getXMag(), this.v.getYMag(), this.v.getTail());
	}
	public void setVector(Vector v)
	{
//		this.v = v; 
		this.v = new Vector(v.getXMag(), v.getYMag(), v.getTail());
	}
	public int getSize()
	{
		return SIZE;
	}
	public void setCloseWall(String closeWallIn)
	{
		this.closeWall = closeWallIn;
	}
	public String getCloseWall()
	{
		return closeWall;
	}
	public String toString()
	{
		return this.v.toString() + " Size: " + Integer.toString(SIZE);
	}
	
}
