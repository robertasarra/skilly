# EVIDENCE_REGISTER.md — {{PROJETO}}

**Status:** ATIVO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** onde está a prova.

> Documento vivo BEORYS™. Evidência é **referência verificável**, não afirmação. Sem
> SHA-256 não se sabe qual versão foi validada — e uma evidência que não identifica a
> versão não prova nada.

Como obter o hash:

    # Windows
    certutil -hashfile <arquivo> SHA256
    # Linux / Mac
    shasum -a 256 <arquivo>

## Registro

| ID | O que foi validado | Comando / teste | Ambiente | Commit | Saída | SHA-256 do artefato | Data |
|---|---|---|---|---|---|---|---|
| EV-001 | Gate documental — RC=1 (documento ausente) | `python scripts/verificar_gate_documental.py --staged` | local | — | — | — | — |
| EV-002 | Gate documental — RC=0 (aprovado) | idem | local | — | — | — | — |
| EV-003 | Gate documental — RC=2 (LOCKED sem ADR) | idem | local | — | — | — | — |
| EV-004 | Gate documental — RC=3 (política ausente) | idem | local | — | — | — | — |

As quatro linhas acima são o critério de aceite da fase F00 e ainda **não** foram
preenchidas. Preencher exige rodar os quatro cenários de fato — nunca transcrever de
memória.
