 // Write here your program
import java.util.Scanner;
 public class MainTest {
 // write a calulator
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        System.out.println("Enter the operation: ");
        String op = sc.next();
        if (op.equals("+")) {
            System.out.println(a + b);
        } else if (op.equals("-")) {
            System.out.println(a - b);
        } else if (op.equals("*")) {
            System.out.println(a * b);
        } else if (op.equals("/")) {
            System.out.println(a / b);
        } else {
            System.out.println("Invalid operation");
        }
    }
 }