# AGENTS.md — Contrato de trabalho para IA e desenvolvedores

**Projeto:** {{PROJETO}}
**Status:** ATIVO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** qual é o contrato obrigatório de trabalho.

> Repositório governado pelo **BEORYS™**. Princípio central:
> **conhecimento que existe apenas na conversa não existe oficialmente.**

## Abertura de sessão — obrigatória

Antes de qualquer alteração, leia nesta ordem: `ONDE_PARAMOS.md`, `HANDOFF.md`,
`PENDENCIAS_VIVAS.md`, `BEORYS_GATES.md`. Só então proponha ação.

## Hierarquia da fonte da verdade

```
LOCKED  >  ADR  >  Documentação  >  Código  >  Conversa
```

Fontes em desacordo: a de maior precedência vence e a divergência **vira pendência
registrada** — nunca se resolve só na resposta ao usuário.

## Classificação de afirmações

| Classificação | Significado | Evidência exigida |
|---|---|---|
| CONFIRMADO | li o arquivo / rodei o comando nesta sessão | caminho + trecho ou saída |
| PROVÁVEL | inferido de evidência indireta | origem da inferência declarada |
| HIPÓTESE | não verificado | plano de verificação junto |

Nunca apresente HIPÓTESE com a linguagem de CONFIRMADO. Se algo não existe, diga que não
existe: falha declarada custa uma sessão, falha simulada contamina o registro.

## Regras invioláveis

- **Idioma:** toda saída em `pt-BR`.
- **Segredos:** nenhuma credencial em código, documentação, exemplo ou log. Nenhum
  `.env` versionado.
- **LOCKED:** arquivo marcado como **LOCKED** não se altera nesta sessão — proponha um ADR
  em `docs/adr/` e pare aí.
- **Orchestrator-only:** subagentes propõem, não escrevem em arquivos canônicos nem em
  ADRs. O orquestrador consolida, preservando rastreabilidade de autoria.
- **O gate não basta:** ele prova que os documentos foram tocados **juntos**, não que
  dizem a mesma coisa. RC=0 em todos os gates não autoriza fechar sem revisão de
  coerência semântica.

## Antes de todo commit

```
python scripts/verificar_gate_documental.py --staged
```

Exige RC=0. A política normativa vive em `BEORYS_GATES.md` — fonte única, sem cópia em
outro arquivo.

## Encerramento de sessão — obrigatório

Atualize `WORK_LOG.md` e `ONDE_PARAMOS.md`, registre pendências novas em
`PENDENCIAS_VIVAS.md` e evidências em `EVIDENCE_REGISTER.md`. Sessão interrompida no
meio **ainda exige** encerramento: um fechamento parcial com pendências honestas vale
mais que nenhum.
