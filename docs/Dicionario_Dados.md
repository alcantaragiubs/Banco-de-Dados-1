# Dicionário de Dados

## Nível

| Nome      | Descrição                                                | Tipo de dado | Tamanho | Not null | Check        | Default   | PK  | FK  | Exemplo |
| --------- | -------------------------------------------------------- | ------------ | ------- | -------- | ------------ | --------- | --- | --- | ------- |
| Id  | Identificador do nível                                   | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |           | Sim | Não | 1       |
| Descrição | Descrição e contexto do nível que o jogador está no jogo | Varchar      | 300     | Não      |              |           | Não | Não | Bem vindo ao nível 1. Aqui o jogo inicia. |

## Sala

| Nome    | Descrição                    | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  | Exemplo |
| ------- | ---------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- | ------- |
| Id | Identificador da sala        | Int          |         | Sim      | Id_sala >= 1 |         | Sim | Não | 1       |
| Nome | Nome da sala | Varchar |         | Sim | | | Não | Não | 1
| Descrição    | Nome da sala            | Varchar      | 30      | Sim      |              |         | Não | Não | Nesta sala há um baú com benefícios. |
| Destinos | Possíveis salas para o jogador ir | Int | 10 | Sim | | | Não | Não | ARRAY [2, 0, 4, 0] 
| Id_nivel | Referência ao nivel em que o jogador está | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3            |         | Não | Sim | 3

## Coordenadas

| Nome    | Descrição                    | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  | Exemplo |
| ------- | ---------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- | ------- |
| Id | Identificador único      | Int          |         | Sim      | Id_sala >= 1 |         | Sim | Não | 1       |
| Id_origem | Identificador onde o jogador está na sala | Int          |         | Sim      | Id_sala >= 1 |         | Não | Sim | 1       |
| Id_destino | Identificador para onde o jogador vai | Int          |         | Sim      | Id_sala >= 1 |         | Não | Sim | 1       |


## Jogador

| Nome       | Descrição                                          | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |  Exemplo |
| ---------- | -------------------------------------------------- | ------------ | ------- | -------- | --------------- | ------- | --- | --- |  ------- |
| Id | Identificador do jogador                           | Int          |         | Sim      | Id_jogador >= 1 |         | Sim | Não | 10 |
| Vida       | Saúde do jogador                                   | Int          |         | Sim      |                 | 200     | Não | Não | 10 |
| Progresso  | Progresso do jogador no jogo                       | Varchar      |         | Sim      |                 |         | Não | Não | 50% Concluído |
| Nome      | Nickname do jogador no jogo              | Int          |         | Sim      |                 | 1       | Não | Não | 1326 |
| Ataque     | Potência do ataque do jogador                      | Int          |         | Sim      | ataque > 0      | 100     | Não | Não | 150 |
| Defesa     | Saúde de defesa do jogador                         | Int          |         | Sim      | defesa > 0      | 100     | Não | Não | 150 |
| Id_sala    | Identificador da sala em que o jogador se encontra | Int          |         | Sim      | Id_sala >= 1    | 1       | Não | Sim | 3 |
| Id_nivel   | Identificador do nivel que o jogador está          | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |         | Não | Sim | 2 |
 
## Item

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não | 2        |
| Nome          | Nome do item                                | Varchar      | 100      | Sim      |              |         | Não | Não | Código |
| Descrição | Descrição do item | Varchar | 200 | Sim | | | Não | Não | Esse código será utilizado para desbloquear o próximo nível. Guarde-o com cuidado! |
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2        |
| Id_inventario       | Identificador do inventario                       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2        |


## Arma

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id       | Identificador do item específico                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não | 2        |
| Multi_ataque | Multiplicador para aumentar o ataque do jogador | Float |          | Sim      | mult_ataque > 1 |          | Não | Não | 1.0 |
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2        |

## Mágico

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id       | Identificador do item específico                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não | 2        |
| Multi_vida | Multiplicador para aumentar a vida do usuário | Float |          | Sim      | mult_vida > 1 |          | Não | Não | 2.0 |
| Teletransporte | Libera o poder de teletransporte pelo mapa | Boolean |          | Sim |          |          | Não | Não | 2.0 |
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2        |

## Código

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id       | Identificador do item específico                       | Int          |         | Sim      | Id_item >= 1 |         | Sim | Não | 2        |
| Code          | Código final necessário pra vencer a fase                                | Varchar      | 30      | Sim     |           |       | Não | Não | 30317512 |
| Id_item       | Identificador do item                       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2        |

## Inventário

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id | Identificador do inventario                 | Int          |         | Sim      |Id_inventario >=1 | 6   | Sim | Não | 1 |
| Tamanho_inventario       | Tamanho do inventário                       | Int          |         | Sim      |              |         | Não | Não | 6 |
| Id_item       | Identificador do item do inventário         | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 2 |
| Id_jogador     | Identificador do jogador dono do inventário | Int          |         | Sim      | Id_jogador >= 1 |      | Não | Sim | 520 |

## Baú

| Nome          | Descrição                                   | Tipo de dado | Tamanho | Not null | Check        | Default | PK  | FK  |  Exemplo |
| ------------- | ------------------------------------------- | ------------ | ------- | -------- | ------------ | ------- | --- | --- |  ------- |
| Id        | Identificador do baú                        | Int          |         | Sim      | Id_bau >= 1  |         | Sim | Não | 1 |
| Id_item       | Identificador do item presente no baú       | Int          |         | Sim      | Id_item >= 1 |         | Não | Sim | 3 | 
| Id_sala       | Identificador da sala em que o baú está     | Int          |         | Sim      | Id_sala >= 1 |         | Não | Sim | 2 |


## NPC

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                       | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | --------------------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do NPC                           | Int          |         | Sim      | Id_NPC >= 1                 |         | Sim | Não | 3 |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                             |         | Não | Sim | 4 |
| Nome          | Nome do NPC                                | Varchar      | 20      | Sim      |              |         | Não | Não | Annabeth Chase |
| Fala          | Fala principal do NPC                                | Varchar      | 20      | Sim      |              |         | Não | Não |Você baba enquanto dorme! |


## Inimigo

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                      | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | -------------------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do NPC específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Vida    | Saúde do NPC                                   | Int          |         | Sim      |                            |         | Não | Não | 10 |
| Ataque  | Poder de ataque do NPC                         | Varchar      | 30      | Sim      |                            |         | Não | Não | Chute |
| Id_npc | Identificador do NPC  | Int          |         | Sim      |                            |         | Não | Não | 3 |

## Boss

| Nome    | Descrição                                      | Tipo de dado | Tamanho | Not null | Check           | Default | PK  | FK  |  Exemplo |
| ------- | ---------------------------------------------- | ------------ | ------- | -------- | --------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do inimigo específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Mult_vida | Multiplicador que aumenta a vida do boss     | Float        |         | Sim      | multi_vida > 1  |         | Não | Não | 1.0 |
| Mult_ataque | Multiplicador que aumenta o ataque do boss | Float        |         | Sim      | mult_ataque > 1 |         | Não | Não | 2.0 |
| Id_nivel | Identificador do nível do boss                | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |         | Não | Sim | 3 |
| Id_inimigo | Identificador do inimigo  | Int          |         | Sim      |                            |         | Não | Não | 3 |

## Comum

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check             | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ----------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do inimigo específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Id_inimigo | Identificador do inimigo  | Int          |         | Sim      |                            |         | Não | Não | 3 |

## Amigável

| Nome     | Descrição                                      | Tipo de dado | Tamanho | Not null | Check                         | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------- | ------------ | ------- | -------- | ----------------------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do NPC específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Id_npc | Identificador do NPC  | Int          |         | Sim      |                            |         | Não | Não | 3 |

## Narrador

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check              | Default  | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ------------------ | -------- | --- | --- |  ------- |
| Id  | Identificador do amigavel específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Id_sala | Identificador da sala em que o NPC se encontra | Int          |         | Sim      |                             |         | Não | Sim | 4 |
| Id_amigavel | Identificador do amigavel  | Int          |         | Sim      |                            |         | Não | Não | 3 |

## Amigo

| Nome     | Descrição                                            | Tipo de dado | Tamanho | Not null | Check             | Default | PK  | FK  |  Exemplo |
| -------- | ---------------------------------------------------- | ------------ | ------- | -------- | ----------------- | ------- | --- | --- |  ------- |
| Id  | Identificador do amigavel específico                          | Int          |         | Sim      | Id_inimigo >= 1                |         | Sim | Não | 4 |
| Mult_inventario | Multiplicador que adicina mais espaços no inventário do jogador | Float |          | Sim      | mult_inventario > 1 |         | Não |  Não | 1.0 | 
| Id_jogador   | Identificador do jogador que o NPC acompanha          | Int          |         | Sim      | Id_nivel>= 1 && Id_nivel <=3 |         | Não | Sim | 2 |
| Id_amigavel | Identificador do amigavel  | Int          |         | Sim      |                            |         | Não | Não | 3 |

