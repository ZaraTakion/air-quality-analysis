# Conclusão e próximos passos

## Síntese baseada nos cálculos existentes

A etapa 4 investiga `Pollution_Index` a partir de temperatura, umidade, velocidade do vento e mês. O OLS ajustado à amostra completa tem R² de 0,002; os coeficientes meteorológicos registrados não são estatisticamente significativos a 5%. No teste aleatório da Random Forest, com 20% dos dados reservados, o R² é −0,082 e o RMSE é 16,519. Portanto, os resultados disponíveis não demonstram associação meteorológica confiável nem capacidade preditiva superior ao baseline da média.

O R² médio de 0,974 do notebook 06 pertence a outro modelo que recebe como preditores os seis poluentes usados para formar o próprio alvo. É vazamento de alvo, não validação independente, e não deve ser usado para afirmar que a Random Forest tem alto poder preditivo. A [documentação da modelagem](Modelagem.md) detalha a diferença.

## Limitações importantes

- `Pollution_Index` é uma média aritmética simples dos seis campos de poluentes, e não um índice oficial. O dicionário atribui unidades distintas a esses campos; a combinação precisa ser justificada ou redefinida antes de interpretação física ou sanitária.
- Os dados processados são de 2023; não permitem descrever tendência de longo prazo.
- O modelo da etapa 4 não controla cidade/país, e sua divisão aleatória não avalia transferência para novos locais ou períodos.
- Os resultados são observacionais e não estabelecem causalidade.

## Próximos passos recomendados

1. Verificar a fonte e as unidades dos poluentes e definir um alvo comparável, documentado e sem ambiguidade.
2. Reexecutar a validação com baseline explícito e separação por cidade ou período, de acordo com a pergunta pretendida.
3. Manter fora de `X` qualquer variável que componha matematicamente o alvo; tratar o experimento do notebook 06 como demonstração de vazamento, não como resultado de performance.
4. Só então comparar modelos e relatar métricas de teste, incerteza e limitações.

## Conclusão

O repositório contém um fluxo exploratório e um dashboard, mas os modelos atuais não comprovam que temperatura, umidade, vento ou sazonalidade expliquem ou prevejam o índice composto. A apresentação profissional dos resultados deve destacar essa incerteza e evitar conclusões causais ou de desempenho que os cálculos não sustentam.
