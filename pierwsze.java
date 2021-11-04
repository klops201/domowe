import java.util.*;
import java.util.Scanner;
public class kolo {
    public static void main(String[] args) {

            ArrayList<Integer> liczby = new ArrayList<>();
            Scanner in = new Scanner(System.in);
            System.out.println("podaj ilosc liczb (n): ");
            Integer n = in.nextInt();
            int x = 0;
            while(x <= n-1){
                System.out.println("podaj liczbe: ");
                Integer y = in.nextInt();
                liczby.add(y);
                x += 1;
            }
            System.out.println("liczby pierwsze to: ");
            showPrimes(n, liczby);
            }

    static void showPrimes(int p, List<Integer> list){


        for(int t=0; t<=p-1; t++){
            int m = list.get(t);
            if(m == 2){System.out.println("2");}
            if (m > 2) {
                    int dzielniki = 0;
                    if (m % 2 == 1) {
                        for (int j = 1; j <= m; j++) {
                            if (m % j == 0) {
                                dzielniki += 1;
                            }

                        }
                        if (dzielniki == 2) {
                        System.out.println(m);
                        }

                    }
            }
        }

}}
