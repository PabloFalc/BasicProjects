#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>



int acao, class , Dano , Cura, VidaPlayer , VidaTotal;
int VidaMonstro, DanoMonstro, Enemy;
int Xp = 0;
int XpInimigo;
char Nome[20];
char NomeMonstro [10];
int QuantCura = 5;
int CuraTOTAL = 5;
int jornada;
int PoderCurar = 2;
int LevelUp = 5;
int senha;

//função de escolher classe

int Class(){

    

    
    

    printf("\nEscolha sua classe: \n 1 - Pythonzero \n 2 - Javascripter\n 3 - Maculado\n\nClasse: ");
    scanf("%d",&class);
      

        switch (class){

            case 1:

                VidaPlayer = 15;
                Dano = 10;
                VidaTotal = 15;
                Cura = 5;

                printf("\n");
                printf("--> vc aprendeu a arte da guerra %s\n--> Agora vc se tornou um Gueirro\n", Nome);
                break;
                
            
            case 2:

                VidaPlayer = 8;
                Dano = 15;
                VidaTotal = 3;
                Cura = 10;

                printf("\n");
                printf("--> vc aprendeu os segredos da magia %s\n--> Agora vc se tornou um Mago\n", Nome);
                break;
                
            case 3:
                
                VidaPlayer = 20;
                Dano = 5;
                VidaTotal = 20;
                Cura = 10;

                printf("\n");
                printf("--> Bem-vindo de volta as Terras Intermédias Maculado %s\n", Nome);
                break;
            case 4:

                printf("\n");
                scanf("%d", &senha);
                if (senha == 30042004)
                {
                    Dano = 999999999;
                    VidaPlayer = 999999999;
                    VidaTotal = 999999999;
                    Cura = 999999999;

                    printf("BEM-VINDO DE VOLTA MESTRE!!!\n");
                    printf("PPRT, vtnc que linguagem complicada, pythonzin amassava na hora de criar um rpgzin");
                    
                }
                else if (senha != 30042004)
                {
                    Class();                   
                }
                break;
                
                
               


            default: 

                printf("Essa classe não existe\n");
                Class();
                break;
        }

    return 0;
}

int inimigos(){

    

    
    printf("\n");
    printf("Qual inimigo vc quer enfrentar?\n ");
    printf("\n1 - Anão\n2 - Esqueleto\n3 - Zumbi\n4 - Cerberus\n5 - Capeta\n\niniciativa: ");
    scanf("%d", &Enemy);

    switch (Enemy){
        
        case 1:
            
            VidaMonstro = 23;
            DanoMonstro = 2;
            XpInimigo = 1;
            strcpy (NomeMonstro, "Anão");
            break;
           
        
        case 2:
            
            VidaMonstro = 50;
            DanoMonstro = 10;
            XpInimigo = 3;
            strcpy (NomeMonstro, "Esqueleto");
            break;

        case 3:

            VidaMonstro = 90;
            DanoMonstro = 25;
            XpInimigo = 20;
            strcpy (NomeMonstro, "Zumbi");
            break;

        case 4:

            VidaMonstro = 250;
            DanoMonstro = 150;
            XpInimigo = 666;
            strcpy (NomeMonstro, "Cerberus");
            break;

        case 5:

            VidaMonstro = 6666;
            DanoMonstro = 6666;
            XpInimigo = 6666;
            strcpy (NomeMonstro, "Capeta");
            break;

        default:
            printf("Esse inimigo não existe: \n");
            printf("\n");
            inimigos();
            break;

        
    }

}

int Combate(){
    setlocale(LC_ALL, "pt_BR");

    
    
    printf("\n");
    printf("--> vc se aproxima de um %s", NomeMonstro);
    printf("\n");
    
    while(VidaMonstro >0 || VidaPlayer >0){
        printf ("\n");
        printf("----------------------------------------------------------------------------\n");
        printf("Oq vc vai fazer?\n\n1- Atacar \n2- Curar \n3- fugir\n\niniciativa: ");
        scanf ("%d", &acao);

        switch (acao){

            case 1:
            //Se atacar o monstro ele devolve o dano
                if (VidaMonstro <= Dano){
                    printf("VC DECAPITOU ELE SEM PIEDADE!\n");
                    return 0;
                }

                else{  
                    VidaMonstro -= Dano;
                    printf("--> vc acerta ele e da %d de dano.\n", Dano);
                    

                    printf("\n----> ele te ataca de volta vc toma %d de dano\n\n", DanoMonstro);
                    VidaPlayer -= DanoMonstro;
                    if (VidaPlayer <=0){
                        return 0;
                    }
                }
                break;
            
            
            case 2:
            //cura
                if (QuantCura > 0 && VidaPlayer < VidaTotal){
                    
                    
                    VidaPlayer += Cura;
                    QuantCura -=1;
                    printf("--> vc está com |%d| de vida agora\n", VidaPlayer);
                }
                else{
                    printf("--> Sua vida ja está completa");

                }
                
                
                    
                break;

            case 3:
                printf("vc fugiu da batalha!\n");
                return 0;
                break;
                

            default:
                printf("Essa opção não existe, adicione um valor certo: \n");
                break;

         

        }
        
    } 
    printf("----------------------------------------------------------------------------\n");
            
}

int main(){
    setlocale(LC_ALL, "pt_BR");

    printf("----------------------------------------------------------------------------\n");
    printf("\nBem-vindo ao Jogo de RPG Feito em C (lingugem merda)\n");
    printf("\n");

    printf("Digite o nome do seu personagem:\n--->");
    fgets(Nome,20,stdin);
    

    printf("----------------------------------------------------------------------------\n");

    Class();
    printf("_________________________________\n");
    printf("Vida: %d\nDano: %d\nQuantidade de cura: %d\nCura %d pts de vida\n", VidaPlayer ,Dano , QuantCura , Cura);
    printf("_________________________________\n");
       
    do{
        inimigos();
        Combate();
        if (VidaPlayer > 0){
            Xp+=XpInimigo;
            QuantCura == 5;
            if (Xp >= LevelUp){
                LevelUp = LevelUp + LevelUp + 5;
                Xp ==0;
                VidaTotal += LevelUp;
                VidaPlayer == VidaTotal;
                Dano += LevelUp+2;
                Cura += LevelUp+3;
                printf("\nNOVO LEVEL!!!\n---> Dano atual: %d\n--> Vida Atual: %d\n--> Agora vc cura %d de vida\n", Dano ,VidaPlayer , Cura);
                
                
                
            }
            
            printf("----------------------------------------------------------------------------\n");
            printf("\n");
            printf("vc recuperou suas curas e ganhou %d de XP\n\n--> XP atual: %d\n", XpInimigo, Xp);
            printf("\n");
            printf("\nparabens, quer continuar sua aventura?\n1- sim \n2- nao\n\n Inciativa: ");
            scanf("%d",&jornada);
            printf("----------------------------------------------------------------------------\n");
        }else{
            printf("\n");
            
            printf("\nGAME-OVER, VC PERDEU\n");
            jornada == 1;
            return 0;
        }
    }while (jornada == 1);

    printf("\nobrigado por jogar esse jogo bosta!\n");


        














}
