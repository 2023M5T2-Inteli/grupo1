<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Magnetum | Concepção de sistema de automação industrial para separação magnética (IPT)
</center></font>

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Matriz de Risco](#matriz-de-risco)
  - [Oceano Azul](#oceano-azul)
  - [Análise financeira](#análise-financeira)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Personas](#personas)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Diagrama geral](#diagrama-geral)
  - [Projeto mecânico](#projeto-mecânico)
    - [Validação dos dispositivos mecânicos fabricados](#validação-dos-dispositivos-mecânicos-fabricados)
      - [Suporte para ímãs](#suporte-para-ímãs)
      - [Case para PCB](#case-para-pcb)
  - [Projeto eletrônico](#projeto-eletrônico)
    - [Esquemático do circuito](#esquemático-do-circuito)
    - [Implementação do circuito](#implementação-do-circuito)
      - [Componentes utilizados](#componentes-utilizados)
      - [Validação dos dispositivos eletrônicos](#validação-dos-dispositivos-eletrônicos)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Testes de componentes](#testes-de-componentes)
      - [Movimentação do robô](#movimentação-do-robô)
      - [Eletroímã na ponte H](#eletroímã-na-ponte-h)
      - [Bomba d'água na ponte H](#bomba-dágua-na-ponte-h)
      - [Sensor de campo eletromagnético](#sensor-de-campo-eletromagnético)
      - [Célula de carga e amplificador HX711](#célula-de-carga-e-amplificador-hx711)
    - [Relatório de entradas e saídas dos testes](#relatório-de-entradas-e-saídas-dos-testes)
- [UX e UI Design](#ux-e-ui-design)
- [Backend](#backend)
  - [Diagrama de banco de dados](#diagrama-de-banco-de-dados)
- [Teste de Software](#teste-de-software)
  - [Movimentação do robô](#movimentação-do-robô-1)
  - [Integração de hardware com frontend](#integração-de-hardware-com-frontend)
- [Validação da eficácia do sistema](#validação-da-eficácia-do-sistema)
    - [Relatório de entradas e saídas do teste final](#relatório-de-entradas-e-saídas-do-teste-final)
- [Referências](#referências)


# Autores

* Antônio Ribeiro Cavalcante
* Elisa de Oliveira Flemer
* Emanuele Lacerda Morais Martins
* Felipe Campos
* Henrique Agostinho Schilder Lima
* João Vitor Oliveira Rodrigues
* Luca Sarhan Giberti


# Visão Geral do Projeto

## Empresa

O Instituto de Pesquisas Tecnológicas (IPT) é uma instituição de renome no cenário de pesquisa brasileiro. Seu principal objetivo é contribuir para o desenvolvimento científico, tecnológico e industrial do país. Fundado em 1899, é considerado um dos mais antigos centros de pesquisa tecnológica do Brasil, com uma vasta gama de áreas de atuação.

O IPT é equipado com infraestrutura de ponta, incluindo laboratórios e centros de pesquisa, além de possuir uma equipe de pesquisadores, engenheiros, técnicos e especialistas altamente qualificados e multidisciplinares. O instituto estabelece parcerias com empresas e instituições de pesquisa nacionais e internacionais para promover a transferência de tecnologia e a cooperação científica.

Em resumo, o IPT é uma instituição líder no avanço tecnológico do Brasil, oferecendo excelência em pesquisa, equipamentos de última geração e uma equipe multidisciplinar altamente qualificada, buscando contribuir para o desenvolvimento do país e do mundo.

## O Problema

O IPT é uma instituição que atua em diversas áreas, incluindo a de materiais avançados, e faz uso da separação magnética como técnica para avaliar a liberação de minerais e materiais com propriedades magnéticas. No entanto, devido ao fato do processo de separação magnética ser realizado manualmente, a medição da distância não é precisa, o que pode afetar a precisão do campo eletromagnético aplicado às partículas. Como o campo eletromagnético é inversamente proporcional à distância, a determinação do campo correto para separar os minerais pode se tornar complexa. Além disso, experimentar diferentes campos requer a alternância dos ímãs utilizados, o que demanda uma variedade de ímãs disponíveis. Em resumo, a falta de precisão no processo de separação magnética pode prejudicar a avaliação de minerais e materiais com propriedades magnéticas, comprometendo a eficiência das atividades realizadas pelo IPT na área de materiais avançados.

## Objetivos

### Objetivos gerais

Desenvolver um solução de automação industrial para aumentar a precisão e eficiência de ensaios de separação magnética, padronizando a captura, limpeza e despejo dos materiais analisados.

### Objetivos específicos

O projeto objetiva a automatização dos ensaios de separação magnética de amostras de minerais, por meio de um braço mecânico capaz de coletar, limpar e despejar o material captado. Esse processo visa aumentar a produtividade, repetibilidade, eficiência e precisão dos ensaios. Para isso, temos como métricas de sucesso a precisão da altura dos ímãs em relação à amostra, o ajuste da velocidade e o ajuste da intensidade dos ímãs. Em mais detalhes, temos como objetivos:

1. Implementar um sistema capaz de varrer as três bandejas de modo consistente e programável;
2. Otimizar a altura dos ímãs para maximizar a captura de material magnético;
3. Assegurar a limpeza do material captado com o auxílio de bombas d'águas estrategicamente posicionadas;
4. Viabilizar a configuração de intensidade magnética dos eletroímãs a partir de uma interface gráfica;
5. Viabilizar a configuração do número de passadas e o início do ensaio a partir de uma interface gráfica;
6. Gerar relatórios de ensaios passados na interface gráfica;
7. Oferecer ferramentas de controle direto e imediato do sistema, no que tange a ligar e desligar eletroímãs e bombas d'água, independentemente do estado atual do sistema;
8. Oferecer o agrupamento de ensaios por cliente e projeto, facilitando a repetibilidade de amostras através da associação de ensaios diferentes em um tema em comum

## Partes interessadas

* Laboratório de processo metalúrgicos;
* Inteli

# Análise do Problema

Para melhor entender o contexto do projeto, realizamos uma análise de Oceano Azul para identificar nosso posicionamento em relação ao método tradicional de separação magnética. Buscamos também concorrentes, como o HGMS da empresa Metso, mas concluímos que sua aplicação não servia ao mesmo nicho que nosso projeto. Na realidade, não encontramos nenhum concorrente que se adeque ao mercado que pretendemos atender, isto é, o de ensaios de separação magnética para análise de amostras de mineração em pequena escala.

Ademais, criamos uma matriz de risco sobre o desenvolvimento do projeto, com base em nossas experiências conjuntas de riscos e oportunidades de módulos passados aplicados às possibilidades do bimestre vigente. 

Por fim, a partir da análise das informações citadas acima e dados obtidos do entendimento do design, sintetizamos o canvas de proposta de valor da solução.

## Matriz de Risco

![image](https://user-images.githubusercontent.com/99221221/221010837-95321191-ad6f-4ac9-a3ca-75cc505b2966.png)

Riscos análisados:
* 1 - Danificar o Magician Lite
* 2 - Demora do parceiro fornecer materiais necessários
* 3 - Incapacidade de realizar testes fidedignos à demanda do projeto
* 4 - Queima de componentes eletrônicos
* 5 - Conflito de merge no GIT
* 6 - Ausência de membros
* 7 - Falta de comunicação
* 8 - Incerteza com a expectativa dos entregáveis
* 9 - Viés na análise das amostras
* 10 - O MVP ser adotado pelo parceiro
* 11 - Aumento significativo da velocidade e precisão dos ensaios
* 12 - Nova aplicação para o Magician Lite
* 13 - Visitar os laboratórios do IPT
* 14 - Teste in loco (IPT) do MVP com amostras reais
* 15 - Acesso a impressoras 3D

## Oceano Azul

A análise de oceano azul examina como nossa solução se compara aos concorrentes existentes; em especial, identificamos quais aspectous e/ou características sofrem aumento, redução, eliminação ou criação. No caso, comparamos o Magnetum apenas ao método tradicional.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/ux_e_negocios/oceano.png?raw=true)

**Aumentar**
* Precisão da análise: o uso do braço robótico e do microcontorlador permite a padronização de distância e insidade magnética
* Custo: o custo de setup inicial é significativamente maior do que o custo por hora de um trabalhador manual
* Velocidade: o robô pode funcionar 24h por dia
* Tecnologia: o sistema traz mais tecnologia quando comparado a um técnico manual
* Eficiência: a padronização dos ensaios reduz o retrabalho e erro humano

**Diminuir**
* Mantenabilidade: o uso de um sistema automatizado traz mais dificuldades para manutenção
* Durabilidade: o braço robótico é muito mais frágil do que um ímã permanente

**Criar**
* Parametrização: a solução permite a configuração de parâmetros confiáveis e constantes para o processo
* Gasto energético: o processo atual não gasta nenhuma energia elétrica; com o Magnetum, será necessário utilizar uma fonte de alimentação.

**Eliminar**
* Intervenção humana: o Magnetum permite que a separação magnética em si seja feita de modo totalmente automatizado. É preciso apenas que um técnico configure as condições do ensaio e prepare o material.

## Análise financeira

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/ux_e_negocios/analise_financeira.png?raw=true)

**Aspectos considerados:**

A análise financeira é fundamental para avaliar a viabilidade e a eficiência de um projeto ou investimento. Nesse contexto, é necessário considerar todos os custos envolvidos no processo e comparar as alternativas disponíveis. Neste estudo, faremos uma análise financeira comparando o custo do uso do Magnetum com o custo do método tradicional de ensaio.

* Custo fixo de instalação do sistema: R$ 15.301,50 (Dobot Magician Lite + eletrônicos periféricos)
* Custo mensal de manutenção e energia: R$ 764,98
* Custo do Magnetum por ensaio (gasto energético + manutenção): R$ 2,125
* Custo do trabalhador por ensaio tradicional: R$ 7,81

A análise de custo fixo foi feita considerando o custo de uma unidade do braço robótico somado aos valores dos componentes eletrônicos periféricos, como o microcontrolador, as bombas d'água e os eletroímãs. Para o custo mensal, estimamos um gasto energético de 14,4kWh junto de um orçamento para manutenção referente a 5% do valor do braço mecânico, seguindo a teoria de estimativa de custos para manutenção. Por fim, inferimos o custo por hora do trabalhador considerando o salário médio de um técnico de trabalhador que opera seis horas por dia, chegando a R$ 7,81 por ensaio tradicional.

Assim, levando em conta que o uso do método tradicional é mais caro e demorado do que o uso do Magnetum, e considerando que a máquina trabalhará por 6 horas todos os dias, enquanto o trabalhador trabalhará por 8 horas, é possível estimar que, após 3000 utilizações (equivalente a cerca de 168 dias), os custos totais com o trabalhador serão maiores do que com o uso do Magnetum.

Com base na análise financeira realizada, podemos concluir que o uso do Magnetum é mais vantajoso do que o método tradicional de ensaio. Embora o custo fixo de instalação do sistema seja alto, o custo mensal de manutenção e energia é baixo, o que resulta em um custo menor por ensaio. Além disso, a máquina pode realizar o processo com maior precisão e rapidez, reduzindo a necessidade de repetições e aumentando a eficiência do trabalho. Dessa forma, é possível obter uma economia significativa a longo prazo, tornando o Magnetum uma opção mais rentável e eficiente para o processo de ensaio.

## Proposta de Valor: Value Proposition Canvas

Após realizar uma pesquisa de campo e entrevistar um técnico responsável pelo processo de separação magnética de amostras de ensaio, visitamos o local onde é realizado esse processo e analisamos o mercado e os concorrentes. Com base nessas informações, criamos um canvas de proposta de valor para um produto que pode solucionar as dores e problemas identificados pelo técnico e melhorar a eficiência do processo como um todo.

O canvas é composto por três seções: Tarefas, Dores e Ganhos. Na seção Tarefas, identificamos as atividades-chave que o técnico realiza no processo, como determinar a viabilidade de mineração em certa região e separar material magnético em uma amostra com alta precisão. Na seção Dores, listamos os problemas e frustrações que o técnico enfrenta, como ter que repetir ensaios manualmente e não obter a precisão desejada, mesmo com muito esforço.

Por fim, na seção Ganhos, destacamos as melhorias e benefícios que o nosso produto pode trazer para o processo, como a geração de relatórios precisos e padronizados de cada ensaio.

Com base nesses ganhos, criamos um produto que pode aliviar as dores identificadas pelo técnico. O nosso produto é um braço robótico conectado a um eletroímã para a separação magnética precisa e automatizada de amostras de ensaio. Além disso, o produto conta com a geração de relatórios baseados em um template com os dados coletados no ensaio.

Ao analisar o mercado e os concorrentes, percebemos que poucas empresas oferecem soluções automatizadas e precisas para a separação magnética de amostras de ensaio. Portanto, acreditamos que o nosso produto pode ser uma alternativa inovadora e eficiente para esse processo.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/ux_e_negocios/canvas.png?raw=true)

## Personas
A criação de personas é uma técnica importante no design de soluções, pois permite entender as necessidades e desejos dos usuários para desenvolver produtos ou serviços que atendam às suas expectativas.

Para isso, realizamos uma pesquisa aprofundada, incluindo entrevistas com técnicos que atuam na área de ensaios minerais e visitas a oficinas onde esses ensaios são realizados. Dessa forma, conseguimos entender a rotina de trabalho desses profissionais e identificar as dores e desafios enfrentados no processo de separação magnética.

Nesse contexto, apresentamos Tiago Silva, uma persona que representa um dos usuários finais dessa solução. Tiago é um técnico de 32 anos, casado, com ensino técnico completo e atua na área de ensaios minerais. Ele enfrenta uma dor comum a muitos profissionais dessa área, que é o processo manual de separação magnética que demanda muito tempo e esforço repetitivo e maçante, além de apresentar baixa precisão devido a erros humanos ao manter a distância do ímã constante.

![image](https://user-images.githubusercontent.com/99221221/221011051-d283f015-dc3d-49fe-9435-14929ac38111.png)

Com a compreensão das dores e objetivos do usuário, podemos desenvolver uma solução que atenda às suas necessidades, aumentando a eficiência e precisão do processo de separação magnética e permitindo que o usuário dedique seu tempo a tarefas mais relevantes e estimulantes. Dessa forma, a criação de personas é uma etapa crucial no processo de design de soluções, pois permite que o produto final seja desenvolvido de forma mais eficiente e eficaz, com foco nas necessidades do usuário.

## Histórias dos usuários (user stories)

User stories são uma técnica amplamente utilizada em metodologias ágeis de desenvolvimento de software para capturar as necessidades e requisitos dos usuários de maneira clara e sucinta. Essas histórias são escritas em linguagem natural e descrevem a funcionalidade que o usuário deseja ou precisa ter para alcançar um objetivo específico. 

As user stories geralmente incluem uma descrição do usuário, o que ele deseja realizar e o motivo pelo qual isso é importante para ele. Essas histórias são uma forma eficiente de capturar requisitos complexos em pequenos fragmentos de funcionalidade, permitindo que a equipe de desenvolvimento trabalhe de maneira mais ágil e iterativa. 

Nesta documentação de solução, as user stories podem ser usadas para definir os requisitos do sistema de maneira clara e concisa, facilitando a comunicação e a colaboração entre a equipe de desenvolvimento e os usuários finais.

**Épico 1: Como técnico, quero separar o material magnético de uma amostra com eficiência e precisão**

* Como técnico, quero iniciar o ensaio com um botão para que ele seja executado automaticamente.
* Como técnico, quero ajustar a intensidade magnética do eletroímã para capturar materiais diferentes com a mesma amostra.
* Como técnico, quero ajustar o número de passadas do ensaio para adaptá-lo à duração ideal de cada tipo de amostra.
* Como técnico, quero que o braço mecânico colete, limpe e despeje os materiais em cada bandeja automaticamente.
* Como técnico, quero que o sistema mantenha a distância e intensidade magnética constante para garantir resultados precisos e confiáveis.

**Épico: Como técnico, quero acessar relatórios precisos e padronizados de cada ensaio para análise de dados**

* Como técnico, quero ter acesso ao histórico de separações magnéticas para uma referência futura.
* Como técnico, quero poder filtrar os resultados para analisar dados específicos com mais facilidade.
* Como técnico, quero que os relatórios incluam informações como a data e hora do ensaio, o tipo de material testado e os detalhes de cada ciclo em um certo ensaio para que eu possa rastrear e analisar os dados com mais facilidade.

# Arquitetura do Sistema

A utilização de braços robóticos para automação de processos industriais é cada vez mais comum, trazendo ganhos em produtividade e qualidade. No entanto, para aplicações específicas, como a separação magnética, é necessário um sistema que seja capaz de controlar eletroímãs e bombas d'água de forma precisa e eficiente, garantindo a captura e limpeza dos materiais analisados.

Neste contexto, apresentamos uma arquitetura de solução que utiliza um Raspberry Pi Pico W e um Dobot Magician Lite para controlar os eletroímãs e bombas d'água necessários para a separação magnética. Além disso, o sistema conta com duas pontes H para o controle dos motores das bombas, uma conexão sem fio com a internet e um servidor com front-end em React para monitoramento e controle remoto do sistema. Nesse sentido, o servidor também cumpre a função de controlar o movimento do braço robótico e garantir a lisura e integração de todo o processo.

Com essa arquitetura, espera-se que o sistema de separação magnética seja capaz de realizar a tarefa de forma mais eficiente e precisa, trazendo mais praticidade e segurança para o usuário.


## Diagrama geral
![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/Arquitetura%20Do%20Sistema/arquitetura.jpg)

**Legenda do Diagrama**

| Componente / Conexão                                      | Descrição da função                                                                                                                                                                                                                                                                                                                                                           | Tipo: entrada / saída / atuador |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Raspberry Pi Pico W                                       | Microcontrolador responsável por gerenciar o eletroímã e as bombas d’água, segundo parâmetros passados pelo usuário no browser através de uma API com o servidor.                                                                                                                                                                                                             | Microcontrolador                |
| Dobot Magician Lite                                       | Braço robótico responsável por movimentar o eletroímã sobre as bandejas. segundo sequência pré-programada e critério de parada.                                                                                                                                                                                                                                               | Robô                            |
| Eletroímã                                                 | Gera campo magnético dinamicamente segundo instruções do Raspberry.                                                                                                                                                                                                                                                                                                           | Atuador                         |
| Bomba d’água                                              | Responsável por agitar a água na bandeja de captura e na bandeja de limpeza.                                                                                                                                                                                                                                                                                                  | Atuador                         |
| Rede local, servidor,  banco de dados e interface gráfica | Interface gráfica do sistema, pela qual o usuário se comunicará com o robô e com o microcontrolador. A interação do usuário final ocorre no browser e/ou executável, que envia as informações ao servidor. O servidor, por sua vez, comunica-se com o banco de dados para assegurar a persistência dos inputs e os redireciona ao hardware (Raspberry e Dobot Magician Lite). | Entrada e saída                 |
| Fonte elétrica                                            | Fornece eletricidade ao Raspberri, que agira como regulador de tensão, distribuindo energia ao resto do circuito, e ao robô.                                                                                                                                                                                                                                                  | Entrada (alimentação elétrica)  |
| Bandeja de captura                                        | Contém amostra inicial misturada em água, o qual é agitado pela bomba d’água a fim de elevar partículas à superfície do líquido.                                                                                                                                                                                                                                              | N/A                             |
| Bandeja de limpeza                                        | Recipiente utilizado para remover impurezas do material atraído pelo ímã, com o auxílio do atrito causado por uma bomba d’água.                                                                                                                                                                                                                                               | N/A                             |
| Bandeja de despejo                                        | Recebe o material magnético limpo.                                                                                                                                                                                                                                                                                                                                            | N/A                             |
| IR-SF (Interface gráfica e rede local - sem fio)          | As informações inseridas na interface gráfica são redirecionadas ao servidor através da rede local.                                                                                                                                                                                                                                                                           | Conexão                         |
| RS-SF (Rede local e servidor - sem fio)                   | A rede local direciona dados da interface gráfica ao servidor.                                                                                                                                                                                                                                                                                                                | Conexão                         |
| SBA-SF (Servidor e banco de dados - sem fio)              | Servidor acessa banco de dados para manipular dados persistentes.                                                                                                                                                                                                                                                                                                             | Conexão                         |
| HR-SF (Hotspot e rede local - sem fio)                    | Hotspot detecta rede local e viabiliza conexão do Raspberry com ela através de uma interface gráfica de WiFi Manager, que recebe SSID e senha.                                                                                                                                                                                                                                | Conexão                         |
| RH-SF (Raspberry e hotspot - sem fio)                     | Raspberry gera e conecta-se a uma AP para encontrar as redes locais e possibilitar conexão.                                                                                                                                                                                                                                                                                   | Conexão                         |
| RR-SF (Raspberry e rede local - sem fio)                  | Raspberry se comunica com a rede local para receber dados do usuário e comunicar estado geral do sistema à interface gráfica.                                                                                                                                                                                                                                                 | Conexão                         |
| MAS-CF (Magician Lite e Servidor - com fio)               | O robô é conectado com cabo ao servidor para receber instruções da interface gráfica.                                                                                                                                                                                                                                                                                         | Conexão                         |
| RE-CF (Raspberry e eletroímã - com fio)                   | O Raspberry controla a intensidade magnética gerada pelo eletroímã, através do gerenciamento da voltagem, utilizando sinais de PWM.                                                                                                                                                                                                                                           | Conexão                         |
| RBI-CF (Raspberry e bombas d’água iniciais - com fio)     | O Raspberry controla as bombas d’água na primeira bandeja para agitar a amostra.                                                                                                                                                                                                                                                                                              | Conexão                         |
| RBL-CF (Raspberry e bombas d’água de limpeza - com fio)   | O Raspberry controla as bombas d’água na segunda bandeja para limpar o material coletado.                                                                                                                                                                                                                                                                                     | Conexão                         |
| FMA-CF (Fonte elétrica e Magician Lite - com fio)         | A fonte elétrica alimenta o robô.                                                                                                                                                                                                                                                                                                                                             | Conexão                         |
| FR-CF (Fonte elétrica e Raspberry - com fio)              | A fonte elétrica alimenta o Raspberry.                                                                                                                                                                                                                                                                                                                                        | Conexão                         |

## Projeto mecânico
O projeto mecânico para nossa solução envolve três módulos: 

- um suporte para o ímã que fica na ponta do braço;
- um invólucro resistente à água que protege os ímãs nesse suporte;
- uma case simples para o circuito principal, incluindo Raspberry, placa e pontes H, a ser posicionada na traseira do robô.

As conexões por fio foram organizadas ao longo do corpo do robô utilizando fixadores como fita adesiva, a fim de diminuir o risco de nós, curto-circuito ou qualquer outro dano à integridade eletrônica do projeto.


**Visão Superior**

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiVisaoSuperior.png?raw=true)

O suporte para PCB foi produzido em plástico ABS, através de impressão 3D. Escolhemos esse material por sua durabilidade, facilidade de processamento e baixo custo. Essas características são importantes para oferecer uma solução robusta, capaz de suportar choques mecânicos simples a um reduzido investimento inicial. Ademais, por não ser transparente, cumpre a tarefa de ocultar o circuito de vista, otimizando a experiência do usuário. Por fim, como essa case não entrará em contato direto com a água, não é necessário total impermeabilidade, viabilizando o uso da impressão 3D.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/projeto%20mecanico/case.jpeg?raw=true)

O case tem as dimensões 12 cm x 12 cm x 5 cm e fica posicionado logo atrás do braço robótico. Cumpre a função de organizar o circuito principal e abstraí-lo do uso do usuário final, melhorando, assim, sua experiência com o produto.

O suporte para PCB está feita e pronta para ser impressa mas por motivos de tempo o suporte para PCB não conseguiu ser produzido

**Visão Lateral**


![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiVisaoLateral.png?raw=true)

O suporte para ímãs consiste em uma case octagonal, na qual são fixados quatro ímãs. Por entrar em contato direto com a água, é essencial que o material de fabricação seja muito resistente a líquidos e, ao mesmo tempo, exerça interferência mínima no campo magnético. 


![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/projeto%20mecanico/suporte_ima.png?raw=true)


Nesse sentido, produzimos a placa ortogonal em ABS através de impressão 3D, sob a qual os ímãs foram posicionados. Então, agregamos uma capa de plástico flexível para assegurar a resistência à água. 

**Visão Robô**

A figura abaixo apresenta as dimensões do braço robótico Magician Lite, conforme especificações do fabricante.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiRobo.png?raw=true)

### Validação dos dispositivos mecânicos fabricados

#### Suporte para ímãs
#### Case para PCB

## Projeto eletrônico

Como demonstrado na arquitetura da solução, o âmbito eletrônico do nosso projeto contempla, em visão geral, uma Raspberry Pi Pico W, eletroímãs e bombas d'água. A conexão entre esses componentes, por sua vez, é viabilizada através de reguladores de tensão e pontes H.

###  Esquemático do circuito
![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/Arquitetura%20Do%20Sistema/esquematicoDoCircuito.png)

Conforme a figura, nosso circuito utiliza 10 pinos da Raspberry Pi Pico W, duas bombas d'água, quatro eletroímãs, duas pontes H e um regulador de tensão. Tudo isso é alimentado por uma fonte de 5V. 

Nesse contexto, o regulador de tensão é empregado para amplificar essa voltagem aos 12V necessários para o correto funcionamento dos eletroímãs. Desse modo, o componente recebe os 5V nas portas VCC IN/GND e envia 12V nas portas VCC OUT/GND. Estas, por sua vez, conectam-se diretamente à ponte H responsável por controlar os quatro eletroímãs. 

Nesta ponte H, conectamos dois ímãs de cada lado, em paralelo. Assim, pudemos controlar um par por vez através dos pinos de direção da ponte. Esses pinos foram ligados aos GPIOs 11, 12, 14 e 15 do microcontrolador, para que pudessem ser utilizados em PWM para variar a intensidade do campo magnético.

Já a segunda ponte H é alimentada diretamente pelos 5V e controla as duas bombas d'água. Não foi necessário utilizar o regulador de tensão nesta parte porque a especificação de voltagem das bombas é exatamente de 5V. Assim, conectamos os pinos de direção delas também a quatro GPIOs do microcontrolador (8, 9, 10, 11).

###  Implementação do circuito
A implementação do circuito se deu em uma placa perfurada de dimensão 12x18 cm, na qual foram soldados o microcontrolador e os fios de conexão entre componentes. Esses fios foram posicionados no lado inferior da placa por motivos estéticos. Ademais, por falta de suporte específico, ficaram apenas acoplados, através de jumpers soldados, as pontes H, o regulador de tensão e as bombas d'água. 

Nesse sentido, durante os testes, para minimizar riscos de curto-circuito e/ou contato com água, utilizamos fita isolante para proteger as soldas expostas, ampliamos os fios de conexão dos atuadores e prendemos essas conexões ao corpo do robô com fita adesiva.

#### Componentes utilizados
| Unidades | Nome | Link |
|------|-----------|-------|
| 2x  | Ponte H L298N     | [ datasheet ](https://files.comunidades.net/mutcom/Driver_Motor_ponteH__L298N.pdf)  |
| 1x| Regulador de Tensão Ajustável MT3608    | [ datasheet ](https://www.olimex.com/Products/Breadboarding/BB-PWR-3608/resources/MT3608.pdf)    |
| 1x| Raspberry Pi Pico W    | [ datasheet ](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)    |
| 4x| Eletroímã 12v    | [ compra ](https://produto.mercadolivre.com.br/MLB-1756894287-eletroim-12vdc-12v-5kg-forca-de-033a-_JM#position=12&search_layout=stack&type=item&tracking_id=f99d5a87-91f9-4bc5-bf67-01991f1188e0)    |
| 2x| Bomba d'água submersível Dc 3-5V 100l / H    | [ compra ](https://shopee.com.br/Bomba-D-'%C3%81gua-Submers%C3%ADvel-Pet-Mini-Dc3-5V-100l-H-Acess%C3%B3rios-Tanque-De-Peixes-Silenciosa-Para-Aqu%C3%A1rio-i.298167688.4751307098)    

#### Validação dos dispositivos eletrônicos

Os testes de validação de nosso circuito foram executados utilizando o mesmo código-fonte do teste de componentes. Nesse contexto, empregamos a interface gráfica da página "/demo" do frontend. Como esta seção trata dos dispositivos eletrônicos, relatamos apenas os testes referentes a essa parte do sistema (excluímos metas para braço robótico e feedback na interface gráfica).

| Componente                             | Entrada                                                       | Saída esperada                                                                   | Resultado do teste                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eletroímãs                              | Acionamento do botão de "ligar" na interface gráfica          | Emissão de campo eletromagnético nos ímãs, atraindo objetos magnéticos.            | Fracasso. Ao apertar o botão, os ímãs apresentaram forte tremor e não atraíram objetos magnéticos consistentemente. Materiais de maior massa foram particularmente difíceis de atrair, sendo necessário posicioná-los manualmente, sobre o ímã , assegurando contato direto, para se obter sucesso.                                                                                                                                                                         |
| Eletroímãs                              | Acionamento do botão de "desligar" na interface gráfica       | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados. | Fracasso. Ao apertar o botão, os ímãs não soltaram os materiais captados consistemente. Isso ocorreu especialmente com objetos de menor massa, que permaneceram fixados à base dos ímãs mesmo após seu desligamento. Para soltá-los, foi necessário movê-los manualmente.                                                                                                                                                         |
| Bombas d'água                           | Acionamento do botão de "ligar" bombas d'água na interface gráfica            | Ativação das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas ativaram-se corretamente.                                                                                                                                                                                                           |
| Bombas d'água                           | Acionamento do botão de "ligar" bombas d'água na interface gráfica            | Desligamento das bombas                                  | Sucesso. As bombas desativaram-se corretamente.                                                                                                                                                                                                           |
| Acionamento dos eletroímãs na rotina integrada                          | Braço robótico posicionado sobre ou entre a primeira e segunda bandejas       | Emissão de campo eletromagnético nos ímãs, atraindo objetos magnéticos.                                 | Fracasso. Apesar dos ímãs ativarem-se nos período desejado, eles não apresentaram campo magnético suficiente para atrair materiais consistentemente. Também apresentaram forte tremor.                                                                                                                                                                                                         |
| Desligamento dos eletroímãs na rotina integrada                          | Braço robótico posicionado sobre a terceira bandeja            | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados.                                 | Fracasso. Embora os ímãs tenham sido desativados, objetos de menor massa continuaram fixados à base dos atuadores, sendo preciso removê-los manualemente.                                                                                                                                                                                                           |
| Acionamento das bombas d'água na rotina integrada                          | Braço robótico posicionado sobre a segunda bandeja            | Ativação das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas ativaram-se corretamente.                                                                                                                                                                                                           |
| Desligamento das bombas d'água na rotina integrada                          | Braço robótico posicionado fora da segunda bandeja            | Desligamento das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas desativaram-se corretamente.                                                                                                                                                                                                           |
                                                       
**Considerações sobre eletroímãs:** O fracasso obtido nos testes com quatro ímãs foi inesperado, pois a validação de um único ímã havia funcionado perfeitamente. Frente ao problema, nossa primeira hipótese foi que houvesse um erro de código, conexão física, ou interferência entre os campos magnéticos. 

Entretanto, ao examinar a voltagem em diferentes pontos do circuito utilizando um voltímetro, descobrimos que, apesar de a ponte H receber 12V do regulador de tensão, ela está enviando apenas 0,65V-0,75V para os ímãs. Logo, acreditamos ser um problema de divisão de corrente dentro do componente. 

Na Sprint 5, descobrimos que esse erro originou-se da falta de conexão da ponte H com o GND do microcontrolador. Ao soldar essa conexão, os eletroímãs voltaram a funcionar conforme o esperado.


## Tecnologias Utilizadas
### Testes de componentes
#### Movimentação do robô

A movimentação do robô foi testada em três etapas. Inicialmente, fizemos uma exploração das funcionalidades do Magician Lite com o auxílio do software de controle Dobot Studio. Nesse momento, utilizamos os controles manuais da plataforma para nos familiarizarmos com os de periféricos disponíveis, como a garra, a sucção e a caneta. Com isso, também aprendemos mais sobre os limites físicos do robô, no que tange a envelope de trabalho em diferentes configurações das articulações. 

Começando a testar as funcionalidades de programação do robô, configuramos o desenho de um vetor de alta complexidade. Para isso, seguimos os seguintes passos:

1. Fizemos o download do [vetor desejado](https://drive.google.com/file/d/1btHzWGOxXzzZMx91I4lkRq3Hw46jGhcT/view?usp=sharing
) (em svg)
1. Conectamos o robô à fonte e ao computador via USB
2. Trocamos a ponta do robô pelo suporte de caneta
3. Posicionamos um caderno A3 horizontalmente à frente do robô, sob a ponta
4. Calibramos a altura manualmente, utilizando os controles do software, para que a ponta da caneta trocasse o papel
5. Acessamos a seção de "Write & Draw" do Dobot Studio
6. Importamos o vetor na área de configuração de desenho
7. Redimensionamos e reposicionamos o vetor para que ela ficasse contida nos limites do caderno
8. Pressionamos o botão 'AutoZ' para desativá-lo. Isso evita que o robô modifique a altura da caneta, que foi calibrada no passo 4
9.  Pressionamos o botão 'Start'

A execução do desenho levou em torno de 10 minutos. Um vídeo acompanhando o processo se encontra abaixo.

[Teste de desenho](https://drive.google.com/file/d/1DKwGRYJMMwX0WrUkw78yCvqYAucw6ZM4/view?usp=share_link)

Na segunda etapa, objetivamos movimentar o robô diretamente por scripts em Python. Para isso, seguimos os seguintes passos:

1. Instalamos a biblioteca (API) de comunicação Pydobot através de 'pip install pydobot'
2. Conectamos o robô à fonte e ao computador via USB
3. Descobrimos qual porta estava conectada ao robô através de tentativa e erro na interface do Dobot Studio. Isso foi feito apertando o botão "Conectar" para cada opção de porta até que a conexão fosse bem-sucedida.
4. Utilizamos um código de exemplo de movimentação simples, trocando o argumento de porta pela porta encontrada na etapa 3 (no caso, 'COM7')

```
from serial.tools import list_ports

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = 'COM7'

device = pydobot.Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.move_to(x + 20, y, z, r, wait=False)
device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing

device.close()
```

5. Executamos o código

O teste foi bem-sucedido e o robô se movimentou conforme esperado. A partir daí, passamos algum tempo testando diferentes argumentos e operações algébricas na função move_to(). Nesse momento, descobrimos que os limites de envelope de trabalho também se aplicam a essa função, de modo que, quando o robô está posicionado em certos pontos, ele é incapaz de se movimentar para alguns outros pontos específicos. 

Posteriormente, mapeamos as coordenadas desejadas para a movimentação do robô sobre as três bandejas, almejando quatro posições em cada: duas altas e duas baixas. Como os valores de altura e de rotação eram constates, também os substituímos por variáveis. Ademais, adicionamos "pontos de volta" no final do ciclo, correspondentes ao ponto alto final das bandejas 2 e 3, para facilitar a volta do robô. Sem eles, o braço travaria devido às limitações do envelope de trabalho. Este foi o array resultante:

```
high_height = 70
low_height = -32
rotation = -86

tray_coordinates = [
    # BANDEJA 1
    (35, -248, high_height, rotation), # Ponto alto inicial
    (35, -248, low_height, rotation), # Ponto baixo inicial
    (216, -248, low_height, rotation), # Ponto baixo final
    (216, -248, high_height, rotation), # Ponto alto final

    # BANDEJA 2
    (263, -112, high_height, rotation), # Ponto alto inicial
    (263, -112, low_height, rotation), # Ponto baixo inicial
    (263, 68, low_height, rotation), # Ponto baixo final
    (263, 68, high_height, rotation), # Ponto alto final

    # BANDEJA 3
    (222, 255, high_height, rotation), # Ponto alto inicial
    (222, 255, low_height, rotation), # Ponto baixo inicial
    (19, 255, low_height, rotation), # Ponto baixo final
    (19, 255, high_height, rotation), # Ponto alto final

    # PONTOS INTERMEDIÁRIOS PARA REINICIAR
    (222, 255, high_height, rotation), # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation) # Ponto alto inicial da bandeja 2
]
```

Então, juntamos esse array com um código de execução básico:

```
for coordinate in tray_coordinates: 
  device.move_to(*coordinate, wait=True)
```

Rodando tudo isso, conseguimos fazer o braço se movimentar uma vez sobre cada bandeja, conforme vídeo abaixo.

[Movimentação simples](https://drive.google.com/file/d/1U_hwCO9obIUuMkyjYx5wSZpOMIPoqCgo/view?usp=share_link)

Por fim, iniciamos a implementação um servidor simples em Flask para automatizar uma movimentação específica através de uma interface gráfica web. Para isso, fizemos uma rota GET que, quando requisitada, executa a função de movimentação do robô. Este código, por ser muito extenso, está disponível na pasta src deste repositório git. Como ainda não foi completamente desenvolvido, não há vídeos mostrando seu funcionamento integral. Isso é uma meta para a Sprint 3.

#### Eletroímã na ponte H

Um dos fatores fundamentais em nosso projeto é o uso de um eletroímã acoplado ao braço robótico. Com ele, será possível não só ativar e desativar o campo magnético, permitindo a programação da captura e despejo de partículas magnéticas, como também será possível varial a intensidade do campo produzido a fim de atrair diferentes categorias de material.

Nesse sentido, inicialmente testamos um eletroímã diretamente na fonte de 12V (a voltagem máxima do eletroímã). Como esperado, ele foi capaz de atrair uma moeda de dez centavos quando ligado na fonte e a soltou quando o desconectamos. Tendo esse conhecimentos, passamos a estudar a integração do ímã com o Raspberry Pi Pico W. A dificuldade, nesse momento, era alimentar uma voltagem variável ao ímã superior à voltagem disponível no VCC do microcontrolador (3V3).

Para solucionar isso, conectamos o ímã a uma ponte H. Dessa forma, pudemos alimentar a ponte continuamente com os 12V enquanto controlávamos o estado (ativado/desativado) do ímã através dos pinos de direção da ponte, responsáveis por inverter a polaridade da voltagem. Seguindo a lógica de ponte H, para que o ímã ligasse, apenas um pino deveria estar ativo. Com ambos ligados ou desligados, o ímã permanecia desativado. Nesse contexto, os pinos foram conectados a pinos de output do Raspberry, de modo que o microcontrolador decidisse, através de sinais binários, quais pinos da ponte H deveriam ser ativados. Ademais, a entrada positiva da ponte H foi conectada diretamente à fonte, enquando a entrada negativa foi conectada em paralelo à saída negativa da fonte e do GND do Raspberry.

Feita essa configuração de hardware, iniciamos os testes com código. Pensando apenas no comportamento binário, construímos um programa simples que envia sinal de HIGH para apenas um pino na função de ligar o ímã, e mandava sinais de LOW para ambos os pinos na função de desligar o ímã. O código está disponível abaixo.

Como observação, ao ligar a ponte h na fonte de alimentação, foi possivel reparar a necessidade de aumentar a tensão em 2 vols para que a ponte h funcionasse em sua capacidade total.


```
import machine

magnet_pin_1 = machine.Pin(16, machine.Pin.OUT)
magnet_pin_2 = machine.Pin(15, machine.Pin.OUT)

def enable_magnet():
    magnet_pin_1.value(1)
    magnet_pin_2.value(0)

def disable_magnet():
    magnet_pin_1.value(0)
    magnet_pin_2.value(0)

```

Então, chamamos cada função separadamente em diversas execuções. O resultado foi conforme o esperado.

O próximo passo foi dinamizar a intensidade do ímã. O método utilizado para esse fim foi o PWM (Pulse Width Modulation). Ele consiste em alternar rapidamente a tensão aplicada ao dispositivo entre níveis altos e baixos em um determinado ciclo de tempo, conhecido como período. Ao variar a largura dos pulsos (ou seja, a quantidade de tempo que a tensão é mantida alta em relação ao período), é possível controlar a tensão média aplicada ao dispositivo. Por exemplo, se a tensão é alternada entre 0V e 12V com uma frequência de 1kHz e uma largura de pulso de 50%, a tensão média aplicada seria de 6V.

Nesse sentido, para atingir a intensidade magnética de qualquer voltagem abaixo de 12V, bastaria enviar uma largura de pulso proporcional à fração de voltagem desejada. Felizmente, o Micropython, linguagem utilizada para programar o Raspberry Pi Pico W, possui um método nativo para PWM. Nosso código, então, começava com a declaração dos pinos como pinos PWM, em vez de apenas pinos binários. Também definimos a frequência como 1kHz, como valor de teste.

```
import machine

magnet_pin_1 = machine.PWM(machine.Pin(16, machine.Pin.OUT))
magnet_pin_2 = machine.PWM(machine.Pin(15, machine.Pin.OUT))

magnet_pin_1.freq(1000)
magnet_pin_2.freq(1000)

```
Depois, atualizamos as funções de ligar e desligar o ímã. Nessa primeira, adicionamos um argumento de voltagem desejadas e aplicamos o método PWM.duty_u16() para definir a largura de pulso a ser enviada ao pino. Um ponto importante nesta etapa é que a unidade desse argumento não deveria ser passada na porcentagem escolhida (50%, por exemplo), e sim no valor proporcional no intervalo 0 a 65535. Logo, tivemos de converter a voltagem desejada para a fração dessa escala em cada chamada da função de duty_u16(). A função de desligar, por sua vez, passava 0 como argumentos para ambos os pinos.

```

def enable_magnet(voltage):
    magnet_pin_2.duty_u16(0)
    magnet_pin_1.duty_u16(int(voltage / 12.0 * 65535))

def disable_magnet():
    magnet_pin_1.duty_u16(0)
    magnet_pin_2.duty_u16(0)

```
Executando essas funções com diferentes voltagens, atingimos o comportamento esperado, com a intensidade da atração entre o ímã e os materias magnéticos de teste variando conforme aumentávamos e diminuíamos o argumento de voltagem.

Feito isso, adicionamos rotas no servidor e um botão no frontend para controlar o liga e desliga do ímã, ainda sem variação da voltagem. Este código está disponível na pasta src deste repositório git, por ser muito extenso para adicionar aqui. Dito isso, o vídeo abaixo demonstra seu funcionamento:

[Ímã ligando e desligando no front](https://drive.google.com/file/d/1tNGGaVWdjG-uf2RkJPIhACx0uDh1AWXc/view?usp=share_link)

Por fim, voltando ao código de movimentação do robô visto no final do teste anterior, adicionamos uma linha que ativava a sucção da ponta. 

```
device.suck(True)
for coordinate in tray_coordinates: 
  device.move_to(*coordinate, wait=True)
```

Com isso, pudemos conectar o ímã ao movimento braço robótico:

[Ímã conectado ao braço](https://drive.google.com/file/d/1nGkIPEVVNb14Duce5NOnQtC0NVbb49da/view?usp=share_link)


#### Bomba d'água na ponte H

Similarmente ao eletroímã, a bomba d'água também requereu o uso do ponte H por exigir voltagem acima de 3V3. Ainda assim, inicialmente, fizemos um teste conectando-a diretamente a fonte em 12V. Como esperado, ela foi ativada e movimentou a água significativamente.

[Bomba d'água na fonte](https://drive.google.com/file/d/1jfaO7tCQ4pp-55x3oSPvWAU1O0QgRn3F/view?usp=share_link)

Depois, conectamos a bomba à ponte H e ligamos os pinos de sentido restantes a dois pinos digitais livres do Raspberry. Implementamos, então, funções de ligar e desligar, semelhantemente ao primeiro código utilizado para o eletroímã. Nesse caso, o pino ativado influencia no sentido de rotação da bomba. Ainda assim, como esse sentido não influencia no objetivo do uso da bomba (movimentar a água para dispersar material e lavar impurezas), pode-se ativar qualquer um dos pinos. Semelhante, como não é necessário alterar a intensidade da bomba, não tivemos que trabalhar PWM neste teste.


```
import machine

pump_pin_1 = machine.Pin(16, machine.Pin.OUT)
pump_pin_2 = machine.Pin(15, machine.Pin.OUT)

def enable_pump():
    pump_pin_1.value(1)
    pump_pin_2.value(0)

def disable_pump():
    pump_pin_1.value(0)
    pump_pin_2.value(0)

```

O teste unitário de cada função foi bem-sucedido. Então, conectamos essas funções também a rotas de servidor e um botão na interface gráfica, conforme descrito na pasta src deste repositório git. O vídeo abaixo sumariza o funcionamento final dos componentes da ponte H integrados ao frontend:

[Componentes integrados](https://drive.google.com/file/d/1iMuU_Au-HOIZtkMis8Z6_jKLUNROaPFZ/view?usp=sharing)

Como observação, ao ligar a ponte h na fonte de alimentação, foi possivel reparar a necessidade de aumentar a tensão em 2 vols para que a ponte h funcionasse em sua capacidade total.


#### Sensor de campo eletromagnético

Um dos objetivos deste projeto é estimar o peso do material magnético captado pelo eletroímã sem depender da secagem do mesmo. Nossa ideia inicial para isso foi acoplar um sensor magnético atrás do eletroímã, a fim de aproximar o peso da amostra através das variações no campo magnético conforme mais material fosse captado. 

Para testar essa hipótese, utilizamos um sensor de efeito hall KY-024 em um circuito simples. Esse circuito continha um LED de feedback, que brilharia quando o sensor captasse campo magnético. Assim, nesse primeiro teste, o comportamento esperado era binário, informando apenas se havia algum campo significativo na região.

Um esquemático do circuito do sensor pode ser visto abaixo. O capacitor, em cinza, não foi utilizado, e o LED foi conectado separadamente, em outra porta do Raspberry, e controlado apenas por código.

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/sensor_campo_magnetico/hall_effect_sensor_circuit.png)

O código, por sua vez, foi o seguinte:

```
import machine
led = machine.Pin(18, machine.Pin.OUT)
sensor = machine.Pin(14, machine.Pin.IN)

while True:
    if(sensor.value() == 1):
        led.HIGH()
    else:
        led.LOW()
```

O funcionamento pode ser visto no vídeo abaixo:

[Sensor de campo eletromagnético](https://drive.google.com/file/d/1ZvMhhsyrQqPlQ1OZxav6_Ht2Wmu-avOB/view?usp=share_link)

Posteriormente, refatoramos esse código para que ele lesse valores analógicos, a fim de examinar as variações no campo perante a quantidade de material atraído pelo ímã. Para isso, trocamos o tipo de pino por ADC e utilizamos a função read_u16.

```
import machine
sensor = machine.ADC(28)

while True:
    print(sensor.read_u16())
    time.sleep(0.1)
```

Infelizmente, neste teste, as leituras obtidas se concentravam em três intervalos muito distantes entre si: quando o ímã estava desligado, o console exibia leituras em torno de 800; com o ímã a média distância, líamos 20.000 a 27.000; por fim, com o ímã muito perto, tínhamos 64.000-65.000. O vídeo abaixo exibe o comportamento errático.

[Leituras do sensor](https://drive.google.com/file/d/1FX70Vs9eu51dPvugF0spTe9vWaQVk8CA/view?usp=sharing)

De todo, esses saltos eram bruscos e não representavam as microvariações que pretendíamos analisar. Com isso, percebemos que esse sensor não atenderá nossos objetivos. Concluímos, portanto, ser de fato necessário utilizar a célula de carga para estimar o peso da amostra.

#### Célula de carga e amplificador HX711

A célula de carga converte uma força em um sinal elétrico que pode ser medido. Este sinal irá mudar proporcionalmente à força aplicada. A células de carga é composta por uma barra de metal com extensômetros fixados. Os extensômetros são sensores elétricos que medem força ou tensão em um objeto. Quando uma força externa é aplicada a um objeto, como a barra de metal, ocorre uma deformação em sua forma, o que faz com que a resistência dos extensômetros varie. A mudança na resistência é proporcional à carga aplicada, permitindo-nos calcular o peso dos objetos.

Sabe-se que existem alterações de tensão, todavia, como essas mudanças são muito pequenas, é necessário um amplificador. O amplificador utilizado se chama HX711 e se comunica com o microcontrolador utilizando de uma interfaze de dois fios, "Clock" e "Data". Para realizar o teste foi preciso prender a célula de carga de maneira a criar uma tensão entre as extremidades opostas da barra de metal. 

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/celula_de_carga/c%C3%A9lula_de_carga_entre_placas.png)

Após isso, foram feitas as seguintes ligações:

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/celula_de_carga/conexoes_celula_de_carga.png)

O teste consistiu em duas etapas: a calibração da célula e a medição de peso de objetos previamente conhecidos. A primeira etapa é crucial para o teste, pois é a partir dela que determinamos o fator de calibração, que pode ser obtido dividindo o valor lido pela célula pelo peso já conhecido. A segunda etapa consistiu na medição real dos objetos, utilizando o fator de calibração obtido na primeira etapa.

O código em sua íntegra está disponível em src/embedded/weight_cell. Não foi colocado neste relatório por ser muito extenso. Ainda assim, o vídeo abaixo demonstra o funcionalmento final.

[Vídeo do teste realizado](https://drive.google.com/file/d/19G_qC6mr0JAeuuYVfvO6fVKM8mR57QWV/view?usp=share_link)

Isso tudo foi testado em um ESP-32 com C++. Posteriormente, ao tentar diversas vezes integrar a célula de carga em Micropython ao sistema sem sucesso, decidimos finalizar o projeto sem essa feature devido à falta de documentação online para o desenvolvimento desse tipo de tecnologia.

O principal da célula de carga é que seu output é um valor alto, por volta dos 11 mil. O que o código faz pega esse valor e faz as contas necessárias, deduzidas pela documentação da própria, para termos o valor real do peso. O código calibra a célula de carga e deixa pronto para a integração com o restante do código. A integração da célula de carga foi feita de forma muito parecida com as duas outras integrações, a do imã e a da bomba d'água. A única coisa que de fato muda quando compara as integrações é o código que chama o arquivo que faz a célula de carga funcionar.

### Relatório de entradas e saídas dos testes

| Componente                             | Entrada                                                       | Saída esperada                                                                   | Resultado do teste                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braço robótico                         | Acionamento do botão de início do ensaio na interface gráfica | Movimentação do robô segundo as coordenadas de posição programadas para o ensaio (quatro pontos sobre cada bandeja: ponto alto inicial, ponto baixo inicial, ponto baixo final e ponto alto final) | Sucesso. Robô se movimentou conforme o esperado.                                                                                                                                                                                                   |
| Eletroímã                              | Acionamento do botão de "ligar" na interface gráfica          | Emissão de campo eletromagnético no ímã, atraindo objetos magnéticos.            | Sucesso. Ao apertar o botão, o ímã atraiu uma moeda de dez centavos.                                                                                                                                                                               |
| Eletroímã                              | Acionamento do botão de "desligar" na interface gráfica       | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados. | Sucesso. Ao apertar o botão, o ímã soltou a moeda e parou de atrair materiais magnéticos.                                                                                                                                                          |
| Sensor de campo eletromagnético        | Aproximação de campo magnético                                | Iluminação do LED de feedback                                                    | Sucesso. Ao aproximar o ímã ligado, o LED acendeu.                                                                                                                                                                                                 |
| Sensor de campo eletromagnético        | Afastamento de campo magnético                                | Apagamento do LED de feedback                                                    | Sucesso. Ao afastar ou desligar o ímã, o LED se apagou.                                                                                                                                                                                            |
| Sensor de campo eletromagnético analógico     | Aproximação de campo magnético                                | Aumento gradual e granular do valor das leituras                                                    | Fracasso. Leituras passaram do intervalo de 800-900 para 20.000-27.000 e depois 64.000-65.0000.                                                                                                                                                                                            |
| Sensor de campo eletromagnético analógico     | Afastamento de campo magnético                                | Diiminuição gradual e granular do valor das leituras                                                    | Fracasso. Leituras passaram do intervalo de 64.000-65.0000 para 20.000-27.000 e depois 800-900.                                                                                                                                                                                            |
| Célula de carga e amplificador         | Adição de massa sobre a placa da célula de carga              | Exibição do peso da massa adicionada no console do microcontrolador              | Sucesso. A adição de um case de fone de ouvido foi reconhecida e corretamente pesada pela célula de carga. A acuracidade foi estimada através da comparação do peso calculado pela célula de carga com o peso calculado por uma balança calibrada. |
| Bomba d'água                           | Conexão da bomba d'água, na ponte H, à fonte em 5V            | Ativação da bomba em um dos sentidos de rotação.                                 | Sucesso. A bomba ativou-se corretamente.                                                                                                                                                                                                           |
| Contagem de ciclos (interface gráfica) | Repetição dos ciclos (passadas) do robô em um mesmo ensaio    | Atualização do número de ciclos (passadas) no frontend.                          | Sucesso. A linha de contagem de ciclos mudou conforme o esperado.                                                                                                                                                                                  |
| Contagem de ciclos (interface gráfica) | Finalização de um ensaio                                      | Reset da contagem de ciclos, voltando ao 0.                                      | Sucesso. Ao terminar um ensaio, assim que o robô parava de se movimentar, o contador voltava a 0.                                                                                                                                                  |

# UX e UI Design

Como linha geral, priorizamos elementos minimalistas, intuitivos e de fácil entendimento. Seguindo o estilo utilizado até agora nos slides e logotipos, apostamos em uma paleta de cores com alto contraste e foco em tons de roxo. 

A interface oficial apresenta uma sidebar simples, com tela inicial, histórico de relatórios e hub de adição de novos clientes, usuários e projetos. A tela principal, por sua vez, traz um botão de destaque para iniciar um ciclo, assim como campos de preenchimento de mais informações para cada execução.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/home1.png?raw=true)

Já na aba de histórico, tem-se ensaios antigos com diversas funcionalidades de filtragem. Ao clicar em qualquer card, pode-se ver mais informações sobre o ensaios e os ciclos que o compõem.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/history1.png?raw=true)

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/history2.png?raw=true)

Por fim, o hub de adição traz duas tabelas: de usuários e de clientes. 

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/add.png?raw=true)

Na tabela de clientes, pode-se clicar em qualquer um deles para ver seus projetos. 

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/projects.png?raw=true)

Ao clicar em "Adicionar" em qualquer tabela, tem-se um pop-ups para adicionar novos elementos.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/addUser.png?raw=true)

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/addClient.png?raw=true)

O design inicial do Figma pode ser conferido [aqui](https://www.figma.com/file/6mBFBLaAB9pjVo9Z3GzauB/Magnetum?node-id=23%3A2&t=tj4cyeV3llJXr2hb-1). Para a interface de testes, utilizamos um design simples, com um único vetor em tons de verde para decoração na base da página.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/interface_demo.png?raw=true)

# Backend

O backend do Magnetum foi feito em Flask utilizando um banco de dados em SQLite, construído com a ORM SQLAlchemy. O servidor foi estruturado com base na framework de MVC (Model-View-Controller); no entanto, como nosso frontend foi feito separadamente em React e Electron, não implementamos um módulo de views no backend. 

Em vez disso, separamos subpastas de "models", para modelos de tabela e classes de atuadores, "controllers", que coordena as funções dos modelos e manipula requisições, e "routes", que delega as requisições para seus respectivos controladores. Ademais, criamos uma pasta de "utils" para guardar Enums utilizados em vários scripts e uma pasta de "config" que armazena o arquivo de configuração do banco de dados com SQLAlchemy.

## Diagrama de banco de dados

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/backend/database_Erd.png?raw=true)

Nosso banco de dados possui cinco tabelas relacionadas. 
- **Client**: clientes do IPT, que solicitam ensaios de suas amostras. Podem ter vários projetos.
- **User**: usuários do sistema, isto é, técnicos do IPT.
- **Project**: projetos dos clientes, agregando vários ensaios de um mesmo contexto.
- **Routine**: ensaios de cada projeto, contendo vários ciclos
- **Cycle**: ciclos de cada ensaio

# Teste de Software

## Movimentação do robô

A movimentação do robô consiste em uma linha reta sobre cada bandeja. O movimento se inicia em um dos extremos do maior lado, posicionado no ponto médio do menor lado, e transpassa todo o comprimento da bandeja. Para isso, em cada recipiente, o robô primeiro posiciona-se sobre o ponto inicial a uma altura maior, abaixa-se até a altura desejada para contato com o material, transpassa a bandeja, assume a altura inicial neste novo ponto, e então passa para o ponto inicial da próxima bandeja.

Esse padrão de movimento mostrou-se bem-sucedido nos testes. Ao executá-lo, não obtivemos erros de movimentação do robô nem travamentos. Ademais, captamos os objetos metálicos desejados.

Em mais detalhes, as coordenadas utilizadas para cada ponto são as seguintes:

```
high_height = 77
low_height = -40
rotation = -86

tray1 = [
    (215, -155, high_height, rotation),  # Ponto alto inicial
    (215, -155, low_height, rotation),  # Ponto baixo inicial
    (315, -141, low_height, rotation),  # Ponto baixo final
    (315, -141, high_height, rotation),  # Ponto alto final
]

tray2 = [
    (326, 1, high_height, rotation),  # Ponto alto inicial
    #(263, -112, low_height, rotation),  # Ponto baixo inicial
    #(263, 68, low_height, rotation),  # Ponto baixo final
    (184, 1, high_height, rotation),  # Ponto alto final
]

tray3 = [
    (200, 157, high_height, rotation),  # Ponto alto inicial
    (200, 157, low_height, rotation),  # Ponto baixo inicial
    (311, 157, low_height, rotation),  # Ponto baixo final
    (311, 157, high_height, rotation),  # Ponto alto final
]

intermediary_points = [
    (222, 255, high_height, rotation),  # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation)  # Ponto alto inicial da bandeja 2
]

```

## Integração de hardware com frontend

Os testes de integração do hardware (movimentação do robô e acionamento dos atuadores conectados ao microcontrolador) com a interface gráfica foram bem-sucedidos. A integração se deu majoritariamente na página de "Home", tanto na versão online quanto na versão de executável do Magnetum. Os objetivos eram os seguintes:

- Iniciar movimentação do robô ao clicar no botão "Iniciar"
- Ligar/Desligar ímãs ao clicar no controle do ímã
- Ligar/Desligar bombas ao clicar no controle das bombas
- Atualizar número de ciclos durante a movimentação do robô
- Atualizar bandeja atual durante a movimentação do robô

Todos esses casos foram executados conforme o esperado, com as atualizações e modificações desejadas. Uma ressalva é que o comportamento dos ímãs foi relativamente inconsistente, com flutuações na intensidade. No entanto, após análise mais aprofundada, percebemos que isso se deu por problemas de conexão do próprio hardware, como a solda e a placa perfurada, e não da integração do código de frontend com o de backend e embarcado. Logo, consideramos os testes de integração um sucesso.

# Validação da eficácia do sistema

Para garantir a eficácia e usabilidade do sistema, foram realizados testes simulando o cenário real de uso da solução criada. As bandejas foram cuidadosamente posicionadas e todo o sistema, desde as peças de hardware até o software, foi iniciado. Foram utilizadas amostras reais cedidas pelo IPT, nosso parceiro no projeto, dos materiais que passam pelo processo de separação magnética. Após a ativação do sistema nessas condições, foi constatada a eficiência da solução na realização da separação magnética. De fato, após algumas passadas, pudemos conferir o depósito de material magnético na última bandeja, a diminuição da massa na primeira bandeja e o escurecimento da água na segunda bandeja, evidenciando a transferência e limpeza dos minerais.

[Funcionamento completo da solução](https://drive.google.com/file/d/1dWlpdSFzFSZiAK777VvRBB2AGD83wIbd/view?usp=sharing)

### Relatório de entradas e saídas do teste final

| **Componente**                                 | **Entrada**                                                                    | **Saída**                                                                                                                         | **Resultado do teste**         |
|------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Braço robótico                                 | Acionamento após pressionar botão de início                                    | Movimento de acordo com as coordenadas previstas.                                                                                 | Sucesso, ocorreu como esperado |
| Eletroímã                                      | Pressionamento do botão de iniciar sistema                                     | Eletroímã ligar na primeira e segunda bandeja e desligar na ultima para soltar material atraído.                                  | Sucesso, ocorreu como esperado |
| Eletroímã                                      | Alteração do input no slider de intensidade magnética                          | Alteração proporcional na voltagem recebida pelo eletroímã                                                                        | Sucesso, ocorreu como esperado |
| Bomba d'água                                   | Pressionamento do botão de iniciar sistema                                     | Bomba d'água ser ativada ao braço mecânico passar pela bandeja e desligar ao braço mudar de bandeja                               | Sucesso, ocorreu como esperado |
| Acionamento de componentes                     | Pressionamento do botão de iniciar sistema                                     | Braço robótico começa a se mover e componentes (bombas d'água e eletroímã) são ativados de acordo com a posição do braço robótico | Sucesso, ocorreu como esperado |
| Contagem dos ciclos (interface gráfica)        | Preenchimento da quantidade de ciclos necessários e inicio do sistema          | Indicação na interface gráfica da quantidade de ciclos realizados                                                                 | Sucesso, ocorreu como esperado |
| Indicação de bandeja atual (interface gráfica) | Pressionamento do botão de iniciar sistema                                     | Indicação na interface gráfica da posição do robô de acordo com bandeja em que braço robótico está                                | Sucesso, ocorreu como esperado |
| Integração com banco de dados                  | Acesso à página principal da interface gráfica                                 | Atualização dos itens nos dropdowns da página principal conforme cliente, usuário e projeto selecionados                          | Sucesso, ocorreu como esperado |
| Integração com banco de dados                  | Acesso à página de adição de componentes                                       | Atualização das tabelas de usuários, clientes e projetos conforme itens relacionados do banco de dados                            | Sucesso, ocorreu como esperado |
| Integração com banco de dados                  | Pressionamento do botão de adicionar das tabelas de cliente, projeto e usuário | Adição de novos itens na tabela mesmo após recarregamento da página                                                               | Sucesso, ocorreu como esperado |
| Integração com banco de dados                  | Acesso à página de histórico                                                   | Atualização dos cards com os ensaios já realizados                                                                                | Sucesso, ocorreu como esperado |
| Integração com banco de dados                  | Pressionamento no botão de um dos cards da página de histórico                 | Abertura de modal com mais informações, relacionando dados das tabelas de ensaio, usuário, cliente, projeto e ciclo               | Sucesso, ocorreu como esperado |



# Referências

[Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-load-cell-hx711/)
