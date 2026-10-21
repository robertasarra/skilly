# Fase 2 — Investigação e alteração

Duas etapas encadeadas. A investigação produz o mapa; a alteração só acontece depois que
o mapa fecha. Pular a investigação é o que transforma correção pontual em incidente.

## Protocolo de investigação

```
( ) Problema identificado (sintoma observado, não sintoma relatado)
( ) Arquivos impactados identificados
( ) Dependências identificadas
( ) ADRs impactados identificados
( ) Estratégia de validação definida
( ) Estratégia de rollback definida
```

Distinga sintoma de causa. "A query falha" é sintoma; "a coluna foi lida do código e não
do schema de produção" é causa. Quando houver divergência entre schema de código e schema
real, o schema real vence e a divergência vira pendência — nunca ajuste a leitura para
"caber" na expectativa.

## Protocolo de alteração

Sete perguntas. Responda todas **antes** de escrever a primeira linha:

1. **O que muda?** — escopo exato, arquivo a arquivo
2. **Por que muda?** — necessidade, com evidência CONFIRMADA
3. **Onde muda?** — caminhos completos
4. **O que pode quebrar?** — consumidores, migrations, contratos de API, testes
5. **Como validar?** — comando ou passo concreto, com saída esperada
6. **Como reverter?** — passo de rollback executável, não "reverter o commit"
7. **Onde documentar?** — qual arquivo canônico recebe o registro

Se a resposta 4 for "não sei", a investigação não terminou. Volte.

## Quando parar

Pare e escale ao usuário — sem alterar nada — quando:

- o arquivo alvo estiver `Status: LOCKED`
- a mudança contrariar um ADR vigente sem que um novo ADR a substitua
- a mudança exigir credencial que não deveria estar disponível na sessão
- a alteração cruzar a fronteira entre projetos (ex.: mexer no Ergon "de passagem"
  enquanto se resolve algo do VeritAI)

## Registro do que foi feito

Toda alteração aplicada gera, no mesmo turno: entrada no `WORK_LOG`, atualização do
`CURRENT_STATE` e — se a decisão tiver consequência arquitetural — um ADR novo. ADR não
é burocracia retroativa: é o que impede a sessão seguinte de refazer a mesma discussão
com menos informação.
