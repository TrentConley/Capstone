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
	
	public static final BigDecimal PRESSURE = new BigDecimal("1.0e-10");
	public static final BigDecimal TEMPERATURE = new BigDecimal ("293.0");
	
//  square size (for now) in picometers
	public static final BigDecimal VOLUME = new BigDecimal(1.0e16); 

	//	need mathcontext to prevent infinite decimal errors. I will try to speed up simulation 
//	in future and not use big Decimals. 
	public static final MathContext MC = new MathContext(30, RoundingMode.HALF_UP);
	
	public static final BigInteger NUM_ATOMS = PRESSURE.multiply(VOLUME, MC).divide(R.multiply(TEMPERATURE, MC), MC).toBigInteger(); 
	
//	avagadros number
	public static final BigDecimal A = new BigDecimal(6.02214076e23);
	

	

	
	public static final BigDecimal SIZE_X = VOLUME.sqrt(MC);
	
	public static final BigDecimal SIZE_Y = VOLUME.sqrt(MC);
	
//	all atoms will be assigned a single temperature, but as the simulation continues they will 
//	naturally fall into a Maxwell-Boltzmann distribution. 

	
//	This should equal 1.38064852 * 10^-23, boltzmann constant
	public static final BigDecimal k = new BigDecimal("1.38064852e-23");
	

//	1 amu  = 1.6605e-27 kg
	public static final BigDecimal atomicMassUnitsToKilograms = new BigDecimal("1.6605e-27");
	
	public static final double END_TIME = 0;
	
	/**
	 * @param args
	 * next step: collision mechanism. 
	 */
	public static void main(String[] args) 
	{
//		as of February 20th, 2021, the current number of atoms are 410. Should be enough to simulate. 
		Atom[] myAtoms = createArgon();
		BigDecimal currentTime = new BigDecimal("0.0");
		BigDecimal shortestTime = myAtoms[0].timeUntilCollision(MC, myAtoms[1]);
		while (currentTime.doubleValue() < END_TIME)
		{
			// finding the shortest time and atoms until collision
			for (int i =0; i < myAtoms.length; i++)
			{
				for (int j = 1; j < myAtoms.length; j ++)
				{
					//There will always be more than 2 atoms
					BigDecimal collision = myAtoms[i].timeUntilCollision(MC, myAtoms[j]);
					
				}
			}
			update(myAtoms, shortestTime);
			currentTime = currentTime.add(shortestTime, MC);
			// simulate!
		}
		
		// TODO Auto-generated method stub
	}
	
	public static void timeUntilCollision()
	{
		 
	}
	
	public static void update(Atom[] arr, BigDecimal t)
	{
		for (Atom a: arr)
		{
			a.update(t, MC);
		}
	}

	public static Argon[] createArgon()
	{
		print(NUM_ATOMS);
		Argon[] allAtoms = new Argon[NUM_ATOMS.intValue()];
		for (int i = 0; i < NUM_ATOMS.intValue(); i++)
		{
			allAtoms[i] = createArgonFollowingDistribution();
		} 
		return allAtoms;
	}
	
	private static Argon createArgonFollowingDistribution()
	{
//		Note to self: make sure there are no overlaps with the wall and the created atoms. 
//		velocity will be in terms of meters per second, so we need to convert to picometers per second
		BigDecimal velocity = getVelocity().multiply(new BigDecimal("1000000000"), MC) /*milimeters*/  /*micrometers*/ /*picometers*/;
//		I can combine the line above when I finilize the project
//		I created the lines above to be redundant in the calculation of the velocity. 

		Argon newArgon = null;
		do
		{
			BigDecimal x = SIZE_X.multiply(new BigDecimal(Math.random()));
			BigDecimal y = SIZE_Y.multiply(new BigDecimal(Math.random()));
			BigDecimal xMag = null, yMag = null;
			xMag = velocity; yMag = velocity;
//			now we need to get the magnitude in an effiecinent way. 
			Coordinates c = new Coordinates (x,y);
			Vector v = new Vector(xMag, yMag, new Coordinates(x, y));
			newArgon = new Argon(v);
		}
		while(notTouchingBorder(newArgon));
		
		return newArgon;	
	}
	
	private static Boolean notTouchingBorder(Atom a)
	{
		return false;
	}
	
	private static BigDecimal getVelocity()
	{
//		velocity equals (from solving equations from the link at the top of the file) 
//		(3kT/m)^(1/2) where k is the 
//		k = 1.38064852 × 10^-23 m^2 kg s^-2 K-1
		BigDecimal three = new BigDecimal("3.0"); 
//		converting amu to kg
		BigDecimal massAtomicUnits = new BigDecimal (String.valueOf((Argon.MASS)));
		BigDecimal massKilograms = massAtomicUnits.multiply(atomicMassUnitsToKilograms);
		
//		operations
		BigDecimal ktemp = k.multiply(TEMPERATURE);
		BigDecimal ktempthree = ktemp.multiply(three);
		

		BigDecimal ktempthreemass = ktempthree.divide(massKilograms, MC);
		BigDecimal velocityBigDecimal = ktempthreemass.sqrt(MC);
		return velocityBigDecimal;
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
	
	public static void print(BigInteger n)
	{
		System.out.println(n);
	}
}