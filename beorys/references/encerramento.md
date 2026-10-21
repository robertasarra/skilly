# Fase 4 — Encerramento de sessão

O encerramento é o que converte trabalho em continuidade. Uma sessão brilhante sem
encerramento equivale, para a sessão seguinte, a uma sessão que não aconteceu.

## Checklist de encerramento

```
( ) Diário da sessão criado
( ) WORK_LOG atualizado
( ) Pendências registradas com ID (abertas e fechadas)
( ) Execuções manuais atualizadas (o que sobrou para a humana fazer)
( ) Evidências registradas com ambiente, commit/run e SHA-256
( ) Matriz de rastreabilidade percorrida coluna a coluna
( ) Documentos de arquitetura tocados se a arquitetura mudou
( ) ONDE_PARAMOS / CURRENT_STATE atualizado
( ) HANDOFF.md atualizado
( ) Revisão de coerência semântica executada (references/coerencia.md)
( ) Hash registry revalidado
( ) Gate documental atendido para o tipo de alteração
( ) Segredos de sessão revogados no provedor
( ) Commit preparado

Use os nomes de arquivo da convenção do repositório em questão — ver
`references/documentos-vivos.md`.
```

## Anatomia do ONDE_PARAMOS

Checkpoint técnico de retomada. Registre o que permite reabrir a sessão sem adivinhação:

```
ONDE PARAMOS — <data>
Branch:        <nome>   PR: <#n>   SHA: <hash curto>
Última entrega: <RUN-xxx / fase>
Testes:        <executados, resultado, evidência>
Bloqueios:     <TEC-xxx / MAN-xxx>
Próximo passo: <RUN-xxx ou pendência única, nomeada>
```

## Anatomia do HANDOFF

O HANDOFF é escrito para uma IA que não viu nada desta sessão. Escreva para essa leitora:

```
HANDOFF — <data>
Onde paramos:     <estado factual, não narrativa>
Próximo passo:    <ação única e concreta>
Pré-requisitos:   <o que precisa estar verdadeiro antes>
Armadilhas:       <o que já falhou aqui e por quê>
Não fazer:        <caminhos já descartados, com o motivo>
```

O campo "Não fazer" é o que mais economiza tempo. Sem ele, a sessão seguinte repete os
becos sem saída desta.

## Lições aprendidas

Registre apenas o que muda comportamento futuro. "Corrigimos o bug" não é lição;
"`pyautogui.typewrite` não funciona no Ergon, usar `WScript.Shell SendKeys` com letras
individuais" é lição. Lição sem consequência operacional é ruído no registro.

## Revogação de credenciais

Chaves criadas para esta sessão: apagar do campo de variável de ambiente **e** revogar no
provedor. Registre a revogação no diário — se não está registrado, a próxima sessão não
sabe se a chave ainda vive.

## Commit

Prepare a mensagem, não execute o push sem confirmação. A mensagem descreve o efeito da
mudança, não o processo de fazê-la:

```
<tipo>(<escopo>): <efeito da mudança>

- ADR-<n> (se houver)
- Gates: <n>/<total> RC=0
- Pendências abertas: <n>
```
