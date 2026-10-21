# Gates, hash registry e segurança

Os gates são a camada determinística da governança: eles não dependem de a IA lembrar de
verificar. Rode-os; não os descreva como se tivessem rodado.

## Hash registry

```
( ) Arquivos canônicos registrados
( ) Hash atualizado
( ) validate_hash_registry executado
( ) verificar_cobertura_registry.py executado
( ) Cobertura em 100%
```

Cobertura abaixo de 100% significa que existe arquivo canônico fora do registro — ou
seja, um arquivo que pode mudar sem que ninguém perceba. Trate como bloqueio de commit,
não como aviso.

**Falso-stale**: quando um arquivo aparece como divergente mas o conteúdo é idêntico,
verifique normalização de fim de linha (CRLF em ambiente Windows) e encoding antes de
reescrever o registro. Reescrever o hash para "resolver" um falso-stale destrói o sinal.

## Verificação de segredos

```
( ) Nenhum segredo exposto em código
( ) Nenhuma credencial em documentação ou exemplo
( ) Nenhum token em ADR, diário ou HANDOFF
( ) Nenhum .env versionado
( ) verificar_segredos.py executado com RC=0
```

Se um segredo real for encontrado no repositório, a ordem é: **revogar no provedor
primeiro**, depois sanitizar o arquivo com placeholder, depois registrar o incidente.
Sanitizar sem revogar não resolve nada — o histórico do git continua contendo a chave.

Placeholders usam formato explícito e não plausível como valor real:
`<SUA_CHAVE_AQUI>`, `<AWS_SECRET_ACCESS_KEY>`.

Credenciais operacionais moram no gerenciador de segredos, referenciadas por nome no
código. Chaves master e de produção nunca entram em campo de variável de ambiente de
interface web, em nenhuma circunstância.

## Gate documental (BEORYS_GATES.md)

Além dos gates de script, existe o bloqueio documental: para cada **tipo** de alteração,
um conjunto de documentos precisa acompanhar a entrega. Mudança de infraestrutura exige
memorial e matriz; fechamento de pendência exige evidência registrada; mudança de
sequência exige runbook. A política vive em `BEORYS_GATES.md` — leia-a antes de assumir
qual conjunto se aplica.

O que este gate **não** detecta: contradição semântica entre dois documentos ambos
atualizados. Ver `references/coerencia.md`.

## Estado dos gates

Ao reportar, use `RC=0` para gate aprovado e informe o código de retorno real para
falhas — não traduza para "ok" ou "quase". Se um gate não pôde ser executado nesta
sessão, o estado dele é **desconhecido**, não aprovado.

## Política e ativos

O gate documental é distribuído com esta skill em `assets/`:

- `BEORYS_GATES.md` — política normativa (bloco JSON após `<!-- BEORYS-GATE-POLICY -->`)
- `verificar_gate_documental.py` — script que a consome
- `ADR-059-gate-documental.md` — decisão de adoção, com o limite explicitado
- `inicializar_beorys.py` — bootstrap: detecta a convenção e gera a política ajustada
- `INCORPORACAO.txt` — runbook de instalação no repositório

Ao instalar em um repositório novo, rode o bootstrap em vez de editar o JSON à mão — ele
traduz os nomes canônicos para a convenção local e relata os papéis sem documento.
