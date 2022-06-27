# RPG MAP

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0124099  |  Juliana Pereira Valle Gonçalves |
| 18/0106805  |  Mateus Cunha Maia |

## Sobre 
O projeto mostra a menor rota entre um país e outro em um mapa de RPG, utilizando o algoritmo BFS.

## Apresentação

A apresentação do projeto pode ser vista no seguinte [link](https://youtu.be/neoMKvIZVyU).

## Screenshots

![Tela Inicial](./assets/img_3.jpeg)
</figcaption>
    Imagem 1: Tela Inicial
</figcaption>

![Tela de Resultado](./assets/img_2.jpeg)
</figcaption>
    Imagem 2: Tela de Resultado 1
</figcaption>

![Tela de Resultado](./assets/img_1.jpeg)
</figcaption>
    Imagem 3: Tela de Resultado 2
</figcaption>

## Instalação 
**Linguagem**: python e javascript <br>
**Framework**: react js<br>

Um dos pré requisitos para rodar o projeto é ter o docker e o docker-compose instalados. Outro pré-requisito é ter o python versão 3+.

Para subir o docker basta rodar o camando na pasta backend:
``` shell
$ docker-compose up --build
```

para subir o frontend basta executar os comandos dentro da pasta frontend:
``` shell
$ yarn
```
e
``` shell
$ yarn start
```

E acessar o endereço http://localhost:3000 no seu navegador.

De preferência, utilizar um navegador diferente do Google Chrome.

## Uso 
Escolha o país de origem e o país de destino e aperte o botão enviar. Feito isso, a api retornará o caminho mais otimizado entre os países selecionados.





