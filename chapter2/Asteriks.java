import java.util.Scanner;

public class Asteriks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive integer: ");
        int n = scanner.nextInt();
        

        if (n <= 0) {
            System.out.println("Please enter a positive integer.");
        } else {
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < i; j++) {
                    System.out.print("* ");
                }
                System.out.println();
            }
        }
    }
}
