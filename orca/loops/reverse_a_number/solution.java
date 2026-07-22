import java.util.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
       Scanner s=new Scanner(System.in);
       int N=s.nextInt();
       int r=0;
       while(N!=0)
       {
        int ls=N%10;
        r=r*10+ls;
        N=N/10;
       }
       System.out.println(r);
    }
}