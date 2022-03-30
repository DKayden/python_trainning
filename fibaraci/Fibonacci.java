import java.util.ArrayList;
import java.util.Scanner;

public class Fibonacci {
    static Scanner sc = new Scanner(System.in);
public static int checkInputInt() {
    while (true) {
        try {
            int result = Integer.parseInt(sc.nextLine());
            if (result <= 0) {
                throw  new NumberFormatException();
            }
            return result;
        } catch (NumberFormatException e) {
            System.err.println("Input must be digit.");
            System.out.println("Please try again.");
        }
    }
}

public static int checkInputNumber() {
        System.out.println("Enter number of element: ");
        int n = checkInputInt();
        return n;
    }

public static void main(String[] args) {
    ArrayList<Integer> arr = new ArrayList<>();
    int n = checkInputNumber();
//    int n;
//    Scanner sc = new Scanner(System.in);
//    System.out.println("Enter number of element: ");
//    n = sc.nextInt();
    for (int i = 0; i < n; i++) {
        arr.add(fibonacci(i));
    }
    System.out.print(arr);
}

// Không dùng đệ quy
//    public static int fibonacci(int n) {
//        int a = 0;
//        int b = 1;
//        int c = 1;
//
//        if (n < 0) {
//            return -1;
//        } else if (n == 0 || n == 1) {
//            return n;
//        } else {
//            for (int i = 2; i < n; i++) {
//                a = b;
//                b = c;
//                c = a + b;
//            }
//        }
//        return c;
//    }

// Dùng đệ quy
    public static int fibonacci(int n) {
        if (n < 0) {
            return -1;
        } else if (n == 0 || n == 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n -2);
        }
    }
}

