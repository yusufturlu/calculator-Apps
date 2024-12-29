import java.util.Scanner;

public class App  {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in) ;

        System.out.println("Enter first number: ");
        double num1 = input.nextDouble();
        System.out.println("Enter second number: ");
        double num2 = input.nextDouble();

        System.out.println("Chose an operator (+, -, *, /): ");

        if (input.hasNext()) {
            char operator = input.next().charAt(0);

            switch (operator) {
                case '+':
                    System.out.println("Result: " + (num1 + num2));
                    break;
                case '-':
                    System.out.println("Result: " + (num1 - num2));
                    break;
                case '*':
                    System.out.println("Result: " + (num1 * num2));
                    break;
                case '/':
                    System.out.println("Result: " + (num1 / num2));
                    break;
                default:
                    System.out.println("Invalid operator");
            }
            input.close();
        }

    }

}
