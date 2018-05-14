import java.util.ArrayList;

import java.net.ServerSocket;
import java.net.Socket;

public class ServidorTCP{
	Servidor p;
	ArrayList<ServidorTCPThread> alh; //hijos
	int num;
	public static final int PUERTO = 4444;
	
	public ServidorTCP(Servidor s){
		this.p = s;
	}
	public void iniciar(){
		System.out.println("STCP");
		try{
            System.out.println("TCP Server"+"S : Connecting...");
            ServerSocket serverSocket = new ServerSocket(PUERTO);
            alh = new ArrayList<ServidorTCPThread>();
            num = 0;
            while(true){
                Socket client = serverSocket.accept();
                System.out.println("TCP Server"+"S: Receiving...");
                System.out.println("Engendrado " + num);
                alh.add(new ServidorTCPThread(this,num,client));
                num++;
                new Thread(alh.get(alh.size()-1)).start();
                System.out.println("Nuevo conectado:"+num+" jugadores conectados");
            }
        }catch( Exception e){
            System.out.println("Error"+e.getMessage());
        }finally{

        }
	}
	public void enviarAll(Mensaje m){
		System.out.println("enviarAll:"+alh.size());
		for(int i=0;i<alh.size();i++){
			alh.get(i).enviar(m);
		}
	}
}
