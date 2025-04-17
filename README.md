# Sistema de Dublagem em Tempo Real

## Motivação do Projeto

Após incontáveis horas assistindo ao YouTube com anúncios — sempre os mesmos cursos de inglês para desenvolvedores — algo começou a testar minha paciência. Sabendo que a única linguagem que realmente interessa a esse público é aquela que *compila sem warnings*, decidi revisitar alguns conhecimentos dos tempos de faculdade sobre sistemas distribuídos.

Foi assim que nasceu esta primeira versão do sistema. Ainda me custa acreditar que alguém além de mim vá usá-lo, mas segue firme no processo de testes. A proposta é simples (e um tanto ousada): criar uma solução eficiente para comunicação em múltiplos idiomas, operando de forma descentralizada — algo que, imagino, deixaria o tio Tanenbaum orgulhoso.

### O que é o projeto?

Este projeto propõe o desenvolvimento de um sistema de dublagem em tempo real, distribuído e full-duplex, capaz de permitir diálogos naturais entre falantes de diferentes idiomas **sem recorrer à tradução direta**. Em vez disso, o sistema constrói uma **linguagem intermediária universal**, fundamentada em morfismos e estruturas formais, o que possibilita a reconstrução da fala em qualquer idioma de destino com fidelidade semântica e morfológica.

Dessa forma, não se trata exatamente de um sistema de dublagem no sentido tradicional, mas sim de algo mais próximo do que o cérebro humano faz: quando nos comunicamos, não “traduzimos” palavra por palavra, mas organizamos o pensamento em tempo real, usando o idioma apenas como instrumento. A proposta é replicar essa inteligência estrutural de modo computacional.

Em outras palavras, este framework rompe com o paradigma da tradução literal. Ele parte do princípio de que **a linguagem é uma estrutura universal**, enquanto os idiomas são apenas **representações formais e locais** dessa estrutura.

---

## Arquitetura e Design

![alt text](image.png)

> *Alt text: Um projeto com dois módulos e um plano secreto de eliminar um deles futuramente.*

### Canais (C)

A arquitetura baseia-se em múltiplos canais full-duplex, onde cada canal realiza tanto a codificação quanto a decodificação. Cada canal recebe um **objeto de valor especial**, responsável por encapsular as informações linguísticas essenciais. Esse objeto, que chamo com carinho de **objeto mórfico**, é o produto de operações estruturais baseadas em morfemas.

O objeto mórfico carrega consigo um bloco de dados contendo um conjunto de **instruções genéticas** interpretáveis por qualquer canal, desde que no idioma adequado.

Atualmente, estamos trabalhando com dois canais básicos:

- **PT-BR** (Português)
- **EN** (Inglês)

Cada canal possui um idioma de entrada e outro de saída. O canal de entrada utiliza o microfone padrão do sistema para capturar e transmitir a voz. O canal de saída — atualmente em desenvolvimento — será um driver de áudio virtual que poderá ser integrado a plataformas como o Google Meet.

---

### Barramento (B)

O barramento é, por enquanto, uma **estrutura provisória** de multiplexação dos dados. Ainda não conta com mecanismos robustos de sincronização, mas cumpre seu papel nesta fase inicial do projeto.

Em versões futuras, o sistema será migrado para um ambiente **Kubernetes (K8s)**, onde cada canal será executado como um microserviço serverless. Nesse cenário, o barramento poderá ser eliminado por completo, com os canais operando de forma direta e autônoma.

---

## Como Utilizar

Por enquanto, o sistema é uma **prova de conceito (POC)**. Para testá-lo localmente, basta executar:

```bash
docker-compose up --build
```

O sistema iniciará automaticamente e tudo o que for falado em português será reproduzido em inglês em tempo real.

---

## Notas Finais

Este projeto ainda está em sua infância, mas já vislumbro várias possibilidades para as próximas fases. Aos poucos, vou refinando as ideias, testando novas abordagens e, quem sabe, transformando essa curiosidade pessoal em uma ferramenta real para facilitar a comunicação entre mundos linguísticos.

## Notas para não esquecer

Futuramente pretendo implementar:

- Drive virtual para utilizar em video chamada
- Feature de personalização da voz de saída para ser a mesma de quem fala.
- Rede social a nível global para falantes nativos de indionas desconhecido poder criar seus próprios canais.

# Sistema de Dublagem em Tempo Real

## Motivação do Projeto

Após incontáveis horas assistindo ao YouTube com anúncios — sempre os mesmos cursos de inglês para desenvolvedores — algo começou a testar minha paciência. Sabendo que a única linguagem que realmente interessa a esse público é aquela que *compila sem warnings*, decidi revisitar alguns conhecimentos dos tempos de faculdade sobre sistemas distribuídos.

Foi assim que nasceu esta primeira versão do sistema. Ainda me custa acreditar que alguém além de mim vá usá-lo, mas segue firme no processo de testes. A proposta é simples (e um tanto ousada): criar uma solução eficiente para comunicação em múltiplos idiomas, operando de forma descentralizada — algo que, imagino, deixaria o tio Tanenbaum orgulhoso.

### O que é o projeto?

Este projeto propõe o desenvolvimento de um sistema de dublagem em tempo real, distribuído e full-duplex, capaz de permitir diálogos naturais entre falantes de diferentes idiomas **sem recorrer à tradução direta**. Em vez disso, o sistema constrói uma **linguagem intermediária universal**, fundamentada em morfismos e estruturas formais, o que possibilita a reconstrução da fala em qualquer idioma de destino com fidelidade semântica e morfológica.

Dessa forma, não se trata exatamente de um sistema de dublagem no sentido tradicional, mas sim de algo mais próximo do que o cérebro humano faz: quando nos comunicamos, não “traduzimos” palavra por palavra, mas organizamos o pensamento em tempo real, usando o idioma apenas como instrumento. A proposta é replicar essa inteligência estrutural de modo computacional.

Em outras palavras, este framework rompe com o paradigma da tradução literal. Ele parte do princípio de que **a linguagem é uma estrutura universal**, enquanto os idiomas são apenas **representações formais e locais** dessa estrutura.

---

## Arquitetura e Design

![alt text](image.png)

> *Alt text: Um projeto com dois módulos e um plano secreto de eliminar um deles futuramente.*

### Canais (C)

A arquitetura baseia-se em múltiplos canais full-duplex, onde cada canal realiza tanto a codificação quanto a decodificação. Cada canal recebe um **objeto de valor especial**, responsável por encapsular as informações linguísticas essenciais. Esse objeto, que chamo com carinho de ** objeto homomórfico**, é o produto de operações estruturais baseadas em morfemas.

O objeto mórfico carrega consigo um bloco de dados contendo um conjunto de **instruções genéticas** interpretáveis por qualquer canal, desde que no idioma adequado.

Atualmente, estamos trabalhando com dois canais básicos:

- **PT-BR** (Português)
- **EN** (Inglês)

Cada canal possui um idioma de entrada e outro de saída. O canal de entrada utiliza o microfone padrão do sistema para capturar e transmitir a voz. O canal de saída — atualmente em desenvolvimento — será um driver de áudio virtual que poderá ser integrado a plataformas como o Google Meet.

---

### Barramento (B)

O barramento é, por enquanto, uma **estrutura provisória** de multiplexação dos dados. Ainda não conta com mecanismos robustos de sincronização, mas cumpre seu papel nesta fase inicial do projeto.

Em versões futuras, o sistema será migrado para um ambiente **Kubernetes (K8s)**, onde cada canal será executado como um microserviço serverless. Nesse cenário, o barramento poderá ser eliminado por completo, com os canais operando de forma direta e autônoma.

---

## Como Utilizar

Por enquanto, o sistema é uma **prova de conceito (POC)**. Para testá-lo localmente, basta executar:

```bash
docker-compose up --build
```

O sistema iniciará automaticamente e tudo o que for falado em português será reproduzido em inglês em tempo real.

## Notas Finais

Este projeto ainda está em sua infância, mas já vislumbro várias possibilidades para as próximas fases. Aos poucos, vou refinando as ideias, testando novas abordagens e, quem sabe, transformando essa curiosidade pessoal em uma ferramenta real para facilitar a comunicação entre mundos linguísticos.

## Futuro para não esquecer

Futuramente pretendo implementar:

- Drive virtual para utilizar em video chamada
- Feature de personalização da voz de saída para ser a mesma de quem fala.
- Rede social a nível global para falantes nativos de indionas desconhecido poder criar seus próprios canais.
- Possibilidade de criar idiomas virtuis, sabendo que tanto a entrada quanto saidas processam objetos morficos, não é restritivo existir a linguagem, apenas evoluir o sistema para criar liguagem formais onde as regras de produção em gramáticas de Chomsky talvez possa ser utilizada com um morfimos derivativos das operações internas do sistema seja terminais ou não terminais, para gerar as sequências de uma linguagem decoficicavel, caso contrário não existem como ter uma retropropagação para calibrar a rede.
