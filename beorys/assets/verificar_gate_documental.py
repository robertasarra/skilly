#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_gate_documental.py — Gate Documental BEORYS(TM)
Versao: 1.0  |  ADR-059

Le a politica normativa do bloco JSON de BEORYS_GATES.md, classifica os arquivos
alterados por tipo e verifica se os documentos vivos exigidos foram tocados na
mesma entrega.

Codigos de retorno:
    0  aprovado
    1  documento obrigatorio ausente
    2  arquivo LOCKED alterado sem ADR
    3  erro de politica ou execucao (estado DESCONHECIDO, nao aprovado)

Sem dependencias externas. Compativel com Windows/CMD e Linux.
"""

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

POLITICA_PADRAO = "BEORYS_GATES.md"
MARCADOR = "<!-- BEORYS-GATE-POLICY -->"


def _saida(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", "replace").decode("ascii"))


def carregar_politica(caminho):
    if not os.path.isfile(caminho):
        raise RuntimeError("politica nao encontrada: %s" % caminho)
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    if MARCADOR not in conteudo:
        raise RuntimeError("marcador %s ausente em %s" % (MARCADOR, caminho))
    depois = conteudo.split(MARCADOR, 1)[1]
    bloco = re.search(r"```json\s*(.*?)```", depois, re.DOTALL)
    if not bloco:
        raise RuntimeError("bloco json da politica nao encontrado apos o marcador")
    try:
        return json.loads(bloco.group(1))
    except ValueError as e:
        raise RuntimeError("json da politica invalido: %s" % e)


def arquivos_alterados(staged, base):
    if staged:
        cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    else:
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMR", "%s...HEAD" % base]
    try:
        saida = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except (subprocess.CalledProcessError, OSError) as e:
        raise RuntimeError("falha ao consultar o git: %s" % e)
    itens = saida.decode("utf-8", "replace").splitlines()
    return [i.strip().replace("\\", "/") for i in itens if i.strip()]


def casa(caminho, padrao):
    if padrao.endswith("/"):
        return caminho.startswith(padrao)
    if fnmatch.fnmatch(caminho, padrao):
        return True
    # "src/**" tambem deve casar com "src/a/b.ts" em qualquer profundidade
    if "**" in padrao:
        prefixo = padrao.split("**", 1)[0]
        if prefixo and caminho.startswith(prefixo):
            return True
    # padrao sem diretorio casa com o basename (ex.: README.md em docs/README.md)
    if "/" not in padrao and os.path.basename(caminho) == padrao:
        return True
    return False


def esta_presente(exigido, alterados, aliases=None):
    candidatos = [exigido] + list((aliases or {}).get(exigido, []))
    for c in candidatos:
        for a in alterados:
            if casa(a, c) or a.endswith("/" + c) or a == c:
                return True
    return False


LINHAS_CABECALHO = 40


def _regex_marcador(marcador):
    """Compila o marcador de travamento como CAMPO de cabecalho.

    O marcador da politica ("Status: LOCKED") declara um campo e o valor que
    trava o arquivo. A deteccao exige que ele apareca em INICIO DE LINHA, como
    campo de verdade, tolerando o negrito markdown com que os modelos escrevem
    o cabecalho ("**Status:** LOCKED") e espacos ao redor.

    Casar o marcador em qualquer posicao da linha nao funciona nos dois
    sentidos: perde o arquivo escrito em negrito (falso negativo, silencioso) e
    trava qualquer documento que apenas CITE o marcador em texto explicativo
    (falso positivo). Ver ADR-003.

    Marcador sem ":" nao declara campo; nesse caso devolve None e a deteccao
    cai no comportamento antigo de substring.
    """
    if ":" not in marcador:
        return None
    campo, valor = marcador.split(":", 1)
    campo, valor = campo.strip(), valor.strip()
    if not campo or not valor:
        return None
    return re.compile(
        r"^[ \t]*\**[ \t]*" + re.escape(campo) +
        r"[ \t]*:[ \t]*\**[ \t]*" + re.escape(valor) + r"\b",
        re.IGNORECASE | re.MULTILINE,
    )


def esta_locked(caminho, marcador):
    if not os.path.isfile(caminho):
        return False
    try:
        with open(caminho, "r", encoding="utf-8", errors="replace") as f:
            cabecalho = "".join([next(f, "") for _ in range(LINHAS_CABECALHO)])
    except OSError:
        return False
    padrao = _regex_marcador(marcador)
    if padrao is None:
        return marcador.lower() in cabecalho.lower()
    return padrao.search(cabecalho) is not None


def avaliar(politica, alterados):
    achados = {"disparados": [], "faltantes": [], "avisos": [], "locked": []}
    aliases = politica.get("aliases", {})

    exigidos_base = politica.get("sempre_exigidos", [])
    for doc in exigidos_base:
        if not esta_presente(doc, alterados, aliases):
            achados["faltantes"].append(("sempre", doc))

    for tipo in politica.get("tipos", []):
        disparou = any(
            casa(a, p) for a in alterados for p in tipo.get("padroes", [])
        )
        if not disparou:
            continue
        achados["disparados"].append(tipo["id"])
        for doc in tipo.get("exige", []):
            if esta_presente(doc, alterados, aliases):
                continue
            if tipo.get("severidade") == "avisa":
                achados["avisos"].append((tipo["id"], doc))
            else:
                achados["faltantes"].append((tipo["id"], doc))

    bl = politica.get("bloqueio_locked", {})
    if bl.get("ativo"):
        padrao_adr = bl.get("exige_adr_em", "docs/adr/ADR-*.md")
        tem_adr = any(casa(a, padrao_adr) for a in alterados)
        for a in alterados:
            if esta_locked(a, bl.get("marcador", "Status: LOCKED")) and not tem_adr:
                achados["locked"].append(a)

    return achados


def relatar(achados, alterados, formato_json):
    if formato_json:
        rc = 2 if achados["locked"] else (1 if achados["faltantes"] else 0)
        print(json.dumps({"rc": rc, "alterados": alterados, **achados},
                         ensure_ascii=False, indent=2))
        return rc

    _saida("GATE DOCUMENTAL BEORYS")
    _saida("Arquivos alterados: %d" % len(alterados))
    _saida("Tipos disparados:   %s" % (", ".join(achados["disparados"]) or "nenhum"))

    if achados["locked"]:
        _saida("")
        _saida("BLOQUEIO — arquivo LOCKED alterado sem ADR na entrega:")
        for a in achados["locked"]:
            _saida("  - %s" % a)
        _saida("")
        _saida("RC=2")
        return 2

    if achados["faltantes"]:
        _saida("")
        _saida("DOCUMENTOS OBRIGATORIOS AUSENTES:")
        for tipo, doc in achados["faltantes"]:
            _saida("  - %-22s exige  %s" % (tipo, doc))

    for tipo, doc in achados["avisos"]:
        _saida("  ! aviso: %s sugere %s" % (tipo, doc))

    _saida("")
    if achados["faltantes"]:
        _saida("RC=1")
        return 1
    _saida("RC=0")
    return 0


def main():
    p = argparse.ArgumentParser(description="Gate documental BEORYS")
    p.add_argument("--politica", default=POLITICA_PADRAO)
    p.add_argument("--staged", action="store_true",
                   help="avalia o que esta em stage (padrao se --base ausente)")
    p.add_argument("--base", default=None,
                   help="referencia de comparacao, ex.: origin/main")
    p.add_argument("--json", action="store_true", dest="formato_json")
    args = p.parse_args()

    try:
        politica = carregar_politica(args.politica)
        usar_staged = args.staged or not args.base
        alterados = arquivos_alterados(usar_staged, args.base or "origin/main")
    except RuntimeError as e:
        _saida("ERRO: %s" % e)
        _saida("RC=3 — estado do gate DESCONHECIDO, nao aprovado")
        return 3

    if not alterados:
        _saida("Nenhum arquivo alterado detectado. RC=0")
        return 0

    return relatar(avaliar(politica, alterados), alterados, args.formato_json)


if __name__ == "__main__":
    sys.exit(main())
