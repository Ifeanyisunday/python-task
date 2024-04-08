<<<<<<< HEAD
import java.util.Scanner;

public class Assignment1{
	public static void main(String... args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter price: ");
	int price = input.nextInt();

	System.out.println("Enter discount percentage: ");
	double discountPercentage = input.nextFloat();
	
	double calculateDiscount = price * discountPercentage;

	double getDiscount = price - calculateDiscount;
	
	System.out.printf("%s%.1f", "The new price after discount is = ",  getDiscount);




}
=======
import java.util.Scanner;

public class Assignment1{
	public static void main(String... args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter price: ");
	int price = input.nextInt();

	System.out.println("Enter discount percentage: ");
	double discountPercentage = input.nextFloat();
	
	double calculateDiscount = price * discountPercentage;

	double getDiscount = price - calculateDiscount;
	
	System.out.printf("%s%.1f", "The new price after discount is = ",  getDiscount);




}
>>>>>>> 37f5bb5d8452cb40f3a8f9fad63707cca77afc44
}