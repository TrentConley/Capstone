
package simulation;

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
		Atom myAtom = new Atom(myCoords, myVector, 0);
		System.out.println(myAtom);
		
		// TODO Auto-generated method stub
	}
	
	public Atom[] createAtoms()
	{
		Atom[] allAtoms = new Atom[NUM_ATOMS];
		for (int i = 0; i < NUM_ATOMS; i++)
		{
			allAtoms[i] = createAtomFollowingDistribution();
		}
		 
		return allAtoms;
	}
	
	public Atom createAtomFollowingDistribution()
	{
		
		return null;
	}
	

			
	
}

