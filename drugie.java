import java.util.ArrayList;
import java.util.Scanner;

public class zad2 {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        System.out.println("podaj ilosc liczb (n): ");
        Integer n = in.nextInt();
        System.out.println("najwiekszy element w tablicy oraz ile razy wystapil: ");
        max(n);

    }

    public static void max(int m){
        ArrayList<Integer> liczby = new ArrayList<>();
        int ile = 0;
        int max = 50;
        int min = -50;
        while(ile <= m-1){
            int x = (int)Math.floor(Math.random()*(max-min+1)+min);
            System.out.println(x);
            liczby.add(x);
            ile += 1;
        }
        int maxi = 0;
        for(int i=0;i<m-1;i++){
            int y = liczby.get(i);
            if(y > maxi){maxi=y;}
        }
        System.out.println("najwieksza wart: " + maxi);
        int ileR = 0;
        for(int i=0;i<ile;i++){
            if(liczby.get(i) == maxi){ileR += 1;}
    }
        System.out.println(ileR);
//        return ileR;
    }
    }
