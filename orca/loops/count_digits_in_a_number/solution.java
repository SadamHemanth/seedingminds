import java.util.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int N=s.nextInt();
        int i=0;
        while(N!=0)
        {
           N=N/10;
           i++;
        };
        System.out.println(i);
    }
}