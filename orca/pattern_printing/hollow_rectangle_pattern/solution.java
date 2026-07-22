import java.util.Scanner;

public class HollowRectangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows = scanner.nextInt();
        int cols = scanner.nextInt();
        
        for (int r = 0; r < rows; r++) {
            StringBuilder rowOutput = new StringBuilder();
            for (int c = 0; c < cols; c++) {
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1) {
                    rowOutput.append("*");
                } else {
                    rowOutput.append(" ");
                }

                if (c < cols - 1) {
                    rowOutput.append("");
                }
            }
            System.out.println(rowOutput.toString());
        }
        
        scanner.close();
    }
}
