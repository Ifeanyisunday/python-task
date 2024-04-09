public class LoopTaskJava5{
	public static void main(String... args){

	int sampleInput = 6;
	int multiplication = sampleInput;
	int count = 1;
	int index = 1;


	while(count <= 10){
		System.out.println(sampleInput + "x" + count + "=" + multiplication);
		index++;
		multiplication = sampleInput * index;
		count++;

	}
}
}