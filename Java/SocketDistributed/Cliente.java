import java.util.Scanner;

public class Cliente{
	ClienteTCP h;
	Scanner sc;
	public static void main(String args[]){
		new Cliente().iniciar();
	}
	void iniciar(){
		System.out.println("iniciar");
		Cliente yo = this;
		Thread thread = new Thread(){
			public void run(){
				h = new ClienteTCP(yo,"127.0.0.1");
				h.iniciar();
			}
		};
		thread.start();
		// ----
		String sin = "n";
        sc = new Scanner(System.in);
        System.out.println("Cliente bandera 01");
        while( !sin.equals("s")){
            sin = sc.nextLine();
            //ClienteEnvia(new Mensaje(sin));
            h.enviar(new Mensaje("gg"));
        }
        System.out.println("Cliente bandera 02");
	}
}
