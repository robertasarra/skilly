#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Casos de deteccao do marcador de travamento (ADR-003).

Cada caso abaixo ja quebrou o gate na pratica ou existe para impedir que ele
volte a quebrar. Rode antes de mexer em esta_locked():

    python scripts/testar_gate_locked.py

Sai 0 se todos passarem, 1 se algum falhar, listando o que divergiu.
Sem dependencias externas.
"""

import importlib.util
import os
import sys
import tempfile

MARCADOR = "Status: LOCKED"

# (nome, conteudo, deve_travar)
CASOS = [
    (
        "A) cabecalho em negrito, como os modelos escrevem",
        "# Doc\n\n**Status:** LOCKED\n**Atualizado em:** 2026-08-04\n",
        True,
    ),
    (
        "B) cabecalho sem negrito",
        "# Doc\n\nStatus: LOCKED\n",
        True,
    ),
    (
        "C) marcador apenas CITADO em texto explicativo no cabecalho",
        "# Doc\n\n**Status:** ATIVO\n\n> marque com `Status: LOCKED` ao estabilizar\n",
        False,
    ),
    (
        "D) marcador fora do cabecalho (linha 100)",
        "# Doc\n" + ("bla\n" * 100) + "**Status:** LOCKED\n",
        False,
    ),
    (
        "E) documento vivo comum, nao travado",
        "# Doc\n\n**Status:** EM DEFINICAO\n",
        False,
    ),
    (
        "F) campo com espacos irregulares",
        "# Doc\n\n  **Status:**   LOCKED\n",
        True,
    ),
    (
        "G) valor anterior mencionado no proprio campo",
        "# Doc\n\n**Status:** ATIVO (antes era LOCKED)\n",
        False,
    ),
]


def carregar_gate():
    aqui = os.path.dirname(os.path.abspath(__file__))
    alvo = os.path.join(aqui, "verificar_gate_documental.py")
    spec = importlib.util.spec_from_file_location("gate", alvo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main():
    gate = carregar_gate()
    falhas = []
    tmp = tempfile.mkdtemp(prefix="gate-locked-")
    caminho = os.path.join(tmp, "doc.md")

    print("DETECCAO DO MARCADOR DE TRAVAMENTO")
    print("marcador da politica: %r\n" % MARCADOR)

    for nome, conteudo, esperado in CASOS:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        obtido = gate.esta_locked(caminho, MARCADOR)
        ok = obtido == esperado
        if not ok:
            falhas.append((nome, esperado, obtido))
        rotulo = "TRAVADO    " if obtido else "nao travado"
        print("  %s  %s  <-  %s" % ("ok  " if ok else "FALHA", rotulo, nome))

    os.remove(caminho)
    os.rmdir(tmp)

    if falhas:
        print("\n%d caso(s) divergiram:" % len(falhas))
        for nome, esperado, obtido in falhas:
            print("  - %s\n      esperado: %s | obtido: %s"
                  % (nome, esperado, obtido))
        return 1

    print("\nRC=0  (%d casos)" % len(CASOS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
