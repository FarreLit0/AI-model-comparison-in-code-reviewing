
public class JavaClean02_Factorial {
    public static int factorial(int n) {
        if (n == 0) return 1;
        return n * factorial(n - 1);
    }
}
