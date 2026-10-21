#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida cada skill deste repositorio antes que ela vire upload.

As regras abaixo nao sao estilo: sao os limites que o claude.ai aplica no
envio. Uma skill que os viola e RECUSADA na interface, e a mensagem de erro
chega tarde — depois de voce montar o zip, abrir o navegador e enviar.

Rodar:

    python scripts/validar_skills.py

Sai 0 se todas passarem, 1 se alguma falhar. Sem dependencias externas.
"""

import io
import os
import re
import sys

# Limites do claude.ai para skills personalizadas.
NOME_MAX = 64
DESC_MAX = 1024
NOME_PADRAO = re.compile(r"^[a-z0-9-]+$")
NOME_RESERVADO = ("anthropic", "claude")

IGNORAR = {".git", ".github", "scripts", "docs"}

# Nao entram na contagem: sao gerados, e o .gitignore ja os exclui. Contar
# arquivo que nao vai no zip faz o numero divergir do que a interface do
# claude.ai mostra depois do upload.
NAO_CONTAR_DIR = {"__pycache__"}
NAO_CONTAR_EXT = (".pyc", ".pyo")


def contar_arquivos(caminho):
    total = 0
    for raiz, dirs, arquivos in os.walk(caminho):
        dirs[:] = [d for d in dirs if d not in NAO_CONTAR_DIR]
        total += sum(1 for a in arquivos if not a.endswith(NAO_CONTAR_EXT))
    return total


def skills_do_repo(raiz):
    for nome in sorted(os.listdir(raiz)):
        caminho = os.path.join(raiz, nome)
        if not os.path.isdir(caminho) or nome in IGNORAR or nome.startswith("."):
            continue
        yield nome, caminho


def frontmatter(texto):
    """Devolve (dict, erro). Aceita apenas o bloco --- ... --- no topo."""
    if not texto.startswith("---"):
        return None, "SKILL.md nao comeca com o bloco --- do frontmatter"
    partes = texto.split("---", 2)
    if len(partes) < 3:
        return None, "frontmatter nao fechado (falta o segundo ---)"
    campos = {}
    for linha in partes[1].splitlines():
        if ":" in linha and not linha.startswith(" "):
            chave, valor = linha.split(":", 1)
            campos[chave.strip()] = valor.strip()
    return campos, None


def validar(nome_pasta, caminho):
    """Devolve lista de problemas. Lista vazia = passou."""
    problemas = []
    skill_md = os.path.join(caminho, "SKILL.md")

    if not os.path.isfile(skill_md):
        return ["falta SKILL.md"]

    texto = io.open(skill_md, encoding="utf-8").read()
    campos, erro = frontmatter(texto)
    if erro:
        return [erro]

    nome = campos.get("name", "")
    desc = campos.get("description", "")

    if not nome:
        problemas.append("frontmatter sem campo 'name'")
    else:
        if len(nome) > NOME_MAX:
            problemas.append("name tem %d caracteres (maximo %d)"
                             % (len(nome), NOME_MAX))
        if not NOME_PADRAO.match(nome):
            problemas.append("name %r: so minusculas, numeros e hifens" % nome)
        for reservado in NOME_RESERVADO:
            if reservado in nome.lower():
                problemas.append("name contem palavra reservada %r" % reservado)
        if nome != nome_pasta:
            problemas.append("name %r difere do nome da pasta %r — no terminal o "
                             "comando vem da PASTA, e a divergencia confunde"
                             % (nome, nome_pasta))

    if not desc:
        problemas.append("frontmatter sem campo 'description' — sem ele o Claude "
                         "nunca aciona a skill sozinho")
    elif len(desc) > DESC_MAX:
        problemas.append("description tem %d caracteres (maximo %d)"
                         % (len(desc), DESC_MAX))

    return problemas


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills = list(skills_do_repo(raiz))

    if not skills:
        print("Nenhuma skill encontrada em %s" % raiz)
        return 1

    print("VALIDACAO DAS SKILLS")
    print("limites do claude.ai: name <= %d, description <= %d\n"
          % (NOME_MAX, DESC_MAX))

    falhas = 0
    for nome_pasta, caminho in skills:
        problemas = validar(nome_pasta, caminho)
        arquivos = contar_arquivos(caminho)
        if problemas:
            falhas += 1
            print("  FALHA  %-24s (%d arquivos)" % (nome_pasta, arquivos))
            for p in problemas:
                print("           - %s" % p)
        else:
            print("  ok     %-24s (%d arquivos)" % (nome_pasta, arquivos))

    print("")
    if falhas:
        print("%d skill(s) reprovaram — seriam recusadas no upload." % falhas)
        return 1
    print("RC=0  (%d skill(s))" % len(skills))
    return 0


if __name__ == "__main__":
    sys.exit(main())
