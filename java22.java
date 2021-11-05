package com.company;
import java.lang.Math;
import java.util.Scanner;

public class zad2 {

    public static void najmniejszy(int[]tab)
    {
        int min=tab[0];
        int licznik=0;
        for (int i=1;i<tab.length;i++)
        {
            if (tab[i]<min)
                min=tab[i];
        }
        for (int i=0;i<tab.length;i++)
        {
            if (tab[i]==min)
                licznik++;
        }
        System.out.println("najmniejszy element wynosi "+ min+ " wystepuje:"+ licznik+ " razy" );
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] tab= new int[n];
        for (int i=0;i<n;i++)
        {
           tab[i]=(int)((Math.random()*(51+51))-51);
            System.out.println(tab[i]);
        }
        najmniejszy(tab);
    }
}
