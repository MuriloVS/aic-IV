# A Maze'n Game (Em Desenvolvimento)

Projeto desenvolvido para a disciplina de Atividade de Integração Curricular 4 (AIC 4) do curso de Engenharia de Computação - FURG. A Maze'n Game é o MVP de um jogo onde o objetivo é encontrar a saída de uma labirinto gerado proceduralmente através de backtracking. O jogo pode ser jogado no mode singleplayer ou multiplayer.

## Desenvolvido por

- Augusto Cardoso Setti
- Murilo Vitória da Silva

## Instalando requirements

Os requisitos ou dependências para a execução do jogo estão disponíveis no arquivo 'requirements.txt'. Para que a aplicação seja executada é necessário:

- Ter a versão 3.9 (ou superior) do python instalada.
- Usar o comando para instalar a lista de requerimentos<br>

``` pip install -r requirements.txt	```

## Executando o jogo

O jogo pode ser executado através do comando:<br>

``` python main.py ```

## Como jogar

- Setas: Movimentação do jogador
- Enter: Acessa ítem no menu
- Escape: Retorna a cena anterior

## Observações

- Para testar o jogo no modo multiplayer é necessário executá-lo em dois terminais. Na primeira janela acesse multiplayer>create room e aguarde até que o jogo carregue. No segundo acesse multiplayer>connect room.


## Funcionalidades a serem implementadas

    - Continuar a implementar menus
    - Tela Lobby
    - Tela Carregamento
    - Tela Game Over
    - Tela Vencedor
    - Buscar artes
    - Buscar sons
    - Dinâmica de captura de ítens
    - Criar executável (Sem mostrar terminal)

    - Modificar servidor para hospedagem em um host online
    - Implementar obstáculos
    - Implementar relógio
    - Redesenhar menus
    - Implementar animação
    - Capturar e imprimir em cima do jogador nome do cliente
    - Revisar resize e posição dos objetos em outras resoluções
    - Implementar multiplayer local