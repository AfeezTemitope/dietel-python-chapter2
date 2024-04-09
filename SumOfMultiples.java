public class SumOfMultiples {
    public static void main(String[] args) {
        int totalSum = 0;
        for (int i = 1; i <= 20000; i++) {
            if (i % 10 == 0) {
                totalSum += i;
            }
        }
        System.out.println("The sum of multiples of 10 between 1 and 20,000 is: " + totalSum);
    }
}
