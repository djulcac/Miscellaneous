import java.net.Socket;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.*;

public class ServidorTCPThread extends Thread{
	int id;
	ServidorTCP p;
	Socket socket;
	private Mensaje msj;
	ObjectOutputStream ou;
    ObjectInputStream in;
    
	public ServidorTCPThread(ServidorTCP sp,int id,Socket s){
		this.p = sp;
		this.id = id;
		this.socket = s;
	}
	public void run(){
		System.out.println("okTCPT");
		try {
            try {
                ou = new ObjectOutputStream(this.socket.getOutputStream());
                in = new ObjectInputStream(this.socket.getInputStream());
                System.out.println("Conectado");
                // escucha mensajes del cliente
                while (true) {
                    //message = new Mensaje(in.readLine());//
                    msj = (Mensaje)in.readObject();
                    //if (message.str != null && messageListener != null) {
                    if (msj != null) {
                    	System.out.println("Mensaje del cliente: "+this.id+"\n"+msj);
                        //messageListener.messageReceived(message);
                    }else{
                    	break;
                    	// aqui se detecta que el cliente se desconecto
                    }
                    //eco
                    //System.out.println("Eco de:" + clientID +" dice:" + message);
                 
                    msj = null;
                }
                System.out.println("RESPONSE FROM CLIENT"+ "S: Received Message: '" + msj + "'");
            } catch (Exception e) {
                System.out.println("TCP Server"+ "S: Error"+ e);
            } finally {
                this.socket.close();
            }

        } catch (Exception e) {
            System.out.println("TCP Server"+ "C: Error"+ e);
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
