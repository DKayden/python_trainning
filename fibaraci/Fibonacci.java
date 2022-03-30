import java.util.Scanner;

public class Fibonacci {
public static void main(String[] args) {
    int n;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter number of element: ");
    n = sc.nextInt();
    for (int i = 0; i < n; i++) {
        System.out.print(fibonacci(i) + " ");
    }
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

