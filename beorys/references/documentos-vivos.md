# Documentos vivos e cadeia de rastreabilidade

Cada documento vivo responde a **uma** pergunta. Quando um documento começa a responder
a pergunta de outro, a governança degrada: o leitor não sabe mais onde procurar e as
duas cópias divergem. Antes de escrever em qualquer arquivo, confirme qual pergunta ele
responde.

## Catálogo

| Documento | Pergunta que responde | Atualizar quando |
|---|---|---|
| `README.md` | O que é o produto, como executar, o que ele não faz | Mudar produto, capacidade, implantação, comandos ou próximo passo relevante |
| `AGENTS.md` | Qual é o contrato obrigatório para IA ou dev | Mudar o processo obrigatório de trabalho ou governança |
| `MEMORIAL_DESCRITIVO.md` | Como o sistema é por dentro: módulos, agentes, dados, infra, fronteiras | Mudar arquitetura, módulo, integração ou comportamento estrutural |
| `MANUAL_DO_DESENVOLVEDOR.md` | Como executar, testar, configurar, implantar, diagnosticar | Mudar código, comando, variável, ambiente ou procedimento |
| `MASTER_IMPLEMENTATION_PLAN.md` | O que será construído em cada fase (F00–F13) | Mudar escopo, tecnologia, dependência ou critério de aceite de uma fase |
| `EXECUTION_RUNBOOK.md` | Em que ordem executar (RUN-001–RUN-021) | Mudar sequência, dependência, validação ou próximo RUN |
| `PENDENCIAS_VIVAS.md` | O que falta, quem responde, o que prova que terminou | Toda entrega — inclusive quando nada concluiu mas surgiu bloqueio |
| `EXECUCOES_MANUAIS.md` | O que depende de ação humana (acesso, autorização, domínio, decisão comercial) | Surgir, mudar ou terminar uma ação humana |
| `EVIDENCE_REGISTER.md` | Onde está a prova: teste, ambiente, commit, run, arquivo, SHA-256 | Qualquer teste ou validação produzir evidência nova |
| `REQUIREMENTS_TRACEABILITY.md` | Cada requisito tem implementação, teste e prova? | Qualquer elo da corrente mudar |
| `WORK_LOG.md` | O que foi feito, em ordem cronológica | Cada ciclo material de trabalho |
| `ONDE_PARAMOS.md` | De onde retomar: branch, PR, SHA, testes, bloqueios, próximo passo exato | Fim de toda etapa, teste, decisão, interrupção, commit, PR ou implantação |
| `HANDOFF.md` | Como outra IA continua sem reconstruir contexto | Mudar arquitetura, estado do código, riscos, ambiente ou instrução de continuidade |
| `BEORYS_GATES.md` | Quais documentos são obrigatórios para cada tipo de alteração | Mudar a política documental ou o próprio gate |

**Variação por repositório.** Nem todo projeto governado usa esta nomenclatura. Alguns
usam `PROJECT_CONTEXT.md`, `CURRENT_STATE.md`, `SUMARIO.md` e `TASK_BOARD` para papéis
equivalentes. Na abertura, identifique qual convenção o repositório usa e siga a dele —
não importe nomes de outro projeto, isso cria arquivos órfãos que ninguém lê.

## A cadeia

```
README + MEMORIAL          o que o sistema é
        ↓
MASTER_IMPLEMENTATION_PLAN transforma visão em fases
        ↓
EXECUTION_RUNBOOK          determina a ordem
        ↓
PENDENCIAS + EXECUCOES     o que falta e quem age
        ↓
código, infraestrutura, testes
        ↓
EVIDENCE_REGISTER          prova + SHA-256
        ↓
REQUIREMENTS_TRACEABILITY  requisito ligado à prova
        ↓
ONDE_PARAMOS + HANDOFF     estado e próxima ação
        ↓
BEORYS_GATES               aprova ou bloqueia
```

A cadeia é dirigida: nenhuma etapa pula a anterior. Implementar antes do RUN
correspondente existir, ou fechar pendência sem evidência registrada, quebra a
rastreabilidade mesmo que o código funcione.

## Convenções de identificador

| Prefixo | Significado | Onde vive |
|---|---|---|
| `F00`–`F13` | Fase do plano mestre | `MASTER_IMPLEMENTATION_PLAN.md` |
| `RUN-001`–`RUN-021` | Passo operacional ordenado | `EXECUTION_RUNBOOK.md` |
| `TEC-xxx` | Pendência técnica | `PENDENCIAS_VIVAS.md` |
| `MAN-xxx` | Pendência que depende de ação humana | `PENDENCIAS_VIVAS.md` + `EXECUCOES_MANUAIS.md` |

Cite sempre pelo identificador, nunca por descrição solta. "O problema do banco" não
rastreia; `TEC-021` rastreia.

## Matriz de rastreabilidade

Cada linha liga a corrente inteira:

```
requisito → fase → pendência → código/infra → teste → evidência → rollback → estado
```

Uma linha com qualquer coluna vazia é um requisito sem prova. Ao fechar uma fase,
percorra a matriz coluna a coluna em vez de confiar na memória da sessão — é justamente
onde o estado real e o estado declarado costumam divergir.

## Evidência

Evidência é referência verificável, não afirmação. Registre: o teste executado, o
ambiente, o commit ou run, o arquivo de saída e o **SHA-256** do artefato. Sem hash, a
evidência não prova qual versão foi validada.
