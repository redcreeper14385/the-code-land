import java.util.*;
import java.net.*;
import java.io.*;
class ServerT {
	public static StringBuilder place = new StringBuilder("_________");
	public static char this_team = 'X';
	public static int win[] = {1,2,3,4,5,6,7,8,9,1,4,7,2,5,8,3,6,9,1,5,9,7,5,3};

	public static void showBoard() throws Exception
	{
		new ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();
		System.out.println("\n\t    Welcome to TicTacToe\n\n");
		System.out.println("\t          Player (X)\n");
		System.out.println("\t\t.-----------.");
		System.out.println("\t\t|_"+place.charAt(0)+"_|_"+place.charAt(1)+"_|_"+place.charAt(2)+"_|");
		System.out.println("\t\t.           .");
		System.out.println("\t\t|_"+place.charAt(3)+"_|_"+place.charAt(4)+"_|_"+place.charAt(5)+"_|");
		System.out.println("\t\t.           .");
		System.out.println("\t\t|_"+place.charAt(6)+"_|_"+place.charAt(7)+"_|_"+place.charAt(8)+"_|");
		System.out.println("\t\t'-----------'");
	}

	public static void setupGame()
	{
		place = new StringBuilder("_________");
		try {
			playGame();
		}
		catch(Exception e) {}
	}

	public static boolean checkWin(char player) {
		int i = 0;
		while(i<23) {
			if(place.charAt(win[i]-1)==player && place.charAt(win[i+1]-1)==player && place.charAt(win[i+2]-1)==player)
				return true;
			i+=3;
		}
		return false;
	}

	public static void move(char player) throws Exception {
		int index = -1;
		System.out.print("\nEnter your move (1-9) : ");
		do {
			Scanner keyboard = new Scanner(System.in);
			while(!keyboard.hasNext("[1-9]"))
			{
				showBoard();
				System.out.println("Please enter valid input!");
				System.out.print("Enter your move (1-9) : ");
				keyboard.next();
			}
			index = keyboard.nextInt();
		} while(place.charAt(index-1)!='_');
		
		place.setCharAt(index-1,player);
	}

	public static void playGame() throws Exception
	{
		byte buffer[] = null;
		DatagramSocket ds_send = new DatagramSocket();
		InetAddress ip = InetAddress.getLocalHost(); //InetAddress.getByName("192.168.43.47"); //client IP
		DatagramSocket ds_receive = new DatagramSocket(4100); //serverPort

		for(int i=0;i<9;i++) {
			if(this_team=='X') {
				move('X');
				buffer = new byte[1024];
				String s = new String(place);
				buffer = s.getBytes();
				DatagramPacket dp_send = new DatagramPacket(buffer,buffer.length,ip,3100);
				ds_send.send(dp_send);
				
				if(checkWin('X'))
				{
					showBoard();
					System.out.println("X wins!");
					break;
				}
				this_team = 'O';
			}
			else {
				System.out.println("\nWait for opponent move!");
				buffer = new byte[1024];
				DatagramPacket dp_receive = new DatagramPacket(buffer,buffer.length);
				ds_receive.receive(dp_receive);
				String s = new String(dp_receive.getData());
				place = new StringBuilder(s);

				if(checkWin('O'))
				{
					showBoard();
					System.out.println("O wins!");
					break;
				}
				this_team = 'X';
			}
			showBoard();
		}
		if(!checkWin('O') && !checkWin('X')) {
			System.out.println("Match Draw!");
		}
	}
	public static void main(String args[]) throws Exception {
		showBoard();
		setupGame();
	}
}