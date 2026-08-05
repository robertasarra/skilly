# REQUIREMENTS_TRACEABILITY.md — {{PROJETO}}

**Status:** ATIVO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** cada requisito tem implementação, teste e prova?

> Documento vivo BEORYS™. Uma linha com qualquer coluna vazia é um requisito **sem
> prova**. Ao fechar uma fase, percorra a matriz coluna a coluna — é exatamente onde o
> estado real e o estado declarado costumam divergir.

## A corrente

```
requisito → fase → pendência → código/infra → teste → evidência → rollback → estado
```

## Matriz

| Requisito | Fase | Pendência | Código / Infra | Teste | Evidência | Rollback | Estado |
|---|---|---|---|---|---|---|---|
| RF-001 | F00 | TEC-002 | — | — | — | — | ABERTO |

## Legenda de estado

`ABERTO` sem implementação · `EM CURSO` implementado, sem prova · `PROVADO` corrente
completa · `REGREDIDO` já esteve provado e quebrou.
