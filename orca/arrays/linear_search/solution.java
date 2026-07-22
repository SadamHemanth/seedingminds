import java.util.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int N=s.nextInt();
        int[] a =new int[N];
        for(int i=0;i<N;i++){
            a[i]=s.nextInt();
        }
        int K=s.nextInt();
        int l=-1;
        for(int i=0;i<N;i++)
        {
           if(a[i]==K){
             l=i;
             break;
           }
        }
        System.out.println(l);
    }
}