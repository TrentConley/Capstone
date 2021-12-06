package testCodePackage;

import java.awt.*;						
import javax.swing.*;

/**
 * Some not-very-well documented working examples of drawing recursive "trees"
 */

public class FractalTrees extends JFrame 
{
	public static void main(String args[])
	{
		FractalTrees gp = new FractalTrees();
		gp.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gp.setTitle("Draw A Recursive Tree");			
		gp.setSize(1000, 770);					
		gp.setVisible(true);					
	}

	public void paint(Graphics g) 		
	{
		drawTree1(300, 750, 140, Math.PI/2, g);
		drawTree2(650, 550, 300, Math.PI/2, g);
	}

	public void drawTree1(double x0, double y0, double len, double angle, Graphics g) 
	{
		g.setColor(Color.BLUE);
		if (len > 1.5) 
//		if (len > 5)
//		if (len > 40)		
//		if (len > 80) 
		{
			double x1 = x0 + len * Math.cos(angle);
			double y1 = y0 - len * Math.sin(angle);

			g.drawLine((int)x0, (int)y0, (int)x1, (int)y1);
			drawTree1(x1, y1, len * 0.75, angle + Math.PI / 8, g);
			drawTree1(x1, y1, len * 0.66, angle - Math.PI * 50 / 180, g);
		}
	}

	public void drawTree2(double x0, double y0, double len, double angle, Graphics g) 
	{
		g.setColor(Color.RED);
		final double A_MULTIPLIER = 0.35;
		final double B_MULTIPLIER = 0.75;
		
		if(len > 5) 
		{
			double x1 = x0 + len * Math.cos(angle);
			double y1 = y0 - len * Math.sin(angle);
			g.drawLine((int)x0, (int)y0, (int)x1, (int)y1);
			
			double xA = x0 + A_MULTIPLIER * len * Math.cos(angle);
			double yA = y0 - A_MULTIPLIER * len * Math.sin(angle);
			drawTree2(xA, yA, len * 0.75, angle + Math.PI / 12, g);
			
			double xB = x0 + B_MULTIPLIER * len * Math.cos(angle);
			double yB = y0 - B_MULTIPLIER * len * Math.sin(angle);
			drawTree2(xB, yB, len * 0.66, angle - Math.PI * 50 / 180, g);
			
			drawTree2(x1, y1, len * 0.3, angle + Math.PI / 10, g);
		}
	}
}


