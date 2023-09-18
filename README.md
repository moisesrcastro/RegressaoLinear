# Regressão Múltipla usando Matrizes

A regressão múltipla é uma técnica estatística utilizada para entender a relação entre uma variável dependente (Y) e duas ou mais variáveis independentes (X₁, X₂, ... Xₙ).

## Passo a Passo:

### Formulação do Modelo:

O modelo de regressão múltipla é dado por:

Y = &beta;₀ + &beta;₁X₁ + &beta;a₂X₂ + ... + &beta;ₙXₙ + &epsilon; 

Onde:
- \(Y\) é a variável dependente.
- \(&beta;₀, &beta;₁, &beta;₂, ..., &beta;ₙ) são os coeficientes a serem estimados.
- \(X₁, X₂, ..., Xₙ\) são as variáveis independentes.
- \(&epsilon;) é o termo de erro.

### Preparação dos Dados:

Organize os dados em matrizes. As variáveis independentes (\(X\)) são colocadas em uma matriz onde cada coluna representa uma variável e cada linha uma observação. A variável dependente (\(Y\)) é organizada em um vetor.

Exemplo:

X = | X₁₁  X₂₁  ...  Xₙ₁ |
| X₁₂  X₂₂  ...  Xₙ₂ |
| ...   ...  ...  ...  |
| X₁ₘ  X₂ₘ  ...  Xₙₘ |

Y = |Y₁|
    |Y₂|
    |...|
    |Yₘ|

### Adição do Termo de Intercepto:

Para levar em conta o intercepto, uma coluna de uns é adicionada à matriz de variáveis independentes.

X = |1 X₁₁ X₂₁ ... Xₙ₁|
    |1 X₁₂ X₂₂ ... Xₙ₂ |
    |... ... ... ... |
    |1 X₁ₘ X₂ₘ ... Xₙₘ |

### Estimação dos Coeficientes:

Os coeficientes podem ser estimados usando a fórmula:

&beta; = (X^T X)^{-1} X^{T} Y

### Previsões:

Com os coeficientes estimados, podemos fazer previsões para novos conjuntos de variáveis independentes usando a fórmula:

 Y_predito= X_predito * &beta;

### Interpretação dos Coeficientes:

Cada \(&beta;ᵢ\) representa o efeito de uma variável independente \(Xᵢ\) na variável dependente \(Y\), mantendo todas as outras variáveis constantes.

### Avaliação do Modelo:

É importante avaliar o desempenho do modelo utilizando métricas como o erro quadrático médio (MSE), coeficiente de determinação (\(R²\)) e outros indicadores relevantes.

