import java.util.Scanner;
public class LoopTaskJava4{
	public static void main(String... args){
	Scanner input = new Scanner(System.in);

	int passed = 0;
	int failed = 0;
	int count = 1;


	while(count <= 15){
		System.out.printf("Enter student's score: ");
		int score = input.nextInt();
		if(score >= 45){
			passed += 1;	
		}else if(score < 45){
			failed += 1;
		}
		count++;

	}
System.out.println("Number of students who passed is " +passed);
System.out.println("Number of students who failed is " +failed);
}

}