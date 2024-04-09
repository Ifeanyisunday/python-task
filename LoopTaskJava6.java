import java.util.Scanner;
public class LoopTaskJava6{
	public static void main(String... args){
	Scanner input = new Scanner(System.in);

	int sampleInput = input.nextInt();
	
	for(int count = 1; count <= sampleInput; count++){
		for(int index = 1; index <= count; index++){
			System.out.print("*");
		}
		System.out.println();
	}
}
}