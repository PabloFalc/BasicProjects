package Main;

import entidades.ManipuladorXLS;

import java.io.File;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        ManipuladorXLS manipulador = new ManipuladorXLS();
        Scanner scanner = new Scanner(System.in);

        manipulador.criarPasta();

        File file = new File("c:\\frequencia\\pessoas.xls");
        if (file.exists()){
            System.out.println("Arquivo encontrado");
        } else {
            manipulador.configXLS();
        }

        System.out.println("1 - Adicionar pessoa, 2 - Remover pessoa, 3 - Procurar Pessoa");
        int opcao = scanner.nextInt();

        switch (opcao){
            case 1:
                manipulador.addPessoas();
                break;
            case 2:
                manipulador.removePessoas();
                break;
            case 3:
                manipulador.procurarPessoa();
                break;
            default:
                System.out.println("Opção inválida");
        }




    }

}
