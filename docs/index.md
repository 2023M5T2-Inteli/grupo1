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
  - [Análise da área de atuação](#análise-da-área-de-atuação)
  - [Análise do cenário: Matriz SWOT](#análise-do-cenário-matriz-swot)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard](#wireframe--storyboard)
  - [Design de Interface - Guia de Estilos](#design-de-interface---guia-de-estilos)
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

## Análise da área de atuação

*Descrição_da_análise_da_área_de_atuação*

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
* Manteabilidade
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


# Requisitos do Sistema

*Descrição_dos_requisitos*

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

### Requisitos de software


## Tecnologias Utilizadas


# UX e UI Design

## Wireframe + Storyboard

## Design de Interface - Guia de Estilos


# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico


# Teste de Software

## Testes Unitários

### Célula de carga e amplificador HX711

**Célula de carga**

A célula de carga converte uma força em um sinal elétrico que pode ser medido. Este sinal irá muda porporcionalmente à força aplicada. A células de carga é composta por uma barra de metal com extensômetros fixados. Os extensômetros são sensores elétricos que medem força ou tensão em um objeto. Quando uma força externa é aplicada a um objeto, como a barra de metal, ocorre uma deformação em sua forma, o que faz com que a resistência dos extensômetros varie. A mudança na resistência é proporcional à carga aplicada, permitindo-nos calcular o peso dos objetos.
Sabe-se que existem alterações de tensão, todavia, como essas mudanças são muito pequenas é necessário um amplificador. O amplificador utilizado se chama HX711 e se comunica com o microcontrolador utilizando de uma interfaze de dois fio, "Clock" e "Data". Para realizar o teste foi preciso prender à célula de carga de maneira a criar uma tensão entre as extremidades opostas da barra de metal. 

![image](https://user-images.githubusercontent.com/99221221/221018613-c6259f9e-ffcd-4f65-9466-c43a668d1b19.png)
*Fonte: Autoria Própria*

Após isso foram feitas as seguintes ligações:
![image](https://user-images.githubusercontent.com/99221221/221019861-66465ce6-810e-44d8-8232-191ae4f89dd6.png)

O teste consistiu em duas etapas: a calibração da célula e a medição de peso de objetos previamente conhecidos. A primeira etapa é crucial para o teste, pois é a partir dela que determinamos o fator de calibração, que pode ser obtido dividindo o valor lido pela célula pelo peso já conhecido. A segunda etapa consistiu na medição real dos objetos, utilizando o fator de calibração obtido na primeira etapa.

[Vídeo do teste realizado](https://drive.google.com/file/d/1GvVsDhN7IshUwO-Z0ahV_5d9YwZygBXT/view?usp=sharing)


## Teste de Usabilidade


# Análise de Dados


# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências

[Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-load-cell-hx711/)
