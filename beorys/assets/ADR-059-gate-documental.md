# ADR-059 — Gate Documental (13º gate)

**Status:** PROPOSTO
**Data:** 2026-08-04
**Autor:** Mei (Roberta Sarra)
**Substitui:** —
**Relacionado:** ADR-058 (`verificar_segredos.py`, 12º gate)

> Numeração a confirmar contra `docs/adr/` antes do commit. O último ADR conhecido é o
> 058; se houver ADR intermediário criado depois, renumere este.

## Contexto

A estrutura documental do ecossistema existe e está conectada, mas a sincronização entre
os documentos vivos depende hoje de disciplina de sessão. Quando uma entrega altera
código ou infraestrutura e deixa a documentação para o ciclo seguinte, o repositório
passa a afirmar um estado que já não é o real — e como o repositório é a fonte da
verdade, a sessão seguinte parte de premissa falsa.

Os doze gates existentes verificam propriedades do código, dos segredos e do registro de
hashes. Nenhum deles verifica se a **documentação obrigatória acompanhou a alteração**.

## Decisão

Adotar um 13º gate, `verificar_gate_documental.py`, que:

1. lê a política normativa do bloco JSON de `BEORYS_GATES.md`;
2. classifica os arquivos alterados por tipo de alteração;
3. exige que os documentos vivos correspondentes tenham sido tocados na mesma entrega;
4. bloqueia entregas que alterem arquivo `Status: LOCKED` sem ADR correspondente.

A política vive em **um único lugar** — o bloco JSON de `BEORYS_GATES.md` — e é lida
diretamente pelo script. Não há cópia paralela em YAML ou em código: duas cópias
divergiriam, que é precisamente a falha que o gate existe para prevenir.

## Consequências

**Positivas.** Documentação deixa de depender de memória de sessão. O tipo de alteração
passa a ter consequência documental explícita e auditável. Arquivos LOCKED ganham
proteção mecânica, não apenas convencional.

**Negativas.** Entregas ficam mais lentas: alterar uma linha de código passa a exigir
tocar no registro. O custo é intencional — é o preço da rastreabilidade — mas pode gerar
atualizações protocolares de baixo conteúdo, que o gate não distingue de atualizações
substantivas.

**Limite explícito.** Este gate verifica **atualização conjunta**, não **concordância
semântica**. Dois documentos podem ser atualizados na mesma entrega e continuar se
contradizendo. A revisão de coerência antes do fechamento permanece obrigatória e não é
automatizável por este mecanismo. Registrar este limite aqui evita que o RC=0 seja lido
como garantia de consistência.

## Alternativas consideradas

**Hook de pre-commit local.** Rejeitado como mecanismo único: roda apenas na máquina de
quem tem o hook instalado e é silenciosamente contornável com `--no-verify`. Aceito como
camada adicional opcional, com a CI como autoridade.

**Política em YAML separado.** Rejeitado por criar segunda fonte da verdade sobre a
mesma regra.

**Exigir todos os documentos em toda entrega.** Rejeitado: transformaria a atualização
documental em ritual vazio e destruiria o sinal de quais documentos realmente mudaram.

## Validação

`RC=1` quando código é alterado sem os documentos exigidos; `RC=2` quando arquivo LOCKED
é alterado sem ADR; `RC=0` quando o conjunto está completo; `RC=3` em erro de política ou
de repositório — estado desconhecido, jamais tratado como aprovação.

## Rollback

Remover o passo da CI e mover `BEORYS_GATES.md` para `Status: SUSPENSO`. O script é
inerte sem invocação; nenhum artefato do repositório depende dele em tempo de execução.
