# Laboratório 5 de Python: Batalha na Ponte de Piltover
Quinto projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
_______________________________________________________________________________________________________________________________________________________________________
<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004234201312280626/imagem_1.2.jpg?width=950&height=406" />
</p>
<br>

"Uma grande empresa de jogos digitais contratou você para participar do desenvolvimento de um novo jogo a partir da série Arcane, que é uma série animada derivada do jogo League of Legends. 

O seu chefe te alocou em uma das fases do jogo, onde ocorre a luta entre os personagens Jinx e Ekko na ponte da cidade de Piltover.
<br>

Durante o desenvolvimento do jogo, o seu chefe indicou que durante a batalha na ponte de Piltover, Jinx sempre atacará primeiro, já que ela possui uma arma de longa distância, e Ekko sempre atacará depois que Jinx terminar seus disparos. Além disso, caso o personagem que irá atacar tenha menos vida que seu oponente, o ataque efetuado terá apenas metade do poder. Todos os ataques possuem valores inteiros positivos e pares.
Ao final dos ataques dos dois personagens, você precisará indicar se Jinx ganhou a batalha (isso acontece se os pontos de vida de Jinx são maiores que os pontos de vida de Ekko), se Ekko ganhou a batalha (caso os pontos de vida de Ekko sejam maiores que os pontos de vida de Jinx), ou se houve empate (os dois possuem pontos de vida iguais). 
<br>

Se em algum momento da batalha algum dos personagens atingir 0 ou menos pontos de vida, ele não efetuará mais nenhum ataque e nem receberá mais dano, e os pontos de vida deste personagem será igual a 0, além de seu oponente ser declarado como vencedor da batalha.
<br>

O exemplo a seguir mostra Jinx e Ekko começando com 10 pontos de vida.
- Vida Jinx: 10
- Vida Ekko: 10

Na sequência, Jinx efetua dois ataques, sendo que o primeiro ataque tem poder igual a 4.
- Vida Jinx: 10
- Vida Ekko: 6

No segundo ataque de Jinx, o poder é igual a 2.
- Vida Jinx: 10
- Vida Ekko: 4

Ekko irá efetuar quatro ataques. O primeiro deles tem poder igual a 6. Entretanto, como ele possui menos pontos de vida do que Jinx, seu ataque terá poder igual a 3.
- Vida Jinx: 7
- Vida Ekko: 4

No segundo ataque, Ekko irá desferir um golpe de poder igual a 6 novamente. Entretanto, como Ekko possui menos pontos de vida do que Jinx, seu ataque terá poder igual a 3.
- Vida Jinx: 4
- Vida Ekko: 4

Depois, Ekko atingirá Jinx com um poder de ataque igual a 10. Com isso, os pontos de vida de Jinx ficarão negativos. Neste caso, devemos atribuir o valor igual a 0 para os pontos de vida de Jinx.
- Vida Jinx: 0
- Vida Ekko: 4

O último ataque de Ekko possui poder igual a 8. Entretanto, ele não deverá ser contabilizado, já que Jinx perdeu a batalha.
<br>

<b>Neste exemplo, Ekko foi o ganhador do combate.</b><br><br>
:boom: :bomb: :muscle: :martial_arts_uniform: :crossed_swords: :video_game: :dagger: :computer: 
<br>

Seu programa deverá ler nas duas primeiras linhas os pontos de vida de Jinx e Ekko, respectivamente. Na sequência, seu código receberá a quantidade n de ataques que Jinx realizará, seguido por n linhas, indicando os poderes de cada ataque. Depois, seu código deverá ler a quantidade m de ataques de Ekko, seguido por m linhas, indicando os poderes de cada ataque.<br>

Ao final, seu código deverá imprimir os pontos de vida de Jinx e Ekko.
- <b>"Vida da Jinx:</b> ~ pontos de vida da Jinx ~ <b>"</b>
- <b>"Vida do Ekko:</b> ~ pontos de vida do Ekko ~ <b>"</b>

Além disso, seu código deverá imprimir o ganhador da batalha. Caso Jinx tenha vencido, seu código deverá imprimir:
- <b>"Jinx foi a vencedora da batalha"</b>

Caso Ekko tenha vencido, seu código deverá imprimir:
- "Ekko foi o vencedor da batalha"</b>

Caso tenha ocorrido o empate, seu código deverá imprimir:
- <b>"A batalha terminou empatada"</b>
_______________________________________________________________________________________________________________________________________________________________________

<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.
