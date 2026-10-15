# Catálogo — 50 skills do Claude (instaladas)

Origem de cada skill: repositório, caminho e commit exatos copiados em 2026-10-15.
Lista de referência: `segundo-cerebro/03_REFERENCIAS/SKILLS_CLAUDE_50.md`.

Revisão feita antes de copiar: busca por comandos destrutivos, download+execução,
leitura de credenciais, instruções ocultas ao modelo e chaves reais. Nenhum achado
bloqueante (os casos encontrados eram exemplos de teste ou documentação). Algumas
skills chamam serviços externos **somente** se a usuária configurar a chave
(HeyGen, OpenRouter, NCBI/OpenAlex, Google Custom Search).

Para atualizar uma skill: clonar o repositório de origem, copiar o mesmo caminho
por cima da pasta e registrar o novo commit nesta tabela.

| Item | Skill | Repositório | Caminho | Commit |
|---|---|---|---|---|
| 6 | `frontend-design` | anthropics/skills | `skills/frontend-design` | `dbd4588f9e10` |
| 12 | `webapp-testing` | anthropics/skills | `skills/webapp-testing` | `dbd4588f9e10` |
| 18 | `brainstorming` | obra/superpowers | `skills/brainstorming` | `bb92a7774141` |
| 18 | `dispatching-parallel-agents` | obra/superpowers | `skills/dispatching-parallel-agents` | `bb92a7774141` |
| 18 | `executing-plans` | obra/superpowers | `skills/executing-plans` | `bb92a7774141` |
| 18 | `finishing-a-development-branch` | obra/superpowers | `skills/finishing-a-development-branch` | `bb92a7774141` |
| 18 | `receiving-code-review` | obra/superpowers | `skills/receiving-code-review` | `bb92a7774141` |
| 18 | `requesting-code-review` | obra/superpowers | `skills/requesting-code-review` | `bb92a7774141` |
| 18 | `subagent-driven-development` | obra/superpowers | `skills/subagent-driven-development` | `bb92a7774141` |
| 18 | `systematic-debugging` | obra/superpowers | `skills/systematic-debugging` | `bb92a7774141` |
| 18 | `test-driven-development` | obra/superpowers | `skills/test-driven-development` | `bb92a7774141` |
| 18 | `using-git-worktrees` | obra/superpowers | `skills/using-git-worktrees` | `bb92a7774141` |
| 18 | `verification-before-completion` | obra/superpowers | `skills/verification-before-completion` | `bb92a7774141` |
| 18 | `writing-plans` | obra/superpowers | `skills/writing-plans` | `bb92a7774141` |
| 18 | `writing-skills` | obra/superpowers | `skills/writing-skills` | `bb92a7774141` |
| 20 | `skill-builder` | yusufkaraaslan/Skill_Seekers | `skills/skill-seekers` | `5b5d8dfca263` |
| 22 | `shadcn` | shadcn-ui/ui | `skills/shadcn` | `c2477f311c19` |
| 23 | `frontend-slides` | zarazhangrui/frontend-slides | `plugins/frontend-slides/skills/frontend-slides` | `9906a34d640d` |
| 24 | `d3-viz` | chrisvoncsefalvay/claude-d3js-skill | `.` | `e198c87d03f1` |
| 25 | `web-asset-generator` | alonw0/web-asset-generator | `skills/web-asset-generator` | `c6d56dc54ab8` |
| 26 | `remotion-best-practices` | remotion-dev/skills | `skills/remotion-best-practices` | `7ba4dcf8ebe1` |
| 27 | `heygen-avatar` | heygen-com/skills | `heygen-avatar` | `1bd5e4d33a02` |
| 28 | `typography` | glebis/claude-skills | `typography` | `3b8826108af8` |
| 30 | `playwright-skill` | lackeyjb/playwright-skill | `skills/playwright-skill` | `dd47a6a023e2` |
| 31 | `csv-data-summarizer` | coffeefuelbump/csv-data-summarizer-claude-skill | `.` | `9b3affd270f8` |
| 32 | `file-organizer` | ComposioHQ/awesome-claude-skills | `file-organizer` | `be2a406907db` |
| 33 | `notebooklm` | PleasePrompto/notebooklm-skill | `.` | `c80722d3f27d` |
| 34 | `notion-knowledge-capture` | makenotion/claude-code-notion-plugin | `skills/notion/knowledge-capture` | `9847f2aa1a15` |
| 34 | `notion-meeting-intelligence` | makenotion/claude-code-notion-plugin | `skills/notion/meeting-intelligence` | `9847f2aa1a15` |
| 34 | `notion-research-documentation` | makenotion/claude-code-notion-plugin | `skills/notion/research-documentation` | `9847f2aa1a15` |
| 34 | `notion-spec-to-implementation` | makenotion/claude-code-notion-plugin | `skills/notion/spec-to-implementation` | `9847f2aa1a15` |
| 35 | `git-pushing` | mhattingpete/claude-skills-marketplace | `engineering-workflow-plugin/skills/git-pushing` | `b5b34bcf4c92` |
| 36 | `bug-from-user` | rockscy/solo-skills | `skills/bug-from-user` | `80ec4cfc2ff8` |
| 36 | `changelog-from-commits` | rockscy/solo-skills | `skills/changelog-from-commits` | `80ec4cfc2ff8` |
| 36 | `email-customer` | rockscy/solo-skills | `skills/email-customer` | `80ec4cfc2ff8` |
| 36 | `launch-tweet` | rockscy/solo-skills | `skills/launch-tweet` | `80ec4cfc2ff8` |
| 36 | `postmortem-solo` | rockscy/solo-skills | `skills/postmortem-solo` | `80ec4cfc2ff8` |
| 36 | `ship-decision` | rockscy/solo-skills | `skills/ship-decision` | `80ec4cfc2ff8` |
| 36 | `standup-solo` | rockscy/solo-skills | `skills/standup-solo` | `80ec4cfc2ff8` |
| 37 | `automation-advisor` | glebis/claude-skills | `automation-advisor` | `3b8826108af8` |
| 38 | `elimination-research` | glebis/claude-skills | `elimination-research` | `3b8826108af8` |
| 39 | `article-extractor` | michalparkola/tapestry-skills-for-claude-code | `article-extractor` | `80e1dc56df74` |
| 41 | `the-goal` | glebis/claude-skills | `the-goal` | `3b8826108af8` |
| 42 | `pre-session-portrait` | glebis/claude-skills | `pre-session-portrait` | `3b8826108af8` |
| 43 | `aws-cdk-development` | zxkane/aws-skills | `plugins/aws-iac/skills/aws-cdk-development` | `68530c6f296c` |
| 44 | `differential-review` | trailofbits/skills | `plugins/differential-review/skills/differential-review` | `e1f86a390d4c` |
| 44 | `sharp-edges` | trailofbits/skills | `plugins/sharp-edges/skills/sharp-edges` | `e1f86a390d4c` |
| 44 | `supply-chain-risk-auditor` | trailofbits/skills | `plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor` | `e1f86a390d4c` |
| 45 | `VibeSec-Skill` | BehiSecc/VibeSec-Skill | `.` | `0590993b35ad` |
| 46 | `eas-app-stores` | expo/skills | `plugins/expo/skills/eas-app-stores` | `d4f484024fec` |
| 46 | `eas-hosting` | expo/skills | `plugins/expo/skills/eas-hosting` | `d4f484024fec` |
| 46 | `eas-observe` | expo/skills | `plugins/expo/skills/eas-observe` | `d4f484024fec` |
| 46 | `eas-simulator` | expo/skills | `plugins/expo/skills/eas-simulator` | `d4f484024fec` |
| 46 | `eas-update` | expo/skills | `plugins/expo/skills/eas-update` | `d4f484024fec` |
| 46 | `eas-update-insights` | expo/skills | `plugins/expo/skills/eas-update-insights` | `d4f484024fec` |
| 46 | `eas-workflows` | expo/skills | `plugins/expo/skills/eas-workflows` | `d4f484024fec` |
| 46 | `expo-animation` | expo/skills | `plugins/expo/skills/expo-animation` | `d4f484024fec` |
| 46 | `expo-app-clip` | expo/skills | `plugins/expo/skills/expo-app-clip` | `d4f484024fec` |
| 46 | `expo-brownfield` | expo/skills | `plugins/expo/skills/expo-brownfield` | `d4f484024fec` |
| 46 | `expo-data-fetching` | expo/skills | `plugins/expo/skills/expo-data-fetching` | `d4f484024fec` |
| 46 | `expo-design-system` | expo/skills | `plugins/expo/skills/expo-design-system` | `d4f484024fec` |
| 46 | `expo-dev-client` | expo/skills | `plugins/expo/skills/expo-dev-client` | `d4f484024fec` |
| 46 | `expo-dom` | expo/skills | `plugins/expo/skills/expo-dom` | `d4f484024fec` |
| 46 | `expo-examples` | expo/skills | `plugins/expo/skills/expo-examples` | `d4f484024fec` |
| 46 | `expo-module` | expo/skills | `plugins/expo/skills/expo-module` | `d4f484024fec` |
| 46 | `expo-native-ui` | expo/skills | `plugins/expo/skills/expo-native-ui` | `d4f484024fec` |
| 46 | `expo-overview` | expo/skills | `plugins/expo/skills/expo-overview` | `d4f484024fec` |
| 46 | `expo-project-structure` | expo/skills | `plugins/expo/skills/expo-project-structure` | `d4f484024fec` |
| 46 | `expo-router` | expo/skills | `plugins/expo/skills/expo-router` | `d4f484024fec` |
| 46 | `expo-skill-feedback` | expo/skills | `plugins/expo/skills/expo-skill-feedback` | `d4f484024fec` |
| 46 | `expo-ui` | expo/skills | `plugins/expo/skills/expo-ui` | `d4f484024fec` |
| 46 | `expo-upgrade` | expo/skills | `plugins/expo/skills/expo-upgrade` | `d4f484024fec` |
| 46 | `expo-web-to-native` | expo/skills | `plugins/expo/skills/expo-web-to-native` | `d4f484024fec` |
| 47 | `ios-simulator-skill` | conorluddy/ios-simulator-skill | `ios-simulator-skill/skills/ios-simulator-skill` | `c535422ab4ee` |
| 48 | `citation-management` | K-Dense-AI/claude-scientific-skills | `skills/citation-management` | `a1043ef544e3` |
| 48 | `literature-review` | K-Dense-AI/claude-scientific-skills | `skills/literature-review` | `a1043ef544e3` |
| 48 | `peer-review` | K-Dense-AI/claude-scientific-skills | `skills/peer-review` | `a1043ef544e3` |
| 48 | `scientific-writing` | K-Dense-AI/claude-scientific-skills | `skills/scientific-writing` | `a1043ef544e3` |
| 48 | `statistical-analysis` | K-Dense-AI/claude-scientific-skills | `skills/statistical-analysis` | `a1043ef544e3` |
| 49 | `karpathy-llm-wiki` | Astro-Han/karpathy-llm-wiki | `.` | `eafcc77001e4` |

## Fora desta instalação (decisão de 2026-10-15)

| Item | Motivo |
|---|---|
| 1–5, 7–11, 13–17 | Já ativas na conta claude.ai (`anthropic-skills:*` e `claude-api`); duplicar só gastaria contexto |
| 19 context-mode, 21 claude-mem, 29 n8n-skills, 40 get-shit-done, 50 loki-mode | São plugins que instalam e executam programas/hooks; ficam para decisão individual |
| superpowers: `using-superpowers`, `diagnosing-superpowers` | A primeira obriga acionar skill antes de qualquer resposta (conflita com os gates BEORYS); a segunda só depura o próprio plugin |
| Trail of Bits (85) e científicas (177) | Instalado só um núcleo (3 e 5 skills); o restante pode ser copiado sob demanda do mesmo repositório |

## Licenças

Cada pasta traz a licença do repositório de origem (`LICENSE*` ou `LICENSE.upstream`).
Sem licença declarada na origem (uso pessoal, não redistribuir): `d3-viz`,
`csv-data-summarizer`, `file-organizer`, `notion-*`, `remotion-best-practices`.
Trail of Bits usa CC BY-SA 4.0; VibeSec e claude-skills-marketplace, Apache 2.0.
