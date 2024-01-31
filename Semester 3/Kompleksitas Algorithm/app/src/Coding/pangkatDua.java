package Coding;

import java.util.Scanner;

public class pangkatDua {
    public static int hitungPangkatDua(int bilangan){
        int hasil = 1;
        for(int i = 0; i < 2; i++){
            hasil *= bilangan;
        }
        return hasil;
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("Masukkan bilangan: ");
        int bilangan = input.nextInt();
        
        int hasilPangkatDua = hitungPangkatDua(bilangan);
        System.out.println("Hasil" + bilangan + "Pangkat Dua adalah: " + hasilPangkatDua);
    }
}

