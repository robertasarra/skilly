# Fase 1 — Abertura de sessão

Objetivo: reconstruir o estado real do projeto antes de opinar sobre qualquer coisa.
Nenhuma recomendação técnica é emitida antes desta fase terminar.

## Regra Zero

Antes de responder qualquer pergunta sobre o projeto, consulte o repositório. Se o
repositório não estiver acessível nesta sessão, **declare isso na primeira resposta** e
classifique tudo o que vier depois como PROVÁVEL ou HIPÓTESE.

## Checklist de abertura

```
( ) Identidade Git confirmada
( ) PROJECT_CONTEXT.md lido
( ) docs/CURRENT_STATE.md lido
( ) docs/HANDOFF.md lido
( ) docs/SUMARIO.md lido
( ) Último diário lido
( ) Pendências abertas lidas
( ) Política de segurança / LGPD lida
( ) MEMORY.md lido (se existir)
( ) verificar_cobertura_registry.py executado
( ) Lacunas encontradas corrigidas ou registradas
```

## Como reportar a abertura

Após a leitura, devolva um bloco curto de situação — não um resumo dos arquivos, mas o
estado operacional que eles descrevem:

```
ESTADO DA SESSÃO
Projeto:        <nome>
Branch:         <branch>  |  Build: <n>
Último diário:  <data> — <assunto>
Pendências:     <n> abertas  (<as 3 mais críticas>)
Gates:          <n>/<total> em RC=0
Cobertura hash: <%>
Bloqueios:      <o que impede avançar hoje>
```

Se algum item do checklist não pôde ser cumprido, liste-o explicitamente como lacuna em
vez de omiti-lo. Uma abertura com 8 de 11 itens declarados é utilizável; uma abertura
que finge estar completa não é.

## Multi-IA

Quando o projeto é tocado por mais de um assistente, a abertura ganha um passo: verifique
se o último diário e o HANDOFF foram escritos por outra IA e se as regras LOCKED mudaram
desde então. Divergência entre o que a sessão anterior registrou e o que o código mostra
é o sintoma clássico de drift — trate como achado prioritário.
