import java.io.*;
import java.net.InetAddress;
import java.net.Socket;

public class ClienteTCP{
	public static final int PUERTO = 4444;
	String SERVERIP;
	Cliente p;
	private Mensaje msj;
	ObjectOutputStream ou;
    ObjectInputStream in;
    
	public ClienteTCP(Cliente p,String ip){
		this.p = p;
		this.SERVERIP = ip;
	}
	public void iniciar(){
        try {
            InetAddress serverAddr = InetAddress.getByName(SERVERIP);
            System.out.println("TCP Client"+ "C: Conectando...");
            Socket socket = new Socket(serverAddr, PUERTO);
            try {
                //out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
                ou = new ObjectOutputStream(socket.getOutputStream());
                System.out.println("TCP Client"+ "C: Sent.");
                System.out.println("TCP Client"+ "C: Done.");
                in = new ObjectInputStream(socket.getInputStream());
                while (true) {
                	System.out.println("Cliente: Esperando mensaje");
                    //servermsj = in.readLine();
                    msj = (Mensaje)in.readObject();
                    if (msj != null) {
                        //mMessageListener.messageReceived(servermsj);
                        System.out.println(msj);
                    }
                    msj = null;
                    System.out.println("Cliente: Esperando mensaje Fin");
                }
            } catch (Exception e) {
                System.out.println("TCP"+ "S: Error"+e);

            } finally {
                socket.close();
            }
        } catch (Exception e) {
            System.out.println("TCP"+ "C: Error"+ e);
        }
	}
	public void enviar(Mensaje m){
		System.out.println("enviar:");
		if (ou != null ) {
            try{
	            ou.writeObject(m);
	        } catch (IOException ex) {
				System.out.println("eee");
			}
        }
	}
}
