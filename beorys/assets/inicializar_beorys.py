#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inicializar_beorys.py — Bootstrap da governanca BEORYS(TM) em um repositorio
Versao: 2.0

Tres modos:

  --detectar   Le a arvore, mapeia papeis de governanca para os arquivos que
               existem de fato e relata as lacunas. Nao escreve nada.

  --montar     Monta a estrutura de governanca em repositorio NOVO: cria os
               documentos vivos ausentes a partir de assets/modelos/, instala
               scripts/verificar_gate_documental.py, registra o ADR do gate com
               numeracao livre e gera BEORYS_GATES.md. Nunca sobrescreve
               documento existente.

  --gerar      So o BEORYS_GATES.md, ajustado a convencao ja existente no
               repositorio (para repos que ja tem documentos vivos com nomes
               proprios).

Uso:
    python inicializar_beorys.py --detectar
    python inicializar_beorys.py --montar --projeto "Nome do Projeto"
    python inicializar_beorys.py --montar --perfil essencial --ci
    python inicializar_beorys.py --gerar --modelo <caminho>/BEORYS_GATES.md

RC:
    0  concluido
    1  papeis essenciais ausentes no repositorio
    3  erro de execucao
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys

MARCADOR = "<!-- BEORYS-GATE-POLICY -->"
DESTINO = "BEORYS_GATES.md"

# papel -> nomes aceitos, em ordem de preferencia
PAPEIS = {
    "estado_retomada": ["ONDE_PARAMOS.md", "CURRENT_STATE.md", "STATUS.md"],
    "diario_trabalho": ["WORK_LOG.md", "DIARIO.md", "CHANGELOG.md"],
    "arquitetura": ["MEMORIAL_DESCRITIVO.md", "PROJECT_CONTEXT.md", "ARCHITECTURE.md"],
    "plano_fases": ["MASTER_IMPLEMENTATION_PLAN.md", "PLANO_MESTRE.md", "ROADMAP.md"],
    "runbook": ["EXECUTION_RUNBOOK.md", "RUNBOOK.md"],
    "pendencias": ["PENDENCIAS_VIVAS.md", "PENDENCIAS.md", "TASK_BOARD.md"],
    "rastreabilidade": ["REQUIREMENTS_TRACEABILITY.md", "MATRIZ_RASTREABILIDADE.md", "SUMARIO.md"],
    "evidencias": ["EVIDENCE_REGISTER.md", "EVIDENCIAS.md"],
    "manual_dev": ["MANUAL_DO_DESENVOLVEDOR.md", "CONTRIBUTING.md", "DEVELOPMENT.md"],
    "acao_humana": ["EXECUCOES_MANUAIS.md", "ACOES_MANUAIS.md"],
    "contrato_ia": ["AGENTS.md", "CLAUDE.md"],
    "handoff": ["HANDOFF.md"],
    "produto": ["README.md"],
}

ESSENCIAIS = ["estado_retomada", "diario_trabalho", "handoff", "produto"]

# o que cada perfil de montagem cria
PERFIS = {
    "essencial": ["estado_retomada", "diario_trabalho", "handoff", "produto",
                  "contrato_ia", "pendencias"],
    "completo": list(PAPEIS.keys()),
}

DIRS_CODIGO = ["src", "app", "server", "client", "lib", "scripts"]
DIRS_INFRA = ["infra", "terraform", ".github/workflows"]
DIRS_DADOS = ["migrations", "drizzle"]
DIRS_TESTE = ["tests", "test", "spec"]


def _saida(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", "replace").decode("ascii"))


def _dir_assets():
    return os.path.dirname(os.path.abspath(__file__))


def _hoje():
    return datetime.date.today().isoformat()


def localizar(nome, raiz):
    for base in ("", "docs", "doc", "documentacao"):
        caminho = os.path.join(raiz, base, nome) if base else os.path.join(raiz, nome)
        if os.path.isfile(caminho):
            return os.path.relpath(caminho, raiz).replace("\\", "/")
    return None


def detectar(raiz):
    encontrados, ausentes = {}, []
    for papel, nomes in PAPEIS.items():
        achado = None
        for n in nomes:
            achado = localizar(n, raiz)
            if achado:
                break
        if achado:
            encontrados[papel] = achado
        else:
            ausentes.append((papel, nomes[0]))
    dirs = [d for d in DIRS_CODIGO + DIRS_INFRA + DIRS_DADOS + DIRS_TESTE
            if os.path.isdir(os.path.join(raiz, d))]
    return encontrados, ausentes, dirs


def relatar(encontrados, ausentes, dirs):
    _saida("BOOTSTRAP BEORYS — DETECCAO")
    _saida("")
    _saida("Documentos vivos encontrados:")
    for papel, caminho in sorted(encontrados.items()):
        _saida("  %-18s %s" % (papel, caminho))
    if ausentes:
        _saida("")
        _saida("Papeis sem documento (criar ou mapear manualmente):")
        for papel, sugestao in ausentes:
            marca = "ESSENCIAL" if papel in ESSENCIAIS else "opcional "
            _saida("  [%s] %-18s sugestao: %s" % (marca, papel, sugestao))
    _saida("")
    _saida("Diretorios detectados: %s" % (", ".join(dirs) or "nenhum"))
    faltam_essenciais = [p for p, _ in ausentes if p in ESSENCIAIS]
    if faltam_essenciais:
        _saida("")
        _saida("RC=1 — papeis essenciais ausentes: %s" % ", ".join(faltam_essenciais))
        return 1
    _saida("RC=0")
    return 0


# ----------------------------------------------------------------- montagem

def _aplicar_variaveis(texto, projeto, adr_id):
    return (texto.replace("{{PROJETO}}", projeto)
                 .replace("{{DATA}}", _hoje())
                 .replace("{{ADR}}", adr_id))


def adr_do_gate(raiz):
    """Id do ADR do gate, se este repositorio ja tiver um. Evita duplicata em
    execucao repetida."""
    pasta = os.path.join(raiz, "docs", "adr")
    if not os.path.isdir(pasta):
        return None
    for nome in sorted(os.listdir(pasta)):
        m = re.match(r"(ADR-\d+)-gate-documental\.md$", nome, re.IGNORECASE)
        if m:
            return m.group(1).upper()
    return None


def proximo_adr(raiz):
    """Menor numero de ADR ainda livre em docs/adr/, formatado ADR-NNN."""
    pasta = os.path.join(raiz, "docs", "adr")
    usados = set()
    if os.path.isdir(pasta):
        for nome in os.listdir(pasta):
            m = re.match(r"ADR-(\d+)", nome, re.IGNORECASE)
            if m:
                usados.add(int(m.group(1)))
    n = 1
    while n in usados:
        n += 1
    return "ADR-%03d" % n


def montar_documentos(raiz, projeto, adr_id, perfil):
    """Cria os documentos vivos ausentes. Nunca sobrescreve o que ja existe."""
    modelos = os.path.join(_dir_assets(), "modelos")
    criados, preservados, sem_modelo = [], [], []

    for papel in PERFIS[perfil]:
        # o papel pode ja estar cumprido pelo nome canonico ou por um alternativo
        existente = None
        for nome in PAPEIS[papel]:
            existente = localizar(nome, raiz)
            if existente:
                break
        if existente:
            preservados.append((papel, existente))
            continue

        canonico = PAPEIS[papel][0]
        modelo = os.path.join(modelos, canonico)
        if not os.path.isfile(modelo):
            sem_modelo.append(canonico)
            continue
        with open(modelo, "r", encoding="utf-8") as f:
            texto = _aplicar_variaveis(f.read(), projeto, adr_id)
        with open(os.path.join(raiz, canonico), "w", encoding="utf-8") as f:
            f.write(texto)
        criados.append(canonico)

    return criados, preservados, sem_modelo


def instalar_gate(raiz, adr_id, com_ci):
    """Posiciona o script do gate, o ADR renumerado e, opcionalmente, a CI."""
    assets = _dir_assets()
    feitos, mantidos = [], []

    os.makedirs(os.path.join(raiz, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(raiz, "docs", "adr"), exist_ok=True)

    # Os dois andam juntos: o workflow chama o teste antes do gate, e o gate
    # confia em esta_locked() para decidir o RC=2. Copiar so um deixa o
    # projeto novo com a CI vermelha no primeiro PR. Ver ADR-003.
    for nome_script in ("verificar_gate_documental.py", "testar_gate_locked.py"):
        destino_script = os.path.join(raiz, "scripts", nome_script)
        rotulo = "scripts/" + nome_script
        if os.path.exists(destino_script):
            mantidos.append(rotulo)
        else:
            shutil.copyfile(os.path.join(assets, nome_script), destino_script)
            feitos.append(rotulo)

    nome_adr = "%s-gate-documental.md" % adr_id
    destino_adr = os.path.join(raiz, "docs", "adr", nome_adr)
    if os.path.exists(destino_adr):
        mantidos.append("docs/adr/%s" % nome_adr)
    else:
        with open(os.path.join(assets, "ADR-059-gate-documental.md"),
                  "r", encoding="utf-8") as f:
            texto = f.read()
        if adr_id != "ADR-059":
            # o modelo nasceu como ADR-059 no repositorio de origem; aqui ele
            # recebe a numeracao livre DESTE repositorio e perde as referencias
            # que so faziam sentido la
            texto = re.sub(r"^# ADR-059 .*$", "# %s — Gate Documental" % adr_id,
                           texto, count=1, flags=re.MULTILINE)
            texto = re.sub(r"^\*\*Relacionado:\*\* .*$", "**Relacionado:** —",
                           texto, count=1, flags=re.MULTILINE)
            texto = re.sub(r"^> Numeração a confirmar[\s\S]*?\n\n", "",
                           texto, count=1, flags=re.MULTILINE)
            texto = texto.replace("ADR-059", adr_id)
        texto = re.sub(r"^\*\*Data:\*\* .*$", "**Data:** %s" % _hoje(),
                       texto, count=1, flags=re.MULTILINE)
        with open(destino_adr, "w", encoding="utf-8") as f:
            f.write(texto)
        feitos.append("docs/adr/%s" % nome_adr)

    if com_ci:
        pasta_ci = os.path.join(raiz, ".github", "workflows")
        os.makedirs(pasta_ci, exist_ok=True)
        destino_ci = os.path.join(pasta_ci, "beorys-gate.yml")
        if os.path.exists(destino_ci):
            mantidos.append(".github/workflows/beorys-gate.yml")
        else:
            shutil.copyfile(os.path.join(assets, "modelos", "workflow-gate.yml"),
                            destino_ci)
            feitos.append(".github/workflows/beorys-gate.yml")

    return feitos, mantidos


# ----------------------------------------------------------------- politica

def gerar(raiz, modelo, encontrados, dirs, forcar, adr_id=None):
    destino = os.path.join(raiz, DESTINO)
    if os.path.exists(destino) and not forcar:
        _saida("ERRO: %s ja existe. Use --forcar para sobrescrever." % DESTINO)
        return 3
    with open(modelo, "r", encoding="utf-8") as f:
        texto = f.read()
    bloco = re.search(r"(" + re.escape(MARCADOR) + r"\s*```json\s*)(.*?)(```)",
                      texto, re.DOTALL)
    if not bloco:
        _saida("ERRO: modelo sem bloco de politica.")
        return 3
    politica = json.loads(bloco.group(2))

    # troca o nome canonico pelo nome real usado neste repositorio
    canonico_por_papel = {p: n[0] for p, n in PAPEIS.items()}
    substituicao = {}
    for papel, caminho in encontrados.items():
        canonico = canonico_por_papel[papel]
        real = os.path.basename(caminho)
        if real != canonico:
            substituicao[canonico] = real

    def troca(lista):
        return [substituicao.get(x, x) for x in lista]

    politica["sempre_exigidos"] = troca(politica.get("sempre_exigidos", []))
    for tipo in politica.get("tipos", []):
        tipo["exige"] = troca(tipo.get("exige", []))
        tipo["padroes"] = troca(tipo.get("padroes", []))
    politica["gerado_em"] = "bootstrap"
    politica["convencao_detectada"] = {p: os.path.basename(c)
                                       for p, c in sorted(encontrados.items())}

    novo = (bloco.group(1) + json.dumps(politica, ensure_ascii=False, indent=2)
            + "\n" + bloco.group(3))
    saida = texto[:bloco.start()] + novo + texto[bloco.end():]
    if adr_id and adr_id != "ADR-059":
        saida = saida.replace("ADR-059", adr_id)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(saida)

    _saida("Gerado: %s" % DESTINO)
    if substituicao:
        _saida("Nomes ajustados a este repositorio:")
        for de, para in sorted(substituicao.items()):
            _saida("  %s -> %s" % (de, para))
    nao_detectados = [t["id"] for t in politica.get("tipos", [])
                      if t["id"] in ("infraestrutura", "schema_dados", "testes")
                      and not any(d.split("/")[0] in " ".join(t["padroes"]) for d in dirs)]
    if nao_detectados:
        _saida("")
        _saida("Revisar padroes destes tipos — diretorio correspondente nao encontrado:")
        for t in nao_detectados:
            _saida("  - %s" % t)
    _saida("RC=0")
    return 0


def montar(raiz, projeto, perfil, com_ci, forcar):
    # repetir a montagem nao pode gerar um segundo ADR do gate nem sobrescrever
    # a politica ja calibrada: reaproveita o que existir
    adr_id = adr_do_gate(raiz) or proximo_adr(raiz)

    _saida("MONTAGEM BEORYS — perfil %s" % perfil)
    _saida("Projeto:     %s" % projeto)
    _saida("ADR do gate: %s" % adr_id)
    _saida("")

    criados, preservados, sem_modelo = montar_documentos(raiz, projeto, adr_id, perfil)
    feitos, mantidos = instalar_gate(raiz, adr_id, com_ci)

    if criados:
        _saida("Documentos vivos criados:")
        for c in criados:
            _saida("  + %s" % c)
    if feitos:
        _saida("")
        _saida("Gate instalado:")
        for f in feitos:
            _saida("  + %s" % f)
    if preservados or mantidos:
        _saida("")
        _saida("Preservado (ja existia, nao foi tocado):")
        for papel, caminho in preservados:
            _saida("  = %-18s %s" % (papel, caminho))
        for m in mantidos:
            _saida("  = %s" % m)
    if sem_modelo:
        _saida("")
        _saida("Sem modelo em assets/modelos (criar a mao):")
        for s in sem_modelo:
            _saida("  ! %s" % s)

    _saida("")
    encontrados, ausentes, dirs = detectar(raiz)
    rc = relatar(encontrados, ausentes, dirs)
    if rc != 0:
        return rc

    _saida("")
    if os.path.exists(os.path.join(raiz, DESTINO)) and not forcar:
        _saida("Politica preservada: %s ja existe (use --forcar para regerar)."
               % DESTINO)
    else:
        rc = gerar(raiz, os.path.join(_dir_assets(), "BEORYS_GATES.md"),
                   encontrados, dirs, forcar, adr_id)
        if rc != 0:
            return rc

    _saida("")
    _saida("PROXIMOS PASSOS (a IA nao faz sozinha)")
    _saida("  1. Escrever o conteudo real de README.md e MEMORIAL_DESCRITIVO.md.")
    _saida("  2. Quebrar o escopo em fases (F00-F13) no plano mestre.")
    _saida("  3. Validar os quatro RC do gate e registrar em EVIDENCE_REGISTER.md:")
    _saida("       python scripts/verificar_gate_documental.py --staged")
    if not com_ci:
        _saida("  4. Ligar o gate na CI (rode de novo com --ci ou adicione a mao).")
    return 0


def main():
    p = argparse.ArgumentParser(description="Bootstrap BEORYS")
    p.add_argument("--raiz", default=".")
    p.add_argument("--detectar", action="store_true")
    p.add_argument("--montar", action="store_true",
                   help="monta a estrutura de governanca em repositorio novo")
    p.add_argument("--gerar", action="store_true")
    p.add_argument("--modelo", default=None)
    p.add_argument("--projeto", default=None,
                   help="nome usado nos cabecalhos (padrao: nome da pasta)")
    p.add_argument("--perfil", choices=sorted(PERFIS.keys()), default="completo")
    p.add_argument("--ci", action="store_true",
                   help="tambem instala o workflow de CI do gate")
    p.add_argument("--forcar", action="store_true")
    a = p.parse_args()

    try:
        if a.montar:
            projeto = a.projeto or os.path.basename(os.path.abspath(a.raiz))
            return montar(a.raiz, projeto, a.perfil, a.ci, a.forcar)

        encontrados, ausentes, dirs = detectar(a.raiz)
        if a.gerar:
            if not a.modelo:
                _saida("ERRO: --gerar exige --modelo")
                return 3
            relatar(encontrados, ausentes, dirs)
            _saida("")
            return gerar(a.raiz, a.modelo, encontrados, dirs, a.forcar)
        return relatar(encontrados, ausentes, dirs)
    except Exception as e:
        _saida("ERRO: %s" % e)
        _saida("RC=3")
        return 3


if __name__ == "__main__":
    sys.exit(main())
