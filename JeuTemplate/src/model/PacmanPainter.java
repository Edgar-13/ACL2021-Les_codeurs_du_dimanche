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
	protected static final int WIDTH = 1000;
	protected static final int HEIGHT = 1000;

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
	public void draw(BufferedImage im) {
		Graphics2D fond = (Graphics2D) im.getGraphics();
		Graphics2D player = (Graphics2D) im.getGraphics();
		
		Image image = null;
		try {
			image = ImageIO.read(new File("C:\\Users\\esteb\\Documents\\ensem\\2A\\analyse et conception de logiciels\\projet\\ACL2021-Les_codeurs_du_dimanche\\JeuTemplate\\map.png"));
			fond.drawImage(image, 0, 0,1000,1000, null);
			image = ImageIO.read(new File("C:\\Users\\esteb\\Documents\\ensem\\2A\\analyse et conception de logiciels\\projet\\ACL2021-Les_codeurs_du_dimanche\\JeuTemplate\\pacman.png"));
			player.drawImage(image, 0, 0, 50, 50, null);
			
		} 
		catch (IOException e) {

			player.drawString("Image inexistante", 0, 0);  }
		
		
	}

	@Override
	public int getWidth() {
		return WIDTH;
	}

	@Override
	public int getHeight() {
		return HEIGHT;
	}

}
