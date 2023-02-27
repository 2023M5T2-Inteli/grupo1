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
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Descrição dos componentes](#descrição-dos-componentes)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Testes de componentes](#testes-de-componentes)
      - [Movimentação do robô](#movimentação-do-robô)
      - [Eletroímã na ponte H](#eletroímã-na-ponte-h)
      - [Bomba d'água na ponte H](#bomba-dágua-na-ponte-h)
      - [Sensor de campo eletromagnético](#sensor-de-campo-eletromagnético)
      - [Célula de carga e amplificador HX711](#célula-de-carga-e-amplificador-hx711)
    - [Relatório de entradas e saídas dos testes](#relatório-de-entradas-e-saídas-dos-testes)
- [UX e UI Design](#ux-e-ui-design)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
  - [Testes Unitários](#testes-unitários)
  - [Teste de Usabilidade](#teste-de-usabilidade)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
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

O Instituto de Pesquisas Tecnológicas (IPT) é uma instituição de pesquisa brasileira que tem como objetivo contribuir para o desenvolvimento científico, tecnológico e insdustrial do país. Fundado em 1899, é um dos mais antigos centros de pesquisa tecnológica do país e tem uma ampla variedade de áreas de atuação. O instituto possui uma ampla infraestrutura de laboratórios e centros de pesquisa, com equipamentos de última geração e uma equipe multidisciplinar de pesquisadores, engenheiros, técnicos e especialistas. Além disso, realiza parcerias com empresas e instituições de pesquisa nacionais e internacionais, visando a transferência de tecnologia e a cooperação científica.

## O Problema

O IPT possui uma área de atuação em materiais avançados e a separação magnética é uma técnica comumente utilizada para avaliar a liberação de minerais e materiais com propriedades magnéticas. Entretanto, devido ao processo de separação magnética ser manual, a medição da distância não é precisa, o que afeta diretamente a precisão do campo eletromagnético aplicado às partículas. Como o campo eletromagnético é inversamente proporcional à distância, a determinação do campo correto para separar os minerais se torna complicada. Além disso, para experimentar diferentes campos, é preciso alternar os ímãs utilizados, requerendo uma variedade de ímãs disponíveis.

## Objetivos

### Objetivos gerais

É necessário desenvolver um equipamento automatizado capaz de aplicar um campo magnético constante, com intensidade e distância ajustáveis, sobre toda a amostra. Isso permitirá separar os minerais magnéticos, que serão depositados em um recipiente diferente dos minerais não magnéticos, que permanecerão na bandeja original.

### Objetivos específicos

O objetivo é automatizar os ensaios de separação magnética em amostras de mineração, com a finalidade de aumentar a precisão e reduzir a intervenção humana no processo. Para alcançar esse objetivo, serão utilizados um braço robótico Dobot Magician Lite, microcontroladores Raspberry Pi Pico W e um eletroímã.

## Partes interessadas

* Laboratório de processo metalúrgicos;
* Inteli

# Análise do Problema

Para melhor entender o contexto do projeto, realizamos uma análise de Oceano Azul para identificar nosso posicionamento em relação ao método tradicional de separação magnético. Buscamos também concorrentes, como o HGMS da empresa Metso, mas concluímos que sua aplicação não servia ao mesmo nicho que nosso projeto.

Ademais, criamos uma matriz de risco sobre o desenvolvimento do projeto, com base em nossas experiências conjuntas de riscos e oportunidades de módulos passados aplicados às possibilidades do bimestre vigente. 

Por fim, a partir da análise das informações citadas acima e dados obtidos do entendimento do design, sintetizamos o canvas de proposta de valor da solução

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

![image](https://user-images.githubusercontent.com/99221221/221012067-e4c738e2-1bcd-433f-8a77-9b477575add9.png)

**Aumentar**
* Precisão da análise
* Custo
* Velocidade
* Tecnologia
* Eficiência

**Diminuir**
* Mantenabilidade
* Robustez

**Criar**
* Parametrização
* Gasto energético

**Elimiar**
* Interveção humana

## Análise financeira

![image](https://user-images.githubusercontent.com/99221221/221013030-38d26f0c-d581-48ee-bd99-0469c0546937.png)

**Aspectos considerados:**
* Custo do Magnetum por ensaio (gasto energético + manutenção): R$ 2,125
* Custo do trabalhador por ensaio tradicional: R$ 7,81

Considerando que uso do tradicional custe e demore mais que do Magnetum e que a máquina fará uma jornada de trabalho de 6 horas todos os dias, enquanto o trabalhador fará uma de 8, estima-se que com 3000 usos, o equivalente a 168 dias, os gastos totais com o trabalhador supere o do Magnetum. 

## Proposta de Valor: Value Proposition Canvas

![image](https://user-images.githubusercontent.com/99221221/221010689-70564924-dd1f-4ee7-84db-0faa57005949.png)

## Personas

![image](https://user-images.githubusercontent.com/99221221/221011051-d283f015-dc3d-49fe-9435-14929ac38111.png)


## Histórias dos usuários (user stories)

**Épico: Como técnico, quero separar o material magnético de uma amostra com alta precisão e de modo automatizado para otimizar meu tempo e a qualidade da operação**
* Como técnico, quero acionar o início do ensaio por meio de um botão, após preparar a amostra nas bandejas, para que ele se realiza sem intervenção
* Como técnico, quero parametrizar as variáveis envolvidas no ensaio, como velocidade de passagem, intensidade magnética e distância, para analisar os resultados de forma precisa em diferentes condições
* Como técnico, quero ser alertado que o ensaio terminou por meio de sinal sonoro para que possa me concentrar em outras tarefas durante a execução do processo
* Como técnico, quero que o ensaio finalize automaticamente quando o ímã não atrair mais quantidade significativa de material magnético
* Como técnico, quero que o braço mecânico passe em cada bandeja para que realize coleta, limpeza e despejo dos materiais.
* Como técnico, quero que o sistema mantenha a distância e intensidade magnéticas constantes para que os resultados sejam precisos e confiáveis

**Épico: Como técnico, quero acessar relatórios precisos e padronizados de cada ensaio para analisar os resultados, filtrar dados e chegar a conclusões empiricamente embasadas.**
* Como técnico, quero ter um histórico das separações magnéticas que fiz para que possa consultar futuramente.
* Como técnico, quero que tenha filtros de busca por data de realização e por material para que consiga consultar com maior facilidade.


# Arquitetura do Sistema

## Módulos do Sistema e Visão Geral (Big Picture)

![image](https://user-images.githubusercontent.com/99221221/221013792-5d18d134-7978-4332-8e0a-9203602521d0.png)

## Descrição dos Subsistemas

### Descrição dos componentes

![image](https://user-images.githubusercontent.com/99221221/221013920-fce75aeb-2683-48bb-841a-5461bb479c9a.png)


## Tecnologias Utilizadas
### Testes de componentes
#### Movimentação do robô

A movimentação do robô foi testada em três etapas. Inicialmente, fizemos uma exploração das funcionalidades do Magician Lite com o auxílio do software de controle Dobot Studio. Nesse momento, testamos as diferentes possibilidades de periféricos, como a garra, a sucção e a caneta, e nos familiarizamos com os limites físicos do robô, no que tange a range of motion. Um produto disso foi o teste de controle fino do robô no modo de desenho, em que experimentamos delinear um vetor de alta complexidade, conforme visto no vídeo abaixo.

[Teste de desenho](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/movimento_robo/desenho.mp4?raw=true)

Na segunda etapa, instalamos a biblioteca Pydobot, que permite a comunicação com o robô diretamente de scripts em Python. Com isso, testamos scripts simples de movimentação sobre as bandejas, com sucesso.

[Movimentação simples](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/movimento_robo/movimento_robo.mp4?raw=true)

Na terceira etapa, criamos um servidor simples em Flask para automatizar uma movimentação específica através de uma interface gráfica web. Para isso, fizemos uma rota GET que, quando requisitada, executava a função de movimentação do robô.

#### Eletroímã na ponte H

O teste de eletroímã também teve três estágios. Primeiro, construímos o hardware e ativamos o ímã diretamente na fonte com 12V. Com esse sucesso, passamos a programar uma função simples de liga e desliga. Iniciamos com métodos de PWM, mas não conseguimos atingir o comportamento esperado. Por isso, resolvemos testar algo mais simples e apenas ligamos os pinos digitalmente, com sinais de HIGH e LOW. Isso funcionou perfeitamente, e pudemos conectar essa funcionalidade ao servidor e ao frontend.

[Ímã ligando e desligando no front](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/eletroima/ima_liga_e_desliga.mp4?raw=true)

Depois, integramos o ímã ao robô fisicamente, utilizando a ponta de sucção. Também programamos um timer no ímã para que ele alterasse o sentido do campo magnético periodicamente, atraindo e soltando o material magnético das bandejas.

[Ímã conectado ao braço](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/integracao/ima_atrai_e_solta.mp4?raw=true)

[Ímã atraindo e soltando](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/integracao/integracao_ima_robo.mp4?raw=true)

Feito isso, tentamos dinamizar a intensidade do eletroímã. Para isso, modificamos o código para contemplar o uso de PWM e convertemos o argumento de voltagem (0-12V) para a escala de duty cycle (0-65535). Isso funcionou quando rodávamos o código do Raspberry diretamente ou enviávamos uma requisição do servidor. Todavia, não tivemos tempo para integrar plenamente com o frontend. Isso será feito na sprint 3.

#### Bomba d'água na ponte H

O teste da bomba d'água teve duas fases. Começamos pelo teste da bomba d'água diretamente na fonte através da ponte H.

[Bomba d'água na fonte](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/bomba_dagua/bomba_dagua.mp4?raw=true)

Depois, fizemos adicionamos funções de ligar e desligar no código do Raspberry Pi, utilizando pinos digitais, já que não seria necessário controlar a intensidade do atuador. Infelizmente, não tivemos tempo de testá-las. Chegamos a codificar o restante da integração com servidor e frontend, porém não pudemos testá-la por problemas de conexão com a internet no final da sprint.

#### Sensor de campo eletromagnético

Um dos diferenciais de nosso projeto é a possibilidade de se estimar o peso da amostra magnética coletada através da variação do campo magnético do ímã. Para tanto, estamos utilizando um sensor de efeito hall KY-024. Assim, nos testes, inicialmente construímos um circuito simples com o sensor e um LED de feedback, de modo que o LED brilhasse quando o sensor captasse campo magnético. 

[Sensor de campo eletromagnético](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/sensor_campo_magnetico/sensor_de_campo_magnetico.mp4?raw=true)

Posteriormente, conectamos essa parte do circuito ao restante do sistema. Resta para a Sprint 3 aprimorar esse módulo, para que ele mostre a leitura no frontend e, para fins de teste e aprendizado, modifique a intensidade do brilho do LED proporcionalmente.

#### Célula de carga e amplificador HX711

A célula de carga converte uma força em um sinal elétrico que pode ser medido. Este sinal irá mudar proporcionalmente à força aplicada. A células de carga é composta por uma barra de metal com extensômetros fixados. Os extensômetros são sensores elétricos que medem força ou tensão em um objeto. Quando uma força externa é aplicada a um objeto, como a barra de metal, ocorre uma deformação em sua forma, o que faz com que a resistência dos extensômetros varie. A mudança na resistência é proporcional à carga aplicada, permitindo-nos calcular o peso dos objetos.
Sabe-se que existem alterações de tensão, todavia, como essas mudanças são muito pequenas, é necessário um amplificador. O amplificador utilizado se chama HX711 e se comunica com o microcontrolador utilizando de uma interfaze de dois fios, "Clock" e "Data". Para realizar o teste foi preciso prender a célula de carga de maneira a criar uma tensão entre as extremidades opostas da barra de metal. 

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/celula_de_carga/c%C3%A9lula_de_carga_entre_placas.png?raw=true)

Após isso, foram feitas as seguintes ligações:

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/celula_de_carga/conexoes_celula_de_carga.png?raw=true)

O teste consistiu em duas etapas: a calibração da célula e a medição de peso de objetos previamente conhecidos. A primeira etapa é crucial para o teste, pois é a partir dela que determinamos o fator de calibração, que pode ser obtido dividindo o valor lido pela célula pelo peso já conhecido. A segunda etapa consistiu na medição real dos objetos, utilizando o fator de calibração obtido na primeira etapa.

[Vídeo do teste realizado](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/testes_de_componentes/celula_de_carga/celula_de_carga.mp4?raw=true)

Isso tudo foi testado em um ESP-32 com C++. Pretendemos adaptar essa funcionalidade para o Raspberry Pi Pico W com Micropython, integrando isso ao resto do sistema, na Sprint 3.

### Relatório de entradas e saídas dos testes

| Componente                             | Entrada                                                       | Saída esperada                                                                   | Resultado do teste                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braço robótico                         | Acionamento do botão de início do ensaio na interface gráfica | Movimentação do robô segundo as coordenadas de posição programadas para o ensaio (quatro pontos sobre cada bandeja: ponto alto inicial, ponto baixo inicial, ponto baixo final e ponto alto final) | Sucesso. Robô se movimentou conforme o esperado.                                                                                                                                                                                                   |
| Eletroímã                              | Acionamento do botão de "ligar" na interface gráfica          | Emissão de campo eletromagnético no ímã, atraindo objetos magnéticos.            | Sucesso. Ao apertar o botão, o ímã atraiu uma moeda de dez centavos.                                                                                                                                                                               |
| Eletroímã                              | Acionamento do botão de "desligar" na interface gráfica       | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados. | Sucesso. Ao apertar o botão, o ímã soltou a moeda e parou de atrair materiais magnéticos.                                                                                                                                                          |
| Sensor de campo eletromagnético        | Aproximação de campo magnético                                | Iluminação do LED de feedback                                                    | Sucesso. Ao aproximar o ímã ligado, o LED acendeu.                                                                                                                                                                                                 |
| Sensor de campo eletromagnético        | Afastamento de campo magnético                                | Apagamento do LED de feedback                                                    | Sucesso. Ao afastar ou desligar o ímã, o LED se apagou.                                                                                                                                                                                            |
| Célula de carga e amplificador         | Adição de massa sobre a placa da célula de carga              | Exibição do peso da massa adicionada no console do microcontrolador              | Sucesso. A adição de um case de fone de ouvido foi reconhecida e corretamente pesada pela célula de carga. A acuracidade foi estimada através da comparação do peso calculado pela célula de carga com o peso calculado por uma balança calibrada. |
| Bomba d'água                           | Conexão da bomba d'água, na ponte H, à fonte em 5V            | Ativação da bomba em um dos sentidos de rotação.                                 | Sucesso. A bomba ativou-se corretamente.                                                                                                                                                                                                           |
| Contagem de ciclos (interface gráfica) | Repetição dos ciclos (passadas) do robô em um mesmo ensaio    | Atualização do número de ciclos (passadas) no frontend.                          | Sucesso. A linha de contagem de ciclos mudou conforme o esperado.                                                                                                                                                                                  |
| Contagem de ciclos (interface gráfica) | Finalização de um ensaio                                      | Reset da contagem de ciclos, voltando ao 0.                                      | Sucesso. Ao terminar um ensaio, assim que o robô parava de se movimentar, o contador voltava a 0.                                                                                                                                                  |

# UX e UI Design

Até o momento (Sprint 2), iniciamos um design de interface gráfica no Figma e implementamos uma versão simplista como demo para os testes de integração.

Como linha geral, priorizamos elementos minimalistas, intuitivos e de fácil entendimento. Seguindo o estilo utilizado até agora nos slides e logotipos, apostamos em uma paleta de cores com alto contraste e foco em tons de roxo. 

A interface do Figma apresenta uma sidebar simples, com tela inicial, histórico de relatórios e perfil. A tela principal, por sua vez, traz um botão de destaque para iniciar um ciclo, assim como campos de preenchimento de mais informações para cada execução. Abaixo, tem-se um atalho para o ensaio mais recente. Já na aba de histórico, ainda não construída no Figma, poder-se-á visualizar ensaios antigos com diversas funcionalidades de filtragem, compilação, exportação e compartilhamento.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/interface_grafica/figma.png?raw=true)

Para a interface de testes, utilizamos um design simples, com um único vetor em tons de verde para decoração na base da página.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/docs_sprint_2/media/interface_grafica/interface_demo.png?raw=true)

# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico


# Teste de Software

## Testes Unitários


## Teste de Usabilidade


# Análise de Dados


# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências

[Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-load-cell-hx711/)
