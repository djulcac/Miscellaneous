import java.util.Scanner;

public class Servidor{
	ServidorTCP h;
	Scanner sc;
	public static void main(String arg[]){
		new Servidor().iniciar();
	}
	void iniciar(){
		System.out.println("iniciar");
		Servidor yo = this;
		Thread thread = new Thread(){
			public void run(){
				//System.out.println("Thread Running");
				h = new ServidorTCP(yo);
				h.iniciar();
			}
		};
		thread.start();
        //---- escuchar
        sc = new Scanner(System.in);
        String sin = "ok";
        while(!sin.equals("salir")){
        	sin = sc.nextLine();
        	System.out.println("ECO:"+sin);
        	h.enviarAll(new Mensaje("ok--"));
        }
	}
	public void ver(Mensaje m){
		System.out.println("::"+m);
	}
}
