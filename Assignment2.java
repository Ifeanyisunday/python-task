import java.util.Scanner;

public class Assignment2{
	public static void main(String... args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter the D value: ");
	int d = input.nextInt();
	int c = 50;
	int h = 30;
	int calculate = ((2 * c * d)/h);
	double formula = (Math.pow(calculate, 0.5));
	System.out.printf("%s%.0f", "The square root of ((2 * c * D)/h) is = ",  formula);




}
}