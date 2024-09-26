# Sistema de Venda de Passagens Aéreas para Companhias Low-Cost com Comunicação TCP/IP e Infraestrutura em Docker

## Discentes
- **Humberto Bandeira Costa**
- **João Victor Alves**

## Introdução
  O setor de aviação low-cost carriers (LCCs), trouxe uma revolução significativa na forma como as pessoas acessam o transporte aéreo. Ao adotar estratégias inovadoras de redução de custos, como o uso de aeroportos secundários e operações automatizadas, as LCCs possibilitaram que um número maior de pessoas viajasse de avião, promovendo o crescimento do turismo e da conectividade global. Dentro desse contexto, uma nova companhia aérea brasileira de baixo custo busca expandir suas operações ao oferecer a compra de passagens pela Internet, possibilitando que os clientes escolham e reservem assentos em trechos disponíveis de forma eficiente. O desafio principal para a implementação desse sistema reside na necessidade de estabelecer uma comunicação eficiente e confiável entre o cliente e o servidor central da companhia. A solução deve ser construída sobre a base do subsistema de rede TCP/IP, com uma API Socket adequada para permitir que os clientes consultem, selecionem e comprem passagens. Este relatório tem como objetivo apresentar as decisões teóricas e práticas tomadas durante o desenvolvimento do sistema de comunicação, detalhando as opções técnicas e a definição do protocolo de comunicação adotado para atender às necessidades operacionais da companhia.

## Fundamentação Teórica 
Nesta seção, serão apresentados os principais conceitos e teorias que fundamentam o desenvolvimento do sistema de comunicação cliente-servidor.
   Protocolo TCP/IP
O protocolo de Controle de Transmissão/Protocolo Internet é a base de comunicação na internet, sendo responsável pela conexão entre dispositivos em redes distintas. O TCP/IP é uma tecnologia baseada em várias camadas que trabalham juntas para assegurar a transmissão íntegra e segura dos dados na web. A divisão em camadas permite que essa transmissão seja padronizada e independente dos dispositivos, garantindo compatibilidade com diferentes sistemas, arquiteturas e linguagens de programação. As quatro camadas principais são:

Camada de Aplicação:Responsável pela interação direta com o usuário e por fornecer os protocolos que suportam serviços de rede, como HTTP (para navegação web), FTP (para transferência de arquivos), e SMTP (para envio de e-mails). Essa camada lista com dados que serão transmitidos entre os aplicativos, traduzindo as informações para formatos compreensíveis pelas camadas inferiores 

Camada de Transporte: Garante a transmissão confiável de dados entre o emissor e o receptor, independente da rede física. O TCP (Protocolo de Controle de Transmissão) é o principal protocolo desta camada, responsável pela entrega de pacotes na ordem correta, controle de fluxo e retransmissão em caso de falhas.

Camada de Internet: Lida com o endereço e roteamento dos pacotes de dados entre as redes. O principal protocolo desta camada é o IP(Protocolo de Internet), que atribui endereços IP às máquinas e decide qual caminho os pacotes devem seguir até o destino. Nessa camada, os pacotes são chamados de “datagramas”e podem ser fragmentados para melhor se adaptarem às características da rede.

Camada de Rede: Responsável pela transmissão física dos dados, ou seja, ela define como os dados serão enviados ao meio físico. Essa camada lida com a interface entre o hardware e o software de rede, incluindo aspectos como a configuração dos adaptadores de rede e a modulação dos sinais de transmissão.
O TCP/IP foi escolhido no desenvolvimento do sistema devido sua capacidade de garantir uma comunicação segura e confiável entre cliente e servidor. O TCP/IP tem a capacidade de garantir que os dados enviados cheguem ao destino de forma íntegra e na ordem correta, fazendo assim a escolha por ele ser a mais certa possível.
	
   Modelo Cliente-Servidor
A estrutura cliente-servidor é um modelo de arquitetura de rede amplamente utilizado em ambientes de TI. Nesta abordagem, os computadores são divididos em dois grupos: servidores, que fornecem serviços ou recursos, e clientes, que solicitam estes serviços e recursos, recebendo-os como respostas. No contexto do sistema implementado, onde há reservas de passagens, essa arquitetura permite que os clientes consultem rotas e efetuem a compra de passagens em tempo real, garantindo que a disponibilidade de vagas no voos sejam atualizadas constantemente. No desenvolvimento do produto foi escolhida a arquitetura cliente-servidor de duas camadas, onde a comunicação é direta entre o cliente e o servidor. O cliente é responsável pela interface do usuário e envia as solicitações ao servidor, que processa essas solicitações e retorna as respostas ao cliente. Optamos por este modelo por ser simples e adequado para aplicações menores, mas caso a aplicação cresça, ela pode se tornar ineficiente devido à carga direta sobre o servidor.

   Sockets
Sockets são uma abstração fundamental para a comunicação em rede, permitindo a troca de dados entre um cliente e um servidor. Eles oferecem uma interface de programação que facilita a implementação de protocolos de comunicação, seja em um ambiente local ou na Internet. <figure>
  <img src="https://github.com/user-attachments/assets/7f0e0bb4-ba84-48bd-9337-3abb0d12e6ef" alt="Descrição da imagem">
  <figcaption>figura 1. Esquema representando como o socket funciona no cliente-servidor
</figcaption>
</figure>



## Metodologia
Nesta seção, explicaremos a metodologia adotada para o desenvolvimento do sistema, detalhando as etapas de implementação, as ferramentas utilizadas, e o fluxo de trabalho seguido pela equipe.
   Descrição Geral do Projeto
Este projeto tem como objetivo o desenvolvimento de um sistema de comunicação cliente-servidor para uma companhia aérea de baixo custo, utilizando o protocolo TCP/IP. O sistema deve permitir que os clientes realizem a compra de passagens aéreas pela internet, consultando rotas disponíveis e escolhendo os trechos de voo de maneira eficiente e segura. O sistema foi projetado para oferecer uma solução automatizada, onde os clientes possam comprar as passagens online, sem a necessidade da interação com funcionários. Para isso, foi implementado um servidor que gerencia todas as solicitações de compra, listagem de passagens e login, garantindo segurança e confiabilidade. O projeto foi dividido em três partes principais:
Implementação do Servidor:  o servidor, responsável por gerenciar as rotas de voos e o controle de vagas nos voos, foi desenvolvido com base na API de sockets TCP/IP. Ele recebe as solicitações de compra dos clientes, verifica a disponibilidade de vagas nos trechos selecionados e confirma a compra.
Desenvolvimento do Cliente: o cliente é a interface onde permite o usuário consultar as rotas e realizar a compra de passagens. Ele envia as solicitações ao servidor através da rede, seguindo um protocolo definido para garantir a integridade e segurança das informações.
Segurança e Integridade dos Dados: o protocolo TCP/IP foi escolhido por sua confiabilidade, garantindo que os dados sejam transmitidos de forma segura e que nenhuma informação seja corrompida ou perdida durante o processo de comunicação.

   Ferramentas e Tecnologias Utilizadas
Neste projeto, diversas ferramentas e tecnologias foram escolhidas estrategicamente para garantir a implementação eficiente e segura do sistema de comunicação cliente-servidor. Foi utilizada a linguagem de programação Python por sua simplicidade, legibilidade e vasta quantidade de bibliotecas voltadas ao desenvolvimento de redes. Ela facilita a implementação de sockets e o gerenciamento das conexões cliente-servidor, além de oferecer flexibilidade para futuras expansões do projeto. Como falado anteriormente de sockets, utilizamos a biblioteca nativa socket do Python para implementar a comunicação baseada no protocolo TCP/IP. Essa biblioteca permite a criação de servidores e clientes que podem se conectar, enviar e receber dados, garantindo uma comunicação confiável e eficiente. O socket é essencial para o desenvolvimento da lógica de rede do sistema. Para o desenvolvimento do código, optamos por utilizar o Visual Studio Code (VSCode), um editor de código leve, altamente configurável e com suporte a diversas extensões. Ele proporcionou um ambiente de desenvolvimento integrado eficiente, e com variedade de ferramentas. E para garantir a consistência do ambiente de desenvolvimento e facilitar a implementação do sistema utilizamos Docker. Com Docker, o sistema foi encapsulado em containers, permitindo que o servidor e os clientes sejam executados em qualquer máquina sem problemas de compatibilidade. Isso também facilita a escalabilidade e o gerenciamento do ambiente de execução em produção. Essas ferramentas e tecnologias foram selecionadas com base em suas capacidades de facilitar o desenvolvimento, garantir a portabilidade do sistema e assegurar a integridade da comunicação entre cliente e servidor.

   Etapas do Desenvolvimento
O desenvolvimento do sistema cliente-servidor para a compra de passagens aéreas foi realizado seguindo um conjunto estruturado de etapas, com o objetivo de garantir uma implementação eficiente e atender aos requisitos. A seguir, serão descritas as principais etapas do desenvolvimento:
Planejamento e Definição dos Requisitos: nesta etapa inicial, foi realizado um levantamento detalhado dos requisitos do sistema, considerando as necessidades da companhia, como a compra de passagens online, e a garantia de uma comunicação segura e confiável. As sessões de PBL (Aprendizagem Baseada em Problemas), realizadas em conjunto com a turma, foram de grande ajuda nessa fase, permitindo a troca de ideias colaborativa e a identificação de soluções práticas para os desafios do projeto. Esse processo colaborativo foi essencial para definir de forma clara o uso do protocolo TCP/IP para a comunicação e as funcionalidades essenciais da API de rede que garantiriam uma operação eficiente e segura no sistema. 

Implementação do Servidor: uma parte importante do processo de desenvolvimento do projeto foi a implementação do servidor. Para isso, usamos a biblioteca socket em Python, com base no protocolo TCP. O servidor foi programado para gerenciar as conexões dos clientes, receber consultas sobre voos, verificar a disponibilidade das vagas e processar as compras. Ele também foi configurado para lidar com múltiplas conexões simultâneas.

Desenvolvimento do Cliente: paralelamente à implementação do servidor, foi desenvolvido o cliente. Este cliente permite que os usuários consultem as rotas disponíveis, selecionem trechos de voos, e enviem suas solicitações ao servidor. Para realizar a comunicação foi utilizado o TCP, garantindo que os dados fossem transmitidos de forma confiável e segura.
Teste de Comunicação: nesta etapa, realizamos uma série de testes de comunicação entre o cliente e o servidor, simulando diferentes cenários de consulta e reserva de passagens. O objetivo foi garantir que os dados fossem transmitidos corretamente, que as compras fossem processadas de acordo com as regras estabelecidas, e que o sistema fosse capaz de lidar com múltiplos clientes simultaneamente.
Documentação e Preparação para a Entrega: finalizamos o projeto com a elaboração da documentação detalhada sobre o sistema, incluindo descrição das funcionalidades, o protocolo de comunicação implementado e os passos para configurar o ambiente e executar o servidor e o cliente. A documentação foi preparada para ser disponibilizada no GitHub, conforme solicitado.

   Formatação e Tratamento de Dados
A formatação de dados desempenhou um papel essencial no desenvolvimento do sistema de comunicação cliente-servidor, garantindo que as informações pudessem ser trocadas de maneira eficiente e estruturada entre as partes. Para implementar essa troca de dados, utilizamos a biblioteca JSON. Ela foi utilizada para serializar e desserializar objetos complexos, como instâncias de classes que representam passageiros, voos e tickets. Esse processo permite que objetos Python sejam transformados em strings JSON, que podem ser transmitidas pela rede e posteriormente reconstruídas no lado do cliente ou do servidor, mantendo a integridade e legibilidade dos dados.<figure style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/f86436ef-d127-4f47-8202-ca3d0c73eef2" alt="Descrição da imagem">
  <figcaption>Figura 2. Exemplo do uso da biblioteca JSON em Python
</figcaption>
</figure>

   Statefull x Stateless
Neste projeto, adotamos uma abordagem stateful para a comunicação entre cliente e servidor. Isso significa que, durante toda a interação do cliente com o servidor, o estado da conexão é mantido, permitindo que o servidor "lembre" do cliente ao longo da sessão e continue o processamento a partir do ponto onde a comunicação parou. Optamos pela abordagem stateful devido à necessidade de manter a sessão do cliente ao longo do processo de compra. Isso permite que o servidor detenha o estado do cliente, como informações de login e a possibilidade de realizar consultas sobre voos e rotas, sem a necessidade de repetir a autenticação. Além disso, por lidarmos com transações sensíveis, como a compra de passagens aéreas, a persistência do estado assegura que a comunicação seja confiável e consistente, garantindo que cada etapa da compra seja processada de forma segura e sem interrupções.

   Tratamento de Conexões Simultâneas
No desenvolvimento deste sistema, implementamos o tratamento de conexões simultâneas para garantir que múltiplos clientes pudessem interagir com o servidor ao mesmo tempo. Utilizamos a biblioteca threading do Python, que permite a criação de threads para cada cliente conectado. Cada nova conexão estabelecida é tratada em uma thread separada, garantindo que várias solicitações possam ser processadas simultaneamente. Essa abordagem é fundamental para garantir que o servidor permaneça responsivo, mesmo quando vários clientes estão realizando consultas de voos ou efetuando a compra de passagens ao mesmo tempo. A capacidade de lidar com conexões simultâneas foi essencial para simular um ambiente real de atendimento online, onde o sistema precisa processar várias requisições de diferentes usuários de maneira rápida e eficiente, sem que uma conexão interfira no desempenho das outras.

## Testes e Resultados
Nesta seção, apresentamos os principais testes realizados durante o desenvolvimento do sistema de comunicação cliente-servidor, bem como os resultados obtidos. Cada teste foi desenhado para verificar a integridade, a performance e a confiabilidade do sistema em diferentes cenários. Os testes foram realizados tanto no ambiente de desenvolvimento quanto em simulações de situações reais de uso.
### Comandos para inicializar o sistema:

Para inicializar o sistema, siga os passos a seguir, utilizando Docker para configurar tanto o cliente quanto o servidor:

1. **Servidor:**

   - No diretório do servidor, crie a imagem Docker:
     ```bash
     docker build -t airport-server .
     ```

   - Inicie o servidor com o seguinte comando:
     ```bash
     docker run -d -p 5050:5050 airport-server
     ```

2. **Cliente:**

   - **Importante:** Altere o IP no arquivo `client.py` para o IP da máquina onde o servidor está sendo executado.

   - No diretório do cliente, crie a imagem Docker:
     ```bash
     docker build -t airport-client .
     ```

   - Inicie o cliente com o comando:
     ```bash
     docker run -it airport-client
     ```

3. **Utilizando `docker-compose` :**

   - Suba os containers em segundo plano:
     ```bash
     docker-compose up -d
     ```

   - Execute o bash do cliente:
     ```bash
     docker exec airport-client /bin/bash
     ```

   - Por fim, execute o cliente:
     ```bash
     python3 client.py
     ```


O servidor foi inicializado em um ambiente local, utilizando a API de sockets TCP/IP. Testamos se o servidor conseguia escutar a porta designada e estava pronto para receber solicitações de clientes:
<figure>
  <img src="https://github.com/user-attachments/assets/f4b5e8b4-0da5-42c6-97c9-5935d40084c1" alt="Descrição da imagem">
  <figcaption>figura 3. Conexão com o servidor estabelecida </figcaption>
</figure>

A conexão do servidor foi estabelecida com sucesso, permanecendo estável durante todo o período de teste. O servidor foi capaz de escutar continuamente por novas conexões sem interrupções ou falhas. O log do servidor registrou corretamente os eventos de inicialização e as conexões recebidas.

Um cliente foi executado em um terminal/máquina diferente para se conectar ao servidor utilizando o IP e a porta definidos. O cliente enviou solicitações de consulta de voos e reserva de assentos.
<figure>
  <img src="https://github.com/user-attachments/assets/ca16c707-6469-4149-a0ff-b91173596de3" alt="Descrição da imagem">
  <figcaption>Figura 4. Conexão do cliente com o servidor estabelecida </figcaption>
</figure>

A conexão foi estabelecida corretamente, e o cliente pôde enviar e receber dados do servidor sem interrupções. As consultas e reservas foram processadas de acordo com os parâmetros enviados, e o cliente recebeu as respostas apropriadas para cada solicitação. O tempo de resposta foi satisfatório, com latência mínima, indicando uma comunicação eficiente.

Houve a conexão simultânea de mais de um cliente ao servidor. Cada cliente conseguiu estabelecer uma comunicação bem-sucedida, e o servidor registrou adequadamente essas conexões, exibindo a origem de cada uma delas. Isso demonstra que o servidor foi capaz de gerenciar múltiplas conexões de forma eficiente.
<figure>
  <img src="https://github.com/user-attachments/assets/f2e96d76-8aab-4833-ba25-bded52fa0b72" alt="Descrição da imagem">
  <figcaption>Figura 5. Múltiplas conexões  </figcaption>
</figure>

Dois clientes diferentes tentaram comprar a única passagem restante em um voo de forma simultânea. O servidor deveria garantir que apenas uma das transações fosse concluída com sucesso, evitando a duplicidade de compras.
<figure>
  <img src="https://github.com/user-attachments/assets/55b962e0-b33b-4790-99c1-179a3eeaadfe" alt="Descrição da imagem">
  <figcaption>Figura 6. Tentativa de compra de passagem no mesmo momento
</figcaption>
</figure>

O sistema gerenciou corretamente a situação. Apenas um dos clientes conseguiu efetuar a compra da passagem, enquanto o outro recebeu uma mensagem indicando que a passagem já havia sido comprada. O servidor garantiu a consistência dos dados, evitando reservas conflitantes. Os testes demonstraram que o sistema de comunicação cliente-servidor se comporta de maneira eficiente e confiável, atendendo aos requisitos propostos. O servidor foi capaz de lidar com múltiplas conexões simultâneas sem perda de desempenho, e o protocolo de comunicação assegurou que os dados fossem transmitidos de forma íntegra e segura.


## Conclusão
O desenvolvimento deste sistema de comunicação cliente-servidor para uma companhia aérea de baixo custo permitiu implementar uma solução eficiente e confiável, capaz de atender às necessidades operacionais e proporcionar uma experiência de compra de passagens online segura e ágil para os clientes. Ao longo do projeto, diversas decisões técnicas foram tomadas, como o uso do protocolo TCP/IP para garantir a integridade e confiabilidade da transmissão de dados, além da implementação de uma arquitetura cliente-servidor de duas camadas que facilitou a comunicação direta entre o usuário e o servidor central. A integração de ferramentas como a linguagem Python, a biblioteca socket, o Docker, e a abordagem stateful para a comunicação, foram essenciais para garantir a escalabilidade e robustez do sistema. Além disso, a adoção de threads para lidar com conexões simultâneas assegurou que o sistema pudesse atender a múltiplos clientes de maneira eficiente, sem comprometer o desempenho ou a integridade dos dados. Ao final do projeto, as funcionalidades implementadas atenderam plenamente os requisitos levantados na fase inicial, proporcionando um sistema capaz de gerenciar de forma eficaz a compra de passagens em tempo real. Com a documentação detalhada e o uso de práticas de desenvolvimento modernas, o sistema se encontra preparado para futuras expansões, garantindo que a companhia possa continuar oferecendo serviços inovadores e acessíveis aos seus clientes.

## Referências

Drake 2023 DRAKE, V. O que é o modelo TCP/IP? Camadas e protocolos explicados.
2023. Acesso em: 21 set. 2024. Dispon´ıvel em: ⟨https://www.freecodecamp.org/portuguese/
news/o-que-e-o-modelo-tcp-ip-camadas-e-protocolos-explicados/⟩.

Net NET, C. Cliente-Servidor, uma estrutura lógica para a computação centralizada. Acesso em: 21 set. 2024. Disponıvel em: ⟨https://www.controle.net/faq/
cliente-servidor-uma-estrutura-para-a-computacao-centralizada⟩.

Noleto 2023 NOLETO, C. Protocolo TCP/IP: o que é e  exemplos de como funciona.
2023. Acesso em: 21 set. 2024. Disponível em: ⟨https://blog.betrybe.com/tecnologia/
protocolo-tcp-ip/⟩.

Santana 2023 SANTANA, B. O Que é o Protocolo TCP/IP e Como Ele Funciona? 2023.
Acesso em: 21 set. 2024. Disponível em: ⟨https://www.hostinger.com.br/tutoriais/tcp-ip#O_Que_e_TCPIP⟩.

Souza 2024 SOUZA, A. J. Arquitetura Cliente-Servidor. 2024. Acesso em: 21 set. 2024.
Dispon´ıvel em: ⟨https://blog.grancursosonline.com.br/arquitetura-cliente-servidor/⟩.








