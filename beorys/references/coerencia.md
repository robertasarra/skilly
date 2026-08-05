# Coerência semântica entre documentos

O gate documental verifica **existência e atualização conjunta**: se você mexeu em
infraestrutura, ele exige que o memorial e a matriz tenham sido tocados. O que ele não
consegue fazer é ler duas frases em arquivos diferentes e perceber que elas se
contradizem.

Esse é o ponto cego estrutural da governança automatizada. Um repositório pode passar em
todos os gates com RC=0 e ainda assim afirmar duas coisas incompatíveis sobre si mesmo.
A verificação de coerência é humana e de IA — não há script que a substitua — e precisa
acontecer **antes de todo fechamento**.

## Padrões de incoerência

Estes são os quatro que reaparecem. Procure por eles nominalmente:

**1. Tecnologia substituída que sobrevive em cópia.** Uma migração é decidida e aplicada
no corpo do documento, mas a introdução, o resumo ou uma pendência antiga continuam
citando a tecnologia anterior. Exemplo real: o topo do README menciona backend no Render
enquanto o próprio README, adiante, estabelece AWS ECS Fargate — e `TEC-012` ainda
condiciona o piloto ao Render. Quem lê os primeiros parágrafos sai com a arquitetura
errada.

**2. Pendência fechada em um documento e aberta em outro.** Uma PR é mesclada e
registrada como concluída no work log ou em ONDE_PARAMOS, mas a pendência
correspondente continua "aguardando" em `EXECUCOES_MANUAIS.md`. Exemplo real: `MAN-001`
aguardando com a PR #8 já mesclada. O efeito prático é a próxima sessão executar
trabalho já feito.

**3. Data congelada.** Documentos que carregam data de atualização ficam para trás em um
ou dois dias e passam a sugerir um estado que já não vale. Confira as datas contra o dia
corrente da sessão, não contra a última que você leu.

**4. Estado otimista ou pessimista na matriz.** Controles concluídos ainda classificados
como "em execução" ou "planejados nesta entrega" — ou o inverso, controles marcados
concluídos sem evidência correspondente no registro. A matriz é o último lugar onde
alguém olha e o primeiro que desatualiza.

## Procedimento

Antes de preparar o commit de fechamento:

```
( ) Tecnologia/infra citada é a mesma em README, MEMORIAL e PENDENCIAS?
( ) Toda pendência marcada concluída tem evidência em EVIDENCE_REGISTER?
( ) Toda pendência aberta ainda faz sentido diante do que foi entregue?
( ) Datas conferem com o dia corrente?
( ) Estados na matriz batem com o registro de evidências?
( ) ONDE_PARAMOS e HANDOFF contam a mesma história?
( ) Nenhuma decisão revertida sobreviveu em documento não tocado?
```

Cada divergência encontrada vira pendência com identificador — não conserto silencioso.
Corrigir sem registrar apaga o sinal de que a governança tem um vazamento naquele ponto,
e o mesmo vazamento volta na entrega seguinte.

## Como reportar

```
INCOERÊNCIAS ENCONTRADAS
<arquivo>:<seção>  afirma  <A>
<arquivo>:<seção>  afirma  <B>
Fonte vencedora:   <pela hierarquia LOCKED > ADR > Doc > Código>
Ação:              <correção proposta>  |  Pendência: <TEC/MAN-xxx>
```
