# BEORYS_GATES.md — Gate Documental

**Status:** ATIVO
**Versão:** 1.0
**ADR:** ADR-059
**Consumido por:** `scripts/verificar_gate_documental.py`

## O que este gate faz

Para cada **tipo de alteração** detectado no conjunto de arquivos modificados, exige que
um conjunto de documentos vivos tenha sido tocado na mesma entrega. Impede que código
avance deixando a documentação para depois — "depois" é onde o drift nasce.

## O que este gate não faz

Ele prova que os documentos foram atualizados **juntos**. Não prova que dizem a **mesma
coisa**. Dois documentos podem passar no gate e se contradizer. A revisão de coerência
semântica continua sendo obrigatória e humana, antes de todo fechamento.

## Fonte única

A política abaixo é normativa e é lida diretamente pelo script. Não existe cópia em
outro arquivo — duplicar esta tabela criaria exatamente o padrão de incoerência que o
BEORYS™ combate. Para mudar a política, edite este bloco e registre um ADR.

<!-- BEORYS-GATE-POLICY -->
```json
{
  "versao": "1.1",
  "sempre_exigidos": [
    "WORK_LOG.md",
    "ONDE_PARAMOS.md"
  ],
  "bloqueio_locked": {
    "ativo": true,
    "marcador": "Status: LOCKED",
    "exige_adr_em": "docs/adr/ADR-*.md",
    "descricao": "Arquivo LOCKED alterado sem ADR na mesma entrega bloqueia a entrega."
  },
  "tipos": [
    {
      "id": "infraestrutura",
      "descricao": "Terraform, containers, pipelines, rede, provedores de nuvem",
      "padroes": [
        "infra/**",
        "terraform/**",
        "*.tf",
        "*.tfvars",
        "Dockerfile*",
        "docker-compose*.yml",
        ".github/workflows/**"
      ],
      "exige": [
        "MEMORIAL_DESCRITIVO.md",
        "MASTER_IMPLEMENTATION_PLAN.md",
        "REQUIREMENTS_TRACEABILITY.md",
        "EVIDENCE_REGISTER.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "schema_dados",
      "descricao": "Migrations, DDL, modelos de persistencia",
      "padroes": [
        "migrations/**",
        "drizzle/**",
        "*.sql",
        "**/schema.ts",
        "**/schema.py"
      ],
      "exige": [
        "MEMORIAL_DESCRITIVO.md",
        "REQUIREMENTS_TRACEABILITY.md",
        "EVIDENCE_REGISTER.md",
        "PENDENCIAS_VIVAS.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "codigo_aplicacao",
      "descricao": "Codigo de aplicacao backend ou frontend",
      "padroes": [
        "src/**",
        "app/**",
        "server/**",
        "client/**",
        "lib/**"
      ],
      "exige": [
        "REQUIREMENTS_TRACEABILITY.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "dependencias_ambiente",
      "descricao": "Dependencias, variaveis de ambiente, comandos de execucao",
      "padroes": [
        "package.json",
        "package-lock.json",
        "requirements.txt",
        "pyproject.toml",
        ".env.example",
        "Makefile"
      ],
      "exige": [
        "MANUAL_DO_DESENVOLVEDOR.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "testes",
      "descricao": "Suites de teste e validacao automatizada",
      "padroes": [
        "tests/**",
        "test/**",
        "**/*_test.py",
        "**/*.test.ts",
        "**/*.spec.ts"
      ],
      "exige": [
        "EVIDENCE_REGISTER.md",
        "REQUIREMENTS_TRACEABILITY.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "sequencia_operacional",
      "descricao": "Alteracao na ordem ou dependencia dos RUN",
      "padroes": [
        "EXECUTION_RUNBOOK.md",
        "docs/EXECUTION_RUNBOOK.md"
      ],
      "exige": [
        "MASTER_IMPLEMENTATION_PLAN.md",
        "ONDE_PARAMOS.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "escopo_fases",
      "descricao": "Alteracao de escopo, tecnologia ou criterio de aceite de fase",
      "padroes": [
        "MASTER_IMPLEMENTATION_PLAN.md",
        "docs/MASTER_IMPLEMENTATION_PLAN.md"
      ],
      "exige": [
        "EXECUTION_RUNBOOK.md",
        "REQUIREMENTS_TRACEABILITY.md",
        "PENDENCIAS_VIVAS.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "pendencias",
      "descricao": "Abertura, alteracao ou fechamento de pendencia",
      "padroes": [
        "PENDENCIAS_VIVAS.md",
        "docs/PENDENCIAS_VIVAS.md"
      ],
      "exige": [
        "EVIDENCE_REGISTER.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "acao_humana",
      "descricao": "Pendencia que depende de acesso, autorizacao ou decisao comercial",
      "padroes": [
        "EXECUCOES_MANUAIS.md",
        "docs/EXECUCOES_MANUAIS.md"
      ],
      "exige": [
        "PENDENCIAS_VIVAS.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "arquitetura",
      "descricao": "Modulos, agentes, integracoes, fronteiras do sistema",
      "padroes": [
        "MEMORIAL_DESCRITIVO.md",
        "docs/MEMORIAL_DESCRITIVO.md"
      ],
      "exige": [
        "README.md",
        "REQUIREMENTS_TRACEABILITY.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "governanca",
      "descricao": "Contrato de trabalho de IA, politica de gates, regras LOCKED",
      "padroes": [
        "AGENTS.md",
        "CLAUDE.md",
        "BEORYS_GATES.md",
        ".claude/**"
      ],
      "exige": [
        "docs/adr/",
        "README.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "seguranca",
      "descricao": "Politica de seguranca, LGPD, tratamento de credenciais",
      "padroes": [
        "SECURITY.md",
        "docs/LGPD*.md",
        "docs/SEGURANCA*.md"
      ],
      "exige": [
        "docs/adr/",
        "MEMORIAL_DESCRITIVO.md"
      ],
      "severidade": "bloqueia"
    },
    {
      "id": "produto",
      "descricao": "Finalidade, funcionalidades declaradas, limitacoes, situacao comercial",
      "padroes": [
        "README.md"
      ],
      "exige": [],
      "severidade": "avisa"
    }
  ],
  "aliases": {
    "ONDE_PARAMOS.md": [
      "CURRENT_STATE.md",
      "STATUS.md"
    ],
    "WORK_LOG.md": [
      "DIARIO.md",
      "CHANGELOG.md"
    ],
    "MEMORIAL_DESCRITIVO.md": [
      "PROJECT_CONTEXT.md",
      "ARCHITECTURE.md"
    ],
    "MASTER_IMPLEMENTATION_PLAN.md": [
      "PLANO_MESTRE.md",
      "ROADMAP.md"
    ],
    "EXECUTION_RUNBOOK.md": [
      "RUNBOOK.md"
    ],
    "PENDENCIAS_VIVAS.md": [
      "PENDENCIAS.md",
      "TASK_BOARD.md"
    ],
    "REQUIREMENTS_TRACEABILITY.md": [
      "MATRIZ_RASTREABILIDADE.md",
      "SUMARIO.md"
    ],
    "EVIDENCE_REGISTER.md": [
      "EVIDENCIAS.md"
    ],
    "MANUAL_DO_DESENVOLVEDOR.md": [
      "CONTRIBUTING.md",
      "DEVELOPMENT.md"
    ],
    "EXECUCOES_MANUAIS.md": [
      "ACOES_MANUAIS.md"
    ],
    "AGENTS.md": [
      "CLAUDE.md"
    ]
  }
}
```

## Códigos de retorno

| RC | Significado |
|---|---|
| `0` | Todos os documentos exigidos foram tocados |
| `1` | Documento obrigatório ausente na entrega |
| `2` | Arquivo `LOCKED` alterado sem ADR correspondente |
| `3` | Erro de política ou de execução (repositório, JSON inválido) |

`RC=3` não é aprovação disfarçada: significa que o estado do gate é **desconhecido**.

## Uso

```
python scripts/verificar_gate_documental.py --staged
python scripts/verificar_gate_documental.py --base origin/main
python scripts/verificar_gate_documental.py --staged --json
```

## Manutenção

Um padrão que nunca dispara é pior que nenhum padrão: cria a sensação de cobertura sem
cobertura. Ao revisar a política, confira quais `tipos` dispararam nas últimas entregas e
questione os que ficaram permanentemente silenciosos — ou o padrão está errado, ou aquela
área do repositório não está sendo tocada por ninguém.
