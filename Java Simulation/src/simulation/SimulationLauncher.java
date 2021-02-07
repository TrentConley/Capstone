package simulation;
import java.math.*;
import java.util.*;

/**
 * @author trentconley
 * Therefore, the classical calculation holds true when the speed of both colliding bodies are 
 * much lower than the speed of light (~300 million m/s).
 * 
 * http://hyperphysics.phy-astr.gsu.edu/hbase/Kinetic/kintem.html getting some gas math from here
 */
// I will be using argon in the simulation because it is the cheapest noble gas, and I want
// to actually build this simulation
// we can make the simulation a cubic millimeter. I think that is a good idea. 
public class SimulationLauncher 
	{
//	the number of atoms in the system
	public static final int NUM_ATOMS = 10;
	
//	all atoms will be assigned a single temperature, but as the simulation continues they will 
//	naturally fall into a Maxwell-Boltzmann distribution. 
	public static final BigDecimal STARTING_TEMPERATURE_SYSTEM = new BigDecimal ("273.0");
	
//	This should equal 1.38064852 * 10^-23, boltzmann constant
	public static final BigDecimal k = new BigDecimal(".000000000000000000000138064852");
	
	public static final double SIZE_X = 0;
	
	public static final double SIZE_Y = 0;
	

	/**
	 * @param args
	 * next step: collision mechanism. 
	 */
	public static void main(String[] args) 
	{
		Atom[] myAtoms = createArgon();
		print(myAtoms);
		
		
		// TODO Auto-generated method stub
	}
	
	public static Argon[] createArgon()
	{
		Argon[] allAtoms = new Argon[NUM_ATOMS];
		for (int i = 0; i < NUM_ATOMS; i++)
		{
			allAtoms[i] = createArgonFollowingDistribution();
		} 
		return allAtoms;
	}
	
	private static Argon createArgonFollowingDistribution()
	{
//		velocity equals (from solving equations from the link at the top of the file) 
//		(3kT/m)^(1/2) where k is the 
//		k = 1.38064852 × 10^-23 m^2 kg s^-2 K-1
		BigDecimal three = new BigDecimal("3.0"); 
		BigDecimal mass = new BigDecimal (String.valueOf(Argon.MASS));
		print(mass);
		BigDecimal ktemp = k.multiply(STARTING_TEMPERATURE_SYSTEM);
		BigDecimal ktempthree = ktemp.multiply(three);
		MathContext mc = new MathContext(2, RoundingMode.HALF_UP);
		BigDecimal ktempthreemass = ktempthree.divide(mass, mc);
		BigDecimal velocityBigDecimal = ktempthreemass.sqrt(mc);
		print(velocityBigDecimal);
		double velocity = velocityBigDecimal.doubleValue();
		
//		I created the lines above to be redundant in the calculation of the velocity. 
		double theta = Math.random()*2*Math.PI;
		double x = Math.random()*SIZE_X;
		double y = Math.random()*SIZE_Y;
		Coordinates c = new Coordinates (x,y);
		Vector v = new Vector(velocity, theta);
		Argon newArgon = new Argon(c, v);
		return newArgon;
		
		
		
//		find the units for everything!!!
		
		
	}
	
	public static void print(Atom[] a)
	{
		for (int i = 0; i < a.length; i ++)
		{
			print(a[i]);
		}
	}
	
	public static void print(Atom a)
	{
//		I honestly this its dumb how java makes you type out a bunch of stuff for printing
		System.out.println(a);
	}
	
	public static void print(BigDecimal n)
	{
		System.out.println(n);
	}
}