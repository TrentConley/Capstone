package simulation;
import java.util.*;

/**
 * @author trentconley
 * Therefore, the classical calculation holds true when the speed of both colliding bodies are 
 * much lower than the speed of light (~300 million m/s).
 */
public class SimulationLauncher 
	{
	public static final int NUM_ATOMS = 10;
	public static final double TEMPERATURE_SYSTEM = 273;
	

	/**
	 * @param args
	 */
	public static void main(String[] args) 
	{
		System.out.println("Hello, World");
		Vector myVector = new Vector(0,0);
		Coordinates myCoords = new Coordinates(0,0);
		Atom myAtom = new Helium(myCoords, myVector);
		System.out.println(myAtom);
		Atom[] myAtoms = createHelium();
		
		
		// TODO Auto-generated method stub
	}
	
	public static Helium[] createHelium()
	{
		Helium[] allAtoms = new Helium[NUM_ATOMS];
		for (int i = 0; i < NUM_ATOMS; i++)
		{
			allAtoms[i] = createAtomFollowingDistribution();
		} 
		return allAtoms;
	}
	
	private static Helium createAtomFollowingDistribution()
	{
		
		return null;
	}
	

			
	
}

