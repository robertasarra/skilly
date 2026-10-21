# MANUAL_DO_DESENVOLVEDOR.md — {{PROJETO}}

**Status:** EM DEFINIÇÃO
**Atualizado em:** {{DATA}}
**Pergunta que este arquivo responde:** como executar, testar, configurar, implantar e
diagnosticar.

> Documento vivo BEORYS™. Comando que não foi executado não entra aqui. Manual
> aspiracional é pior que manual ausente: ele consome tempo antes de falhar.

## Requisitos de ambiente

| Item | Versão mínima | Como conferir |
|---|---|---|
| Python | 3.8 | `python --version` |
| — | — | — |

## Configuração

Variáveis de ambiente — listar **nomes e finalidade**, jamais valores. Nenhum `.env`
versionado.

| Variável | Finalidade | Obrigatória |
|---|---|---|
| — | — | — |

## Executar

```
# comando real
```

## Testar

```
# comando real
```

## Gate documental (obrigatório antes de todo commit)

```
python scripts/verificar_gate_documental.py --staged
```

| RC | Significado | O que fazer |
|---|---|---|
| 0 | Aprovado | seguir para o commit |
| 1 | Documento obrigatório ausente | tocar o documento apontado, com conteúdo real |
| 2 | Arquivo marcado **LOCKED** alterado sem ADR | abrir ADR em `docs/adr/` na mesma entrega |
| 3 | Política ausente ou JSON inválido | estado DESCONHECIDO — **não é aprovação**; corrigir `BEORYS_GATES.md` |

Na CI, comparando contra a base:

```
python scripts/verificar_gate_documental.py --base origin/main
```

## Diagnóstico

(sintomas conhecidos e o que verificar primeiro)
