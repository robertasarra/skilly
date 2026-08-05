# {{PROJETO}}

**Status:** EM DEFINIÇÃO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** o que é o produto, como executar, o que ele
**não** faz.

## O que é

(uma descrição curta e honesta do produto)

## O que este projeto não faz

Delimitar o fora-de-escopo evita que a expectativa cresça sozinha. Liste aqui o que
alguém poderia razoavelmente supor que existe — e não existe.

## Como executar

```
# comandos reais, testados — não aspiracionais
```

## Governança

Este repositório é governado pelo **BEORYS™**. Toda entrega passa pelo gate documental:

```
python scripts/verificar_gate_documental.py --staged
```

RC=0 aprova, RC=1 falta documento obrigatório, RC=2 arquivo `LOCKED` sem ADR, RC=3
política ausente ou inválida. A política normativa está em `BEORYS_GATES.md`.

Ponto de entrada para continuar o trabalho: `ONDE_PARAMOS.md`.
