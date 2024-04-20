import java.util.Scanner;

public class PurchaseCalculatorApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please Enter Customer Name: ");
        String name = input.nextLine();

        
        double totalCost = 0;

        
        for (int i = 1; i <= 3; i++) {
            System.out.print("What is the name of item " + i + ": ");
            String itemName = input.nextLine();
            System.out.print("How much is it: ");
            double itemCost = input.nextDouble();
            totalCost += itemCost;
            input.nextLine(); 
        }

        
        double discountedCost = totalCost >= 200 ? totalCost * 0.9 : totalCost;

        
        System.out.println("\nCustomer Name: " + name);
        System.out.println("\nTotal item\tcost");
        for (int i = 1; i <= 3; i++) {
            System.out.print("What is the name of item " + i + ": ");
            String itemName = input.nextLine();
            System.out.print("How much is it: ");
            double itemCost = input.nextDouble();
            totalCost += itemCost;
            input.nextLine();
            System.out.printf("%-15s %.2f%n", itemName, itemCost);
        }

        System.out.printf("%nTotal cost: %.2f%n", totalCost);
        System.out.printf("Discounted cost: %.2f%n", discountedCost);

        System.out.println("\nThanks for your patronage!");
    }
}
