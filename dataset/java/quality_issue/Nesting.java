
public class JavaBad02_Nesting {
    public static void check(int x) {
        if (x > 0) {
            if (x < 100) {
                if (x % 2 == 0) {
                    System.out.println("Even");
                }
            }
        }
    }
}
