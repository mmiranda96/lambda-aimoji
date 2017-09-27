import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
public class User 
{
	private String nombre;
	private String identificador;
	private ArrayList<User> seguidores;
	private ArrayList<User> siguiendo;

	public User(String nombre, String identificador, ArrayList<User> seguidores, ArrayList<User> siguiendo)
	{
		this.nombre = nombre;
		this.identificador = identificador;
		this.seguidores = seguidores;
		this.siguiendo = siguiendo;
	}

	public User(ArrayList<User> seguidores, ArrayList<User> siguiendo)
	{
		this.seguidores = seguidores;
		this.siguiendo = siguiendo;
	}
	public User(String nombre, String identificador)
	{
		this.nombre = nombre;
		this.identificador = identificador;
	}

	public String getNombre()
	{
		return this.nombre;
	}

	public String getID()
	{
		return this.identificador;
	}
	public ArrayList<User> getSeguidores()
	{
		return this.seguidores;
	}
	public ArrayList<User> getSiguiendo()
	{
		return this.siguiendo;
	}

	public void mostrarNombre()
	{
		System.out.println("Nombre: "+getNombre());
	}

	public void mostrarID()
	{
		System.out.println("ID: "+getID());
	}

	public String mostrarSeguidores(User usuario)
	{
		ArrayList<User> usuarios = new ArrayList<User>();
		String msj;
		usuarios=usuario.getSeguidores();
		msj=usuario.mostrarUsuario(usuarios);
		return msj;
	}
	public String mostrarSiguiendo(User usuario)
	{
		ArrayList<User> usuarios = new ArrayList<User>();
		String msj;
		usuarios=usuario.getSiguiendo();
		msj=usuario.mostrarUsuario(usuarios);
		return msj;
	}

	public String mostrarUsuario(ArrayList<User> listasDeUsuarios)
	{
		String mostrarMSJ="";
		for(User usuario: listasDeUsuarios)
		{
			mostrarMSJ = mostrarMSJ +"ID: " + usuario.getID()+" ";
			mostrarMSJ = mostrarMSJ +"Nombre: " + usuario.getNombre()+"\n";
		}
		return mostrarMSJ;
	}

	public String toString()
	{
		return ("ID: " + identificador+", Nombre: " + nombre );
	}
	public void setSeguidores(User usuario)
	{
		this.seguidores.add(usuario);
	}
	public void setSiguiendo(User usuario)
	{
		this.siguiendo.add(usuario);
	}
	
		/*public static void menuUsuarios() 
	{
		System.out.println("Gestion de usuarios\n");
		System.out.println("Opciones posibles: ");
		System.out.println("1. Crear Usuario");
		System.out.println("2. Mostrar todos los usuarios");
		System.out.println("3. Borrar Usuario");
		System.out.println("4. Seguir Usuario");
		System.out.println("5. Muestra seguidores de un usuario");
		System.out.println("6. Muestra usuarios que sigue un usuario");
		System.out.println("7. Terminar");
	}*/
}