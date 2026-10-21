# EXECUTION_RUNBOOK.md — {{PROJETO}}

**Status:** EM DEFINIÇÃO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** em que ordem executar (RUN-001…).

> Documento vivo BEORYS™. A ordem é dirigida: nenhum RUN pula o anterior. Cada RUN tem
> validação própria — sem validação, o passo não terminou, só parou.

## Formato do passo

```
### RUN-000 — nome
**Fase:** F00
**Pré-condição:** o que já precisa estar pronto
**Comando:**
    (comando exato, colável)
**Validação:** como saber que deu certo (saída esperada, RC)
**Se falhar:** o que fazer
```

---

### RUN-001 — Validar o gate documental a seco

**Fase:** F00
**Pré-condição:** `BEORYS_GATES.md` e `scripts/verificar_gate_documental.py` na árvore.
**Comando:**

    python scripts/verificar_gate_documental.py --staged

**Validação:** RC=1 nesta etapa (documentos ainda não tocados) — é o esperado.
**Se falhar:** RC=3 significa política não lida. Conferir o marcador
`<!-- BEORYS-GATE-POLICY -->` e a validade do bloco JSON em `BEORYS_GATES.md`.

### RUN-002 — (definir)

**Fase:** —
**Pré-condição:** RUN-001
**Comando:** —
**Validação:** —
**Se falhar:** —
