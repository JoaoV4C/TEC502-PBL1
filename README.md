# TEC502-PBL1
  
    Introdução
O setor de aviação low-cost carriers (LCCs), trouxe uma revolução significativa na forma como as pessoas acessam o transporte aéreo. Ao adotar estratégias inovadoras de redução de custos, como o uso de aeroportos secundários e operações automatizadas, as LCCs possibilitaram que um número maior de pessoas viajasse de avião, promovendo o crescimento do turismo e da conectividade global. Dentro desse contexto, uma nova companhia aérea brasileira de baixo custo busca expandir suas operações ao oferecer a compra de passagens pela Internet, possibilitando que os clientes escolham e reservem assentos em trechos disponíveis de forma eficiente. O desafio principal para a implementação desse sistema reside na necessidade de estabelecer uma comunicação eficiente e confiável entre o cliente e o servidor central da companhia. A solução deve ser construída sobre a base do subsistema de rede TCP/IP, com uma API Socket adequada para permitir que os clientes consultem, selecionem e comprem passagens. Este relatório tem como objetivo apresentar as decisões teóricas e práticas tomadas durante o desenvolvimento do sistema de comunicação, detalhando as opções técnicas e a definição do protocolo de comunicação adotado para atender às necessidades operacionais da companhia.

    Fundamentação Teórica 
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
Sockets são uma abstração fundamental para a comunicação em rede, permitindo a troca de dados entre um cliente e um servidor. Eles oferecem uma interface de programação que facilita a implementação de protocolos de comunicação, seja em um ambiente local ou na Internet.<figure>
  <img src="https://github.com/user-attachments/assets/7f0e0bb4-ba84-48bd-9337-3abb0d12e6ef" alt="Descrição da imagem">
  <figcaption>figura 1. Esquema representando como o socket funciona no cliente-servidor</figcaption>
</figure>

