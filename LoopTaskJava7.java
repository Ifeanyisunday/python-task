import java.util.Scanner;
public class LoopTaskJava7{
	public static void main(String... args){
	Scanner input = new Scanner(System.in);

	int sampleInput = input.nextInt();

	for(int count = sampleInput; count >= 1; count--){
		for(int index = count; index >= 1; index--){
			System.out.printf("%2d", index);
		}
		System.out.println();
	} 
}
}