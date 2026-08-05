# skilly

Skills do Claude, versionadas. Este repositório é a **fonte única** — o lugar de onde
saem todas as cópias instaladas.

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

## Verificação automática

Todo PR roda `scripts/validar_skills.py`, que confere em cada skill o que o claude.ai
só diria no momento do upload: `SKILL.md` presente, frontmatter fechado, `name` em
minúsculas sem palavra reservada e batendo com o nome da pasta, `description` presente e
dentro de 1024 caracteres. Skill reprovada aqui seria recusada lá.

O mesmo workflow executa qualquer `testar_*.py` que uma skill traga. A `beorys` traz os
7 casos da detecção do marcador de travamento — sem isso, uma regressão nela só
apareceria no projeto de quem instalasse.

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
