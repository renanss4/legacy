package application;

import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;
        
        while (continuar) {
            System.out.println("Escolha a operação:");
            System.out.println("1. Soma");
            System.out.println("2. Subtração");
            System.out.println("3. Multiplicação");
            System.out.println("4. Divisão");
            System.out.println("5. Sair");
            System.out.print("Opção: ");
            
            int opcao = scanner.nextInt();
            
            if (opcao >= 1 && opcao <= 4) {
                System.out.print("Digite o primeiro número: ");
                double numero1 = scanner.nextDouble();
                System.out.print("Digite o segundo número: ");
                double numero2 = scanner.nextDouble();
                
                double resultado = 0;
                String operacao = "";
                
                switch (opcao) {
                    case 1:
                        resultado = numero1 + numero2;
                        operacao = "soma";
                        break;
                    case 2:
                        resultado = numero1 - numero2;
                        operacao = "subtração";
                        break;
                    case 3:
                        resultado = numero1 * numero2;
                        operacao = "multiplicação";
                        break;
                    case 4:
                        if (numero2 != 0) {
                            resultado = numero1 / numero2;
                            operacao = "divisão";
                        } else {
                            System.out.println("Erro: divisão por zero.");
                            continuar = false;
                        }
                        break;
                }
                
                if (continuar) {
                    System.out.println("O resultado da " + operacao + " é: " + resultado);
                }
            } else if (opcao == 5) {
                continuar = false;
            } else {
                System.out.println("Opção inválida. Por favor, escolha uma opção válida.");
            }
        }
        
        scanner.close();
    }
}
