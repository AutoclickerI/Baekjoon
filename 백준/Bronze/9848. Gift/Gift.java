import java.util.*;
public class Main {
    public static void main(String[] args) {
        int n,k,t1,t2,ans=0;
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();k=sc.nextInt();
        t1=sc.nextInt();
        for(int i=1;i<n;i++){
            t2=sc.nextInt();
            if (t1-t2>=k)
                ans+=1;
            t1=t2;
        }
        System.out.println(ans);
    }
}