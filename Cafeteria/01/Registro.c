#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

// Definindo a estrutura para uma conta de usuário
struct Conta {
    char usuario[50]; // Nome de usuário
    char senha[30];   // Senha
};

// Função para registrar uma nova conta de usuário
void registrarConta(struct Conta contas[], int *numContas) {
    printf("Digite o nome de usuário: "); // comentario
    scanf("%s", contas[*numContas].usuario); // Lendo o nome de usuário
    printf("Digite a senha: "); // comentario
    scanf("%s", contas[*numContas].senha);   // Lendo a senha
    (*numContas)++; // Incrementando o número total de contas
    printf("Conta registrada com sucesso!\n"); // comentario
}

// Função para acessar uma conta existente
void acessarConta(struct Conta contas[], int numContas) {
    char usuario[50];
    char senha[30];
    printf("Digite o nome de usuário: "); // comentario
    scanf("%s", usuario); // Lendo o nome de usuário
    printf("Digite a senha: "); // comentario
    scanf("%s", senha);   // Lendo a senha
    
    // Procurando a conta no array de contas
    int i;
    for (i = 0; i < numContas; i++) {
        if (strcmp(usuario, contas[i].usuario) == 0 && strcmp(senha, contas[i].senha) == 0) {
            printf("Conta acessada com sucesso!\n"); // comentario
            return;
        }
    }
    
    printf("Nome de usuário ou senha incorretos.\n"); // comentario
}

// Função para recuperar a senha de uma conta
void esqueceuSenha(struct Conta contas[], int numContas) {
    char usuario[50];
    printf("Digite o nome de usuário: "); // comentario
    scanf("%s", usuario); // Lendo o nome de usuário
    
    // Procurando o nome de usuário no array de contas
    int i;
    for (i = 0; i < numContas; i++) {
        if (strcmp(usuario, contas[i].usuario) == 0) {
            printf("A senha para o usuário '%s' é: %s\n", contas[i].usuario, contas[i].senha); // comentario
            return;
        }
    }
    
    printf("Nome de usuário não encontrado.\n"); // comentario
}

int main() {
    int opcao;
    struct Conta contas[100]; // Array para armazenar as contas de usuário
    int numContas = 0;        // Número atual de contas
    
    do {
        // Menu de opções
        printf("┌--------------------------------------------┐\n");
        printf("|            ♙ Acesso a conta ♙              |\n");
        printf("|                                            |\n");
        printf("|  [1] Registrar conta    [2] Acessar conta   |\n");
        printf("|                                            |\n");
        printf("|  [3] Esqueceu a senha   [4] Fechar painel   |\n");
        printf("|                                            |\n");
        printf("└--------------------------------------------┘\n");
        
        scanf("%d", &opcao); // Lendo a opção escolhida pelo usuário
        
        switch(opcao) {
            case 1:
                registrarConta(contas, &numContas);
                break;
            case 2:
                acessarConta(contas, numContas);
                break;
            case 3:
                esqueceuSenha(contas, numContas);
                break;
            case 4:
                printf("Fechando painel...\n"); // comentario
                break;
            default:
                printf("Opção inválida. Tente novamente.\n"); // comentario
        }
    } while (opcao != 4); // O loop continua até que o usuário escolha fechar o programa
    
    return 0;
}
