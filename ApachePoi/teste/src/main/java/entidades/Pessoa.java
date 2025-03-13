package entidades;



import lombok.Getter;
import lombok.Setter;
import lombok.Builder;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

@Getter
@Setter


public class Pessoa {

    private String nome;
    private String cpf;
    private String nomeResponsavel;
    private LocalDate dataNascimento;

    private static final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    public Pessoa(String nome, String cpf, String nomeResponsavel, String dataNascimento){
        this.nome = nome;
        this.cpf = cpf;
        this.nomeResponsavel = nomeResponsavel;
        this.dataNascimento = LocalDate.parse(dataNascimento,formatter);
    }

    public void mostrarInfo(){

        System.out.println("Nome: "+ getNome()+ "\n CPF: "+ getCpf() + "\n Nome do Responsável: "+ getNomeResponsavel()+"\n Data de " +
                "Nascimento: "+ getDataNascimento());

    }







}
