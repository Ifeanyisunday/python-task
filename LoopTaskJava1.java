public class LoopTaskJava1{
	public static void main(String... args){
	
	long multiple = 0;
	long count = 1;
	
	while(count <= 20000){
		if(count % 10 == 0){
			multiple += count;	
		}
		count++;

	}
	System.out.print("The sum of multiples of 10 from 1 - 20,000 is "+multiple);
}


}