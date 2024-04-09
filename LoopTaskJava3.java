public class LoopTaskJava3{
	public static void main(String... args){
	
	long count = 1;
	System.out.println("Even numbers between 1 - 100: ");

	while(count <= 100){
		if(count % 2 == 0){
			System.out.printf("%4d", count);	
		}
		count++;

	}
}


}