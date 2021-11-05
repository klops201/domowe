package com.company;
import java.util.Scanner;
public class zad1 {

    public static int findPrimes(int[] list)
    {
        int licznik = 0;
        int wynik =0;
        for (int i=0;i<list.length;i++)
        {
            for (int j=2; j<=list[i]/2;j++)
            {
                if(list[i]%j==0)
                    licznik++;
            }
            if(licznik==0)
                wynik++;

            licznik=0;
        }
        return wynik;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] list = new int[n];
        for (int i=0;i<n;i++)
        {
            list[i]=i+1;
            System.out.println(list[i]);
        }
        System.out.println("w tablicy jest "+findPrimes(list)+ " liczb pierwszych");



    }
}
