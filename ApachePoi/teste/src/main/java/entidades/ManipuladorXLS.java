package entidades;

import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellStyle;
import org.apache.poi.ss.usermodel.IndexedColors;
import org.apache.poi.ss.usermodel.Row;

import java.io.*;

import java.util.Iterator;
import java.util.Scanner;

public class ManipuladorXLS {


    private static Row linha;
    private static Cell celula;

    public void criarPasta(){
        File repoPath = new File("c:\\frequencia");

        if(!repoPath.exists()){
            repoPath.mkdir();
            System.out.println("Repositório criado com sucesso");
        }
        else{
            System.out.println("O repositório já existe");
        }

    }

    public void configXLS()  {

        HSSFWorkbook workbook = new HSSFWorkbook(); // criamos um novo arquivo do tipo xls
        HSSFSheet planilha = workbook.createSheet("pessoas"); // planilha criada, porém ainda não foi salva em disco


        planilha.setDefaultColumnWidth(50); // configuração da largura das colunas
        planilha.setDefaultRowHeight((short)500); // configuração da altura das linhas


        CellStyle headerStyle = workbook.createCellStyle(); // config do header
        headerStyle.setFillForegroundColor(IndexedColors.GREY_25_PERCENT.getIndex()); // cor do header

        linha = planilha.createRow(0); //criação da linha 0
        celula = linha.createCell(0); //criação da célula 0
        celula.setCellStyle(headerStyle); // aplicação do estilo header
        celula.setCellValue("Nome"); // valor da célula 0

        celula = linha.createCell(1); //criação da célula 1
        celula.setCellStyle(headerStyle); // aplicação do estilo header
        celula.setCellValue("CPF"); // valor da célula 2

        celula = linha.createCell(2); //criação da célula 1
        celula.setCellStyle(headerStyle); // aplicação do estilo header
        celula.setCellValue("Responsável"); // valor da célula 2

        celula = linha.createCell(3); //criação da célula 2
        celula.setCellStyle(headerStyle); // aplicação do estilo header
        celula.setCellValue("Data Nascimento"); // valor da célula 1

        try{
            FileOutputStream out = new FileOutputStream(new File("c:\\frequencia\\pessoas.xls"));
            workbook.write(out);
            out.close();
            workbook.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        }
        catch (IOException e){
            System.out.println("Erro ao salvar o arquivo");
        }

    }

    public void addPessoas(){
        Scanner sc = new Scanner(System.in);

        int rowNum = quantPessoas() + 1;


        try(FileInputStream arquivo = new FileInputStream(new File("c:\\frequencia\\pessoas.xls"))){

            HSSFWorkbook workbook = new HSSFWorkbook(arquivo);
            HSSFSheet planilha = workbook.getSheetAt(0); // pegamos a planilha 0




            System.out.println("Qauntidade de pessoas a serem adicionadas: ");
            int quantidade = sc.nextInt();
            sc.nextLine();
            for (int i = 0; i < quantidade; i++){

                System.out.println("-------------------");
                System.out.print("Nome:");
                String nome = sc.nextLine();
                System.out.print("CPF: ");
                String cpf = sc.nextLine();
                System.out.print("Responsável: ");
                String nomeResponsavel = sc.nextLine();
                System.out.println("Data de nascimento dd/MM/yyyy");
                String dataNascimento = sc.nextLine();


                linha = planilha.createRow(rowNum);
                celula = linha.createCell(0);
                celula.setCellValue(nome);

                celula = linha.createCell(1);
                celula.setCellValue(cpf);

                celula = linha.createCell(2);
                celula.setCellValue(nomeResponsavel);

                celula = linha.createCell(3);
                celula.setCellValue(dataNascimento);


                rowNum++;

            }

            FileOutputStream out = new FileOutputStream(new File("c:\\frequencia\\pessoas.xls"));
            workbook.write(out);
            out.close();
            arquivo.close();
            workbook.close();

        }
        catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado aaaaaaaa");
        }
        catch (IOException e){
            System.out.println("Erro ao salvar o arquivo bbbbbbbbb");
        }
        finally {
            sc.close();
        }
    }

    public void removePessoas(){
        Scanner sc = new Scanner(System.in);

        int rowNum = quantPessoas() + 1;

        System.out.println("Digite o nome ou cpf da pessoa que deseja remover: ");
        String info = sc.nextLine();

        try(FileInputStream arquivo = new FileInputStream(new File("c:\\frequencia\\pessoas.xls"))){

            HSSFWorkbook workbook = new HSSFWorkbook(arquivo);
            HSSFSheet planilha = workbook.getSheetAt(0); // pegamos a planilha 0


            Iterator <Row> rowIterator = workbook.getSheetAt(0).iterator();

            while(rowIterator.hasNext()){
                linha = rowIterator.next();
                if (linha.getRowNum() == 0){
                    continue;
                }
                if(linha.getCell(0).getStringCellValue().equals(info) || linha.getCell(1).getStringCellValue().equals(info)){

                    //loop pode ser simlpificado
                    linha.removeCell(linha.getCell(0));
                    linha.removeCell(linha.getCell(1));
                    linha.removeCell(linha.getCell(2));
                    linha.removeCell(linha.getCell(3));
                    System.out.println("Pessoa removida");

                    FileOutputStream out = new FileOutputStream(new File("c:\\frequencia\\pessoas.xls"));
                    workbook.write(out);
                    out.close();
                    arquivo.close();
                    workbook.close();
                    break;
                }
            }
            System.out.println("Pessoa Nao encontrada");

        }
        catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        }
        catch (IOException e){
            System.out.println("Erro ao salvar o arquivo");
        }
        finally {
            sc.close();
        }



    }

    public void procurarPessoa(){
        try(FileInputStream arquivo = new FileInputStream(new File("c:\\frequencia\\pessoas.xls"))){
            Scanner sc = new Scanner(System.in);

            System.out.print("Digite o nome: ");
            String nome = sc.nextLine();

            HSSFWorkbook workbook = new HSSFWorkbook(arquivo);
            HSSFSheet planilha = workbook.getSheetAt(0); // pegamos a planilha 0

            Iterator<Row> Linhas = planilha.iterator();

            while (Linhas.hasNext()){

                linha = Linhas.next();
                if(linha.getRowNum() == 0){
                    continue;
                }

                if(linha.getCell(0).getStringCellValue().equals(nome)){

                    String nomePessoa = linha.getCell(0).getStringCellValue();
                    String cpf = linha.getCell(1).getStringCellValue();
                    String nomeResponsavel = linha.getCell(2).getStringCellValue();
                    String dataNascimento = linha.getCell(3).getStringCellValue();


                    Pessoa pessoa = new Pessoa(nomePessoa,cpf,nomeResponsavel,dataNascimento);
                    pessoa.mostrarInfo();

                    break;
                }
                else{
                    System.out.println("Pessoa não encontrada");
                }



            }



        }
        catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        }
        catch (IOException e){
            System.out.println("Erro ao salvar o arquivo");
        }


    }

    private int quantPessoas(){

        int quantidade = 0;

        try(FileInputStream arquivo = new FileInputStream(new File("c:\\frequencia\\pessoas.xls"))) {
            HSSFWorkbook workbook = new HSSFWorkbook(arquivo);
            HSSFSheet planilha = workbook.getSheetAt(0); // pegamos a planilha 0


            Iterator <Row> rowIterator = planilha.iterator(); // rowIterator é um iterador de linhas, ou seja vai percorrer as linhas

            while(rowIterator.hasNext()){ // enquanto houver linhas para percorrer
               linha = rowIterator.next(); // pega a proxima linha

                if(linha.getRowNum() == 0){ //descarta o Header
                    continue;
                }
                quantidade++;
            }


        }
        catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        }
        catch (IOException e){
            System.out.println("Erro ao salvar o arquivo");
        }


        return quantidade;
    }

}
