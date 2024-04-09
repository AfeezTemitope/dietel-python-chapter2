import java.util.Scanner;

public class StudentScores {
    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);
        int passCount = 0;
        int failCount = 0;

        for (int i = 1; i <= 15; i++) {
            try {
                System.out.print("Enter score for student " + i + ": ");
                double score = scanner.nextDouble();
                if (score >= 45) {
                    passCount++;
                } else {
                    failCount++;
                }
            } catch (Exception e) {
                System.out.println("oga enter valid score jhoor!!.");
                scanner.nextLine(); 
                i--;
            }
        }

        System.out.println("Number of students who passed: " + passCount);
        System.out.println("Number of students who failed: " + failCount);
    }
}
