# Titulo: Obesidade
# Alunos: Renan dos Santos Silva, Michelli Patricia Luvison, Davi Rodrigues Chiqueti
# Introdução: A obesidade é um problema de saúde global crescente, com sérias consequências físicas e mentais. Seu aumento constante representa um desafio significativo para os sistemas de saúde e as comunidades em todo o mundo.
# Objetivo da Análise: O objetivo é identificar padrões e tendências que nos ajudem a entender melhor a relação entre esses fatores e a obesidade, visando desenvolver modelos preditivos para uma abordagem mais eficaz na prevenção e tratamento da obesidade.
# Materiais e Métodos: Os dados utilizados nesta análise foram coletados de um conjunto de dados que inclui informações sobre idade, peso, hábitos alimentares, atividade física, consumo de álcool, tabagismo e nível de obesidade. O conjunto de dados foi pré-processado e as variáveis relevantes foram selecionadas para análise.
# Resultados e Discussões: Observamos associações entre idade e peso, além de padrões interessantes nos hábitos alimentares, atividade física, consumo de álcool e tabagismo em relação à obesidade.
# Considerações Finais: Os resultados destacam a complexidade da relação entre os fatores estudados e a obesidade. Eles enfatizam a necessidade de abordagens abrangentes na prevenção e tratamento da obesidade, incluindo intervenções personalizadas e modelos preditivos mais precisos.

########################################################################

# Carregando bibliotecas
library(dplyr)
library(ggplot2)

# (a) Escolher um tema de sua área, ou de sua preferência:
# Carregando conjunto de dados
dados <- read.csv('dataset.csv')

# Normalizando coluna com o nível de obesidade
dados$NObeyesdad[dados$NObeyesdad == "Insufficient_Weight"] <- "Abaixo"
dados$NObeyesdad[dados$NObeyesdad == "Normal_Weight"] <- "Normal"
dados$NObeyesdad[dados$NObeyesdad == "Overweight_Level_I"] <- "Sobrepeso I"
dados$NObeyesdad[dados$NObeyesdad == "Overweight_Level_II"] <- "Sobrepeso II"
dados$NObeyesdad[dados$NObeyesdad == "Obesity_Type_I"] <- "Obesidade I"
dados$NObeyesdad[dados$NObeyesdad == "Obesity_Type_II"] <- "Obesidade II"
dados$NObeyesdad[dados$NObeyesdad == "Obesity_Type_III"] <- "Obesidade III"

# Normalizando coluna da frequência na ingestão de álcool
dados$CALC[dados$CALC == "Always"] <- "Sempre"
dados$CALC[dados$CALC == "Frequently"] <- "Frequentemente"
dados$CALC[dados$CALC == "no"] <- "Não"
dados$CALC[dados$CALC == "Sometimes"] <- "As vezes"

# Normalizando coluna de Fumante
dados$SMOKE[dados$SMOKE == "no"] <- "Não"
dados$SMOKE[dados$SMOKE == "yes"] <- "Sim"

# Normalizando coluna da frequência de Consumo de Alimentos Calóricos
dados$FAVC[dados$FAVC == "no"] <- "Não"
dados$FAVC[dados$FAVC == "yes"] <- "Sim"

########################################################################

# (b) Seleção de Variáveis de Interesse:

# Age (Idade): Variável quantitativa.
# Weight (Peso): Variável quantitativa.
# FAVC (Frequência de Consumo de Alimentos Calóricos): Variável qualitativa. 
# SMOKE (Fumante): Variável qualitativa.
# FAF (Frequência de exercício físico): Variável quantitativa.
# CALC (Frequência na ingestão de álcool): Variável qualitativa.
# NObeyesdad (Nível de Obesidade): Variável qualitativa.

# (c) Definição das Variáveis em Estudo:

# Age (Idade): Variável quantitativa que indica a idade do indivíduo. Importante para entender a relação entre idade e saúde.
# Weight (Peso): Variável quantitativa que indica o peso do indivíduo. Essencial para avaliar a relação com a obesidade.
# FAVC (Frequência de Consumo de Alimentos Calóricos): Variável qualitativa que indica se o indivíduo consome alimentos calóricos com frequência. Ajuda a explorar os hábitos alimentares em relação à obesidade.
# SMOKE (Fumante): Variável qualitativa que indica se o indivíduo é fumante. Investigação da associação entre tabagismo e obesidade.
# FAF (Frequência de exercício físico): Variável quantitativa que registra a frequência de atividade física. Importante para compreender a atividade física em relação à obesidade.
# CALC (Frequência na ingestão de álcool): Variável qualitativa que indica a frequência de consumo de álcool. Exploração dos padrões de consumo de álcool em relação à obesidade.
# NObeyesdad (Nível de Obesidade): Variável qualitativa que indica o nível de obesidade do indivíduo. Essa será nossa variável de interesse para investigar a relação com a idade.

########################################################################

# (d) Tabelas de Frequência:

# Tabela de frequência para a variável FAVC (Frequência de Consumo de Alimentos Calóricos)
tabela_favc <- table(dados$FAVC)
print(tabela_favc)
# Conclusão: A maioria dos indivíduos relatou consumir alimentos calóricos com frequência, enquanto uma minoria significativa afirmou não consumir com tanta frequência.

# Tabela de frequência para a variável SMOKE (Fumante)
tabela_smoke <- table(dados$SMOKE)
print(tabela_smoke)
# Conclusão: A grande maioria dos indivíduos não são fumantes, enquanto apenas um pequeno número relatou ser fumante.

# Tabela de frequência para a variável CALC (Consome álcool)
tabela_calc <- table(dados$CALC)
print(tabela_calc)
# Conclusão: A maioria dos indivíduos consome álcool ocasionalmente, seguido por uma minoria que não consome, e apenas um pequeno número consome frequentemente ou sempre.

# Tabela de frequência para a variável NObeyesdad (Nível de Obesidade)
tabela_obesidade <- table(dados$NObeyesdad)
print(tabela_obesidade)
# Conclusão: Os níveis de obesidade estão distribuídos de maneira relativamente equilibrada entre as categorias.

########################################################################

# (e) Gráficos Adequados:

# Histograma para Age (Idade)
hist_age <- ggplot(data = dados, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = "skyblue", color = "white") +
  labs(title = "Distribuição de Idade", x = "Idade", y = "")

print(hist_age)
# Conclusão:

# Gráfico de Barras para FAVC (Frequência de Consumo de Alimentos Calóricos)
barplot_favc <- ggplot(data = dados, aes(x = FAVC)) +
  geom_bar(fill = "salmon") +
  labs(title = "Frequência de Consumo de Alimentos Calóricos", x = "Consumo de Alimentos Calóricos", y = "")

print(barplot_favc)
# Conclusão:

# Gráfico de Barras para SMOKE (Fumante)
barplot_smoke <- ggplot(data = dados, aes(x = SMOKE)) +
  geom_bar(fill = "skyblue") +
  labs(title = "Hábito de Fumar", x = "Hábito de Fumar", y = "")

print(barplot_smoke)
# Conclusão:

# Gráfico de Dispersão para Age (Idade) vs. Weight (Peso) com pontos coloridos pelo nível de obesidade
scatterplot_age_weight_obesity <- ggplot(data = dados, aes(x = Age, y = Weight, color = NObeyesdad)) +
  geom_point() +
  labs(title = "Relação entre Idade, Peso e Nível de Obesidade", x = "Idade", y = "Peso") +
  scale_color_manual(values = c("Abaixo" = "blue", "Normal" = "green", "Sobrepeso I" = "yellow", 
                                "Sobrepeso II" = "orange", "Obesidade I" = "red", "Obesidade II" = "purple", 
                                "Obesidade III" = "black"))

print(scatterplot_age_weight_obesity)
# Conclusão:

########################################################################

# (f) Medidas de Resumo:

# Para a variável Age (Idade)
resumo_age <- summary(dados$Age)
print(resumo_age)

# Para a variável Weight (Peso)
resumo_weight <- summary(dados$Weight)
print(resumo_weight)

# Para a variável FAF (Frequência de exercício físico)
resumo_faf <- summary(dados$FAF)
print(resumo_faf)

# (g) Relacionamento entre Variáveis:

# 1
# Tabela de frequência cruzada para FAVC (Frequência de Consumo de Alimentos Calóricos) vs. NObeyesdad (Nível de Obesidade)
tabela_favc_obesidade <- table(dados$FAVC, dados$NObeyesdad)
print(tabela_favc_obesidade)

# Gráfico de barras para FAVC (Frequência de Consumo de Alimentos Calóricos) por Nível de Obesidade
barplot_favc_obesidade <- ggplot(data = dados, aes(x = FAVC, fill = NObeyesdad)) +
  geom_bar(position = "dodge") +
  labs(title = "Hábito de Consumo de Alimentos Calóricos por Nível de Obesidade", x = "Frequência de Consumo de Alimentos Calóricos", y = "") +
  scale_fill_manual(values = c("Abaixo" = "blue", "Normal" = "green", "Sobrepeso I" = "yellow", 
                               "Sobrepeso II" = "orange", "Obesidade I" = "red", "Obesidade II" = "purple", 
                               "Obesidade III" = "black"))

print(barplot_favc_obesidade)
# Conclusão:

# 2
# Tabela de frequência cruzada para SMOKE (Fumante) vs. NObeyesdad (Nível de Obesidade)
tabela_smoke_obesity <- table(dados$SMOKE, dados$NObeyesdad)
print(tabela_smoke_obesity)

# Gráfico de barras para SMOKE (Fumante) por Nível de Obesidade
barplot_smoke_obesity <- ggplot(data = dados, aes(x = SMOKE, fill = NObeyesdad)) +
  geom_bar(position = "dodge") +
  labs(title = "Hábito de Fumar por Nível de Obesidade", x = "Fumante", y = "") +
  scale_fill_manual(values = c("Abaixo" = "blue", "Normal" = "green", "Sobrepeso I" = "yellow", 
                               "Sobrepeso II" = "orange", "Obesidade I" = "red", "Obesidade II" = "purple", 
                               "Obesidade III" = "black"))

print(barplot_smoke_obesity)
# Conclusão: https://falandodeobesidade.com/obesidade-e-tabagismo/
# De acordo com o gráfico e a fonte acima, percebe-se que o hábito de fumar pode sim ajudar na prevenção da obesidade, segue alguns pontos a ressaltar
# 1- Supressão do apetite: A nicotina, presente no tabaco, tem propriedades supressoras do apetite, o que pode levar os fumantes a comer menos e, potencialmente, a perder peso.
# 2- Metabolismo aumentado: O tabagismo pode aumentar temporariamente a taxa metabólica basal, o que pode levar a um aumento da queima de calorias e, consequentemente, a uma menor propensão ao ganho de peso.
# 3- Substituição de hábitos: Algumas pessoas podem substituir o hábito de comer por fumar, especialmente em situações de estresse.

# 3
# Tabela de frequência cruzada para CALC (Frequência na ingestão de álcool) vs. NObeyesdad (Nível de Obesidade)
tabela_calc_obesity <- table(dados$CALC, dados$NObeyesdad)
print(tabela_calc_obesity)

# Gráfico de barras para CALC (Frequência na ingestão de álcool) por Nível de Obesidade
barplot_calc_obesity <- ggplot(data = dados, aes(x = CALC, fill = NObeyesdad)) +
  geom_bar(position = "dodge") +
  labs(title = "Frequência na Ingestão de Álcool por Nível de Obesidade", x = "Frequência na Ingestão de Álcool", y = "") +
  scale_fill_manual(values = c("Abaixo" = "blue", "Normal" = "green", "Sobrepeso I" = "yellow", 
                               "Sobrepeso II" = "orange", "Obesidade I" = "red", "Obesidade II" = "purple", 
                               "Obesidade III" = "black"))

print(barplot_calc_obesity)
# Conclusão: