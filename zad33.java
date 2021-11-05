package com.company;

public class zad3 {
    public static int delete(String str,String substr)
    {
        StringBuffer buf = new StringBuffer();
        int[] tab= new int[str.length()];
        int licznik=0;
        int pom_licznik=0;
        int wynik=0;
        for (int i=0;i<=str.length()-substr.length();i++)
        {
            for (int j=0;j<substr.length();j++)
            {
                if (str.charAt(i+j)==str.charAt(j))
                    licznik++;
            }
            if (wynik>=1 && licznik==substr.length())
            {
                for (int x=0;x<substr.length();x++)
                {
                    tab[pom_licznik]=i+x;
                    pom_licznik++;
                }
            }
            if (licznik==substr.length())
                wynik++;


            licznik=0;
        }
        buf.append(str);

        int pom=0;
        buf.delete(tab[0]-substr.length(), tab[0+substr.length()]);


        for (int i=0;i<pom_licznik;i++)
        {
            System.out.println(tab[i]);
        }
        System.out.println("wynik:"+buf.toString());
        return wynik;
    }
    public static void main(String[] args)
    {
        String str = "alaalbaalaala";
        String substr = "ala";
        System.out.println(delete(str,substr));
    }
}
