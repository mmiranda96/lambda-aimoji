import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
public class Tweet {
	
	private int id;
	private User usuario;
	private String texto;
	private int longitud;
	private int likes;
	private ArrayList<String> palabras;
	private ArrayList<String> hashtag;

	public ArrayList<String> cuentap(String txt){
		String aux = "";
		ArrayList<String> pal = new ArrayList<String>();
		for(int i = 0; i < txt.length(); i++){
			if(txt.charAt(i) != ' '){
				aux += txt.charAt(i);
			}
			else{
				if(aux.length() > 0){
					if(aux.charAt(0) != '#'){
						pal.add(aux);
					}
				}
				aux = "";
			}
		}
		if(aux.length() > 0){
			if(aux.charAt(0) != '#'){
				pal.add(aux);
			}
		}
		return pal;
	}

	public ArrayList<String> cuentah(String txt){
		String aux = "";
		ArrayList<String> hasht = new ArrayList<String>();
		for(int i = 0; i < txt.length(); i++){
			if(txt.charAt(i) != ' '){
				aux += txt.charAt(i);
			}
			else{
				if(aux.length() > 0){
					if(aux.charAt(0) == '#'){
						hasht.add(aux);
					}
				}
				aux = "";
			}
		}
		if(aux.length() > 0){
			if(aux.charAt(0) == '#'){
				hasht.add(aux);
			}
		}
		return hasht;
	}

	public Tweet(int id, User usuario, String texto)
	{
		this.id = id;
		this.usuario = usuario;
		this.texto = texto;
		this.longitud = texto.length();
		this.likes = 0;
		this.palabras = cuentap(texto);
		this.hashtag = cuentah(texto);
	}

	public void like()
	{
		likes++;
	}

	public User getUsuario()
	{
		return usuario;
	}

	public void mostrarSin()
	{
		System.out.println("Tweet ID: " + id);
		System.out.println("Likes: " + likes);
	}

	public void mostrarCon()
	{
		System.out.println("Tweet ID: " + id);
		System.out.println(texto);
		System.out.println("Likes: " + likes);
	}

	public void mostrarPalabras()
	{
		for(int i = 0; i < palabras.size(); i++)
		{
			System.out.print(palabras.get(i) + " ");
		}
	}

	public void mostrarHashtags()
	{
		for(int i = 0; i < hashtag.size(); i++)
		{
			System.out.print(hashtag.get(i) + " ");
		}
	}
}