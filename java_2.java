import java.util.*;
public class zadania2 {
    public static void main(String[] args) {
//              ZADANIE 1
        System.out.println("------zadanie 1------");
        System.out.println("a)");
        int n = 25;
        List<Double> Ldigits = new ArrayList<>();
        for(double i=0; i<=n; i++){
            Ldigits.add(i);
        }
        int npa = 0;
                for(Double x: Ldigits){
                    if (x % 2 == 1) {
                        npa += 1;
                    }
        }
//        for(Integer x: Ldigits){
//            System.out.println(x);
//        }

        System.out.println("ilosc liczb nieparzystych: " + npa);

        System.out.println("\n");
        System.out.println("b)");

        int spec = 0;
        for(Double x: Ldigits){
            if ((x % 3 == 1) & (x % 5 != 0)) {
                spec += 1;
            }
        }
        System.out.println("ilosc liczb podzielnych przez 3 i niepodzielnych przez 5: " + spec);
        System.out.println("\n");
        System.out.println("c)");

        List<Double> kwadraty = new ArrayList<>();
        for(int i=0; i<=n; i++){
            if (i % 2 == 0) {
                double j = Math.pow(i, 2);
                kwadraty.add(j);
            }
        }
        for(Double y: kwadraty){
            System.out.println(y);
        }
        int c = 0;
        for(Double x: Ldigits){
            for(Double y: kwadraty){
                if (x == y){
                  c += 1;
                }
            }
        }

        System.out.println("ilosc liczb ktore sa kwadratami liczby parzystej: " + c);

    }
}
