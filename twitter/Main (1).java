import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
public class Main
{
	public static void main(String[]args)
	{
		Scanner sc = new Scanner(System.in);
		User user;
		User usuario;
		User usuariosiguiendo;
		User usuarioaseguir;
		int ind, ind2;
		int opc = 0;
		int opcUsuarios = 0;
		int opcTweet = 0;
		String nombre;
		String identificador;
		int idTweet = 0;
		ArrayList<User> usuarios = new ArrayList<User>();
		ArrayList<User> seguidores = new ArrayList<User>();
		ArrayList<User> siguiendo = new ArrayList<User>();
		ArrayList<Tweet> tweets = new ArrayList<Tweet>();

		while(opc!=3)
		{
			menuGeneral();
			opc = sc.nextInt();
			switch(opc)
			{
				case 1:
				while(opcUsuarios!=7)
				{
					menuUsuarios();
					opcUsuarios = sc.nextInt();
					switch(opcUsuarios)
					{
						case 1:
						System.out.println("Para crear un nuevo usuario, establezca su ID (No espacios)");
						identificador = sc.next();		
						System.out.println("Cual quiere que sea el nombre visible para el usuario en cuestion? (No espacios) ");	
						nombre = sc.next();			
						usuarios.add(new User(nombre, identificador, seguidores, siguiendo));
						System.out.println("Se a creado un nuevo usuario");
						break;
						case 2:
						for(int o=0; o<=usuarios.size()-1; o++)
						{
							user = usuarios.get((o));
							System.out.println("Su usuario numero "+o+" es: \n"+ user.toString()+"\n");
						}
						break;
						case 3:
						System.out.println("Tus usuarios actuales son: ");
						for(int o=0; o<=usuarios.size()-1; o++)
						{
							user = usuarios.get((o));
							System.out.println("Su usuario numero "+o+" es: \n"+ user.toString()+"\n");
						}
						System.out.println("Seleccionar el usuario que desea borrar: ");
						int erase = sc.nextInt();
						usuarios.remove(erase);
						break;
						case 4:
						System.out.println("Que usuario eres? (Inserta indice): ");
						ind = sc.nextInt();
						usuariosiguiendo = usuarios.get(ind);
						System.out.println("Indice del usuario que quieres seguir: ");
						ind2 = sc.nextInt();
						usuarioaseguir = usuarios.get(ind2);
						//se setean
						usuarioaseguir.setSeguidores(usuariosiguiendo);
						usuariosiguiendo.setSiguiendo(usuarioaseguir);
						break;
						case 5: 
						System.out.println("Inserta su indice del usuario que desea ver sus seguidores: ");
						ind = sc.nextInt();
						usuario = usuarios.get(ind);
						System.out.println(usuario.mostrarSeguidores(usuario));

						break;
						case 6: 
						System.out.println("Iserte el indice del usuario que desea ver a quien sigue: ");
						ind=sc.nextInt();
						usuario = usuarios.get(ind);
						System.out.println(usuario.mostrarSiguiendo(usuario));
						break;
						case 7:
						break;
						default: System.out.println("Estem, no existe la opcion insertada, intenta de nuevo :)");
					}
				}
				break;
				case 2:
				while(opcTweet!=7)
				{
					System.out.println("Elija desde que usuario quiere acceder al menu de tweets.");
					int nus = sc.nextInt();
					menuTweets();
					opcTweet = sc.nextInt();
					int twt;
					int usr;
					switch(opcTweet)
					{
						case 1:
						System.out.println("Escriba el texto de su tweet.");
						sc.nextLine();
						String textweet = sc.nextLine();
						tweets.add(new Tweet(idTweet, usuarios.get(nus), textweet));
						idTweet++;
						break;
						case 2:
						System.out.println("De que usuario quieres mostrar los tweets?");
						usr = sc.nextInt();
						for(int i = 0; i < tweets.size(); i++){
							if(tweets.get(i).getUsuario() == usuarios.get(usr)){
								tweets.get(i).mostrarSin();
							}
						}
						break;
						case 3:
						System.out.println("De que tweet deseas ver las palabras?");
						twt = sc.nextInt();
						tweets.get(twt).mostrarPalabras();
						break;
						case 4:
						System.out.println("De que tweet deseas ver los hashtags?");
						twt = sc.nextInt();
						tweets.get(twt).mostrarHashtags();
						break;
						case 5:
						System.out.println("De que usuario quieres mostrar los tweets?");
						usr = sc.nextInt();
						for(int i = 0; i < tweets.size(); i++){
							if(tweets.get(i).getUsuario() == usuarios.get(usr)){
								tweets.get(i).mostrarCon();
							}
						}
						break;
						case 6:
						System.out.println("A que tweet quieres darle like?");
						twt = sc.nextInt();
						tweets.get(twt).like();
						break;
						case 7:
						break;
						default: System.out.println("Estem, no existe la opcion insertada, intenta de nuevo :)");
					}
				}
				break;
				case 3:
				System.out.println("*****END*****");
				break;
				default:System.out.println("Estem, no existe la opcion insertada, intenta de nuevo :)");
			}
		}
	}
	public static void menuGeneral() 
	{
		System.out.println("***Twitter version alfa***\n");
		System.out.println("Opciones posibles: ");
		System.out.println("1. Gestion de usuarios");
		System.out.println("2. Gestion de tweets");
		System.out.println("3. Terminar");
	}

	public static void menuUsuarios() 
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
	}

	public static void menuTweets() 
	{
		System.out.println("Gestion de tweets\n");
		System.out.println("Opciones posibles: ");
		System.out.println("1. Escribir Tweet");
		System.out.println("2. Mostrar todos los tweets sin palabras ni hashtags de un usuario seguido");
		System.out.println("3. Separar palabras de un tweet");
		System.out.println("4. Encontrar hashtags de un tweet");
		System.out.println("5. Mostrar todos los tweets con palabras y con hashtags de un usuario seguido");
		System.out.println("6. Dar like a un tweet de un usuario");
		System.out.println("7. Terminar");
	}
}