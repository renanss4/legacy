package application;

import java.util.Scanner;

public class VerificarPalindromo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite uma palavra para verificar se é um palíndromo: ");
        String palavra = scanner.nextLine();
        
        if (ehPalindromo(palavra)) {
            System.out.println(palavra + " é um palíndromo.");
        } else {
            System.out.println(palavra + " não é um palíndromo.");
        }
        
        scanner.close();
    }
    
    public static boolean ehPalindromo(String palavra) {
        int i = 0;
        int j = palavra.length() - 1;
        
        while (i < j) {
            if (palavra.charAt(i) != palavra.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        
        return true;
    }
}
