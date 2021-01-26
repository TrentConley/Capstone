/**
 * 
 */
package simulation;

/**
 * @author trentconley
 * Therefore, the classical calculation holds true when the speed of both colliding bodies are 
 * much lower than the speed of light (~300 million m/s).
 */
public class SimulationLauncher 
	{

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

}
