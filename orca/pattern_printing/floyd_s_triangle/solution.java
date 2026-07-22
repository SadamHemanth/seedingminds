import java.util.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int N=s.nextInt();
        int a=1;
        for(int i=0;i<=N;i++)
         {
            for(int j=0;j<i;j++){
                System.out.print(a++);
                if(j<i-1){
                    System.out.print(" ");
                }
            }
               System.out.println("");
         }
    }
}    