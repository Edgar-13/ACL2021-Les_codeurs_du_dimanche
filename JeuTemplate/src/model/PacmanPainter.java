package model;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.BufferedImage;

import javax.imageio.ImageIO;

import engine.GamePainter;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/**
 * @author Horatiu Cirstea, Vincent Thomas
 *
 * afficheur graphique pour le game
 * 
 */
public class PacmanPainter implements GamePainter {

	/**
	 * la taille des cases
	 */
	protected static final int WIDTH_bg1 = 1000;
	protected static final int HEIGHT_bg1 = 1000;
	
	protected static final int WIDTH_pacman = 50;
	protected static final int HEIGHT_pacman = 50;

	/**
	 * appelle constructeur parent
	 * 
	 * @param game
	 *            le jeutest a afficher
	 */
	public PacmanPainter() {
	}

	/**
	 * methode  redefinie de Afficheur retourne une image du jeu
	 */
	@Override
	public void draw (BufferedImage im) {
		Graphics2D bg1 = (Graphics2D) im.getGraphics();
		Graphics2D player = (Graphics2D) im.getGraphics();
		
		Image image = null;
		try {
			
			// Background 1
			image = ImageIO.read(new File("map1.jpg"));
			bg1.drawImage(image, 0, 0,WIDTH_bg1,HEIGHT_bg1, null);
			
			
			image = ImageIO.read(new File("pacman.png"));
			player.drawImage(image, 0, 0, WIDTH_pacman, HEIGHT_pacman, null);
			
		} 
		catch (IOException e) {

			player.drawString("Image inexistante", 0, 0);  }
		
		
	}
	

	@Override
	public int getWidth() {
		return WIDTH_bg1;
	}

	@Override
	public int getHeight() {
		return HEIGHT_bg1;
	}

}
