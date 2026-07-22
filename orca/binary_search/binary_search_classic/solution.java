import java.util.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       Scanner s = new Scanner(System.in);
       String b = s.nextLine();
       String[] arr = b.split(" ");
       int N = arr.length;
       int[] a = new int[N];
       
       for(int i = 0; i < N; i++){
        a[i] = Integer.parseInt(arr[i]);
       }
       
       int T = s.nextInt();
       int f = 0, l = N - 1, msg = -1;
       
       while(f <= l){
        int m = (f + l) / 2;
        if(a[m] == T){
           msg = m;
           break; 
        }
        else if(a[m] < T){
            f = m + 1;
        }
        else{
            l = m - 1; 
        }
       }
       System.out.println(msg);
    }
}
