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
// we can make the simulation a cubic centimeter. I think that is a good idea. 

// add a way to change the pressure, to determine the number of molecules in the simulation. 
public class SimulationLauncher 
	{
//	the number of atoms in the system

//  PV = nRT
//	we will be determining the amount (n) of molecules in the system
//	measured in atmospheres. 
//	ideal gas constant
	public static final BigDecimal R = new BigDecimal ("8.31446261815324");
	
	public static final BigDecimal PRESSURE = new BigDecimal("1");
	public static final BigDecimal TEMPERATURE = new BigDecimal ("293.0");
	
//	the size of the simulation will be in pico meters to match the radius of the atoms,
//	the size of this is equal to 10 cubic (or square first) micrometers. 100000000000000
//	i should probably check the calculations 
	public static final BigDecimal VOLUME = new BigDecimal(1.0e14); 
	
	public static final BigInteger NUM_ATOMS = PRESSURE.multiply(VOLUME).divide((R.multiply(TEMPERATURE))).toBigInteger(); 
	
	


	
//	avagadros number
	public static final BigDecimal A = new BigDecimal(6.02214076e23);
	

	
	
//	public static final int NUM_ATOMS = (int) (PRESSUE);
//	Because we are not working the three dimensions yet, we cannot apply current equations to govern 
//	pressure, volume, and temperature. 

	
	public static final double CUBIC_SIZE = 0; 
	

	

	
 //	math context for finding the size of the simulation 
	
	public static final MathContext mc = new MathContext(17, RoundingMode.HALF_UP);
	
	public static final BigDecimal SIZE_X = VOLUME.sqrt(mc);
	
	public static final BigDecimal SIZE_Y = VOLUME.sqrt(mc);
	
//	all atoms will be assigned a single temperature, but as the simulation continues they will 
//	naturally fall into a Maxwell-Boltzmann distribution. 

	
//	This should equal 1.38064852 * 10^-23, boltzmann constant
	public static final BigDecimal k = new BigDecimal("1.38064852e-23");
	

	
	

	
//	1 amu  = 1.6605e-27 kg
	public static final BigDecimal atomicMassUnitsToKilograms = new BigDecimal("1.6605e-27");
	
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
//		Note to self: make sure there are no overlaps with the wall and the created atoms. 
//		velocity will be in terms of meters per second, so we need to convert to picometers per second
		double velocity = getVelocity()*1000 /*milimeters*/ *1000 /*micrometers*/ *1000/*picometers*/;
//		I can combine the line above when I finilize the project
//		I created the lines above to be redundant in the calculation of the velocity. 
		double theta = Math.random()*2*Math.PI;
		double x = Math.random()*SIZE_X;
		double y = Math.random()*SIZE_Y;
		Coordinates c = new Coordinates (x,y);
		Vector v = new Vector(velocity, theta);
		Argon newArgon = new Argon(c, v);
		return newArgon;	
	}
	
	private static double getVelocity()
	{
//		velocity equals (from solving equations from the link at the top of the file) 
//		(3kT/m)^(1/2) where k is the 
//		k = 1.38064852 × 10^-23 m^2 kg s^-2 K-1
		BigDecimal three = new BigDecimal("3.0"); 
//		converting amu to kg
		BigDecimal massAtomicUnits = new BigDecimal (String.valueOf((Argon.MASS)));
		BigDecimal massKilograms = massAtomicUnits.multiply(atomicMassUnitsToKilograms);
		
//		operations
		BigDecimal ktemp = k.multiply(STARTING_TEMPERATURE_SYSTEM);
		BigDecimal ktempthree = ktemp.multiply(three);
		
//		need mathcontext to prevent errors. 17 digits is the precision of doubles, so am keeping
//		it at that. 
		MathContext mc = new MathContext(17, RoundingMode.HALF_UP);
		BigDecimal ktempthreemass = ktempthree.divide(massKilograms, mc);
		BigDecimal velocityBigDecimal = ktempthreemass.sqrt(mc);

		double velocity = velocityBigDecimal.doubleValue();
		return velocity;
	}
	
	public static void print(Atom[] a)
	{
		for (int i = 0; i < a.length; i ++)
		{
//			
			print(a[i]);
		}
	}
	
	public static void print(Atom a)
	{
//		I honestly think its dumb how java makes you type out a bunch of stuff for printing
		System.out.println(a);
	}
	
	public static void print(BigDecimal n)
	{
		System.out.println(n);
	}
}