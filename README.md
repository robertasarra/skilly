# skilly

Skills portáteis e versionadas para agentes de IA. Este repositório é a **fonte única** — o lugar de onde saem as cópias/adapters instalados em projetos, Claude, ChatGPT/Work ou outros runtimes compatíveis.

As integrações de cada plataforma podem variar, mas a fonte metodológica deve permanecer aqui.

## Por que este repositório existe

Uma skill do Claude vive em **dois registros desconectados**, e nenhum deles avisa o
outro quando muda:

| Onde você usa | O que carrega a skill | Como atualizar |
|---|---|---|
| Web, celular, app desktop | skills da conta claude.ai | Configurações → Habilidades → ⋮ → Substituir, enviando um `.zip` |
| Terminal (Claude Code) | `~/.claude/skills/`, **por máquina** | copiar a pasta |
| Sessão na nuvem sobre um repo | `.claude/skills/` commitado no repo | commit |

Atualizar um não atualiza os outros. Sem um lugar único, é questão de tempo até você
editar uma cópia, esquecer a outra, e não saber mais qual está certa — foi exatamente o
que aconteceu em 04/08/2026, quando a versão da conta ficou para trás sem sinal nenhum.

Aqui fica o original. As cópias saem daqui.

## Estrutura

Uma pasta por skill, na raiz:

```
skilly/
├── beorys/
│   ├── SKILL.md
│   └── assets/
└── <proxima-skill>/
    └── SKILL.md
```

O conteúdo de cada pasta é copiável **direto** para `~/.claude/skills/` — sem pasta
intermediária. Se um dia isto virar um marketplace de plugins, basta acrescentar
`.claude-plugin/marketplace.json`; nada muda de lugar.

## Instalar uma skill

**No terminal** — copie a pasta:

```
cp -r beorys ~/.claude/skills/
```

Tem que ficar `~/.claude/skills/beorys/SKILL.md`. Abra uma sessão nova e confira com
`/skills`.

No Windows o destino é `C:\Users\<você>\.claude\skills\`.

**Na conta claude.ai** — o upload é de um `.zip` com a pasta da skill **na raiz**:

```
zip -r beorys.zip beorys
```

claude.ai → Configurações → Habilidades → `+` → Criar habilidade. Para atualizar uma que
já existe, use ⋮ → **Substituir** na skill, não crie outra.

## Antes de subir uma versão

Confira que o que está no `.zip` é o que está aqui. É o passo que faltou em 04/08/2026:

```
sha256sum beorys/assets/verificar_gate_documental.py
unzip -p beorys.zip beorys/assets/verificar_gate_documental.py | sha256sum
```

Os dois hashes têm que bater. Depois de substituir, confira a contagem de arquivos que a
interface mostra — se não mudou, o upload não pegou.

## Skills

| Skill | O que faz |
|---|---|
| [`beorys`](beorys/) | Sistema de continuidade e governança BEORYS™: monta a estrutura de documentos vivos e o gate documental em projetos novos |
| [`adversarial-project-intelligence`](adversarial-project-intelligence/) | Meta-skill portátil para revisão adversarial, disciplina de evidência, separação de autoridade/estado, contradiction checks, execução responsável, persistência e aprendizagem por regressão |


## Regra de upstream

Para skills compartilhadas entre projetos, este repositório é o upstream canônico. Projetos consumidores devem manter apenas:
- adapter específico do projeto;
- referência de versão/commit do upstream;
- fallback local versionado quando necessário para operação offline ou limitação de acesso.

Mudanças universais devem voltar primeiro para este upstream; regras específicas permanecem no adapter do projeto.
