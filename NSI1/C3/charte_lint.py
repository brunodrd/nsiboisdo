#!/usr/bin/env python3
"""charte_lint.py — vérifie qu'un document Markdown respecte la Charte des documents NSI.

Usage :
    python3 charte_lint.py C7C1.md [C7E1.md ...]

Le script contrôle les règles MÉCANIQUES de la charte (présence d'un emoji,
type d'encadré, attribut width, longueur des lignes de code…). Les règles qui
demandent du jugement (le type d'encadré correspond-il vraiment au rôle ?
le contenu est-il juste ?) restent à la relecture.

Deux niveaux :
    ÉCART   la règle de la charte n'est pas respectée ;
    À VOIR  probable écart, à confirmer à la relecture.
Code de sortie : 0 si aucun écart, 1 sinon.
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Règles de la charte
# ---------------------------------------------------------------------------

TYPES_ENCADRES = {"abstract", "note", "question", "success", "tip",
                  "warning", "danger", "example", "info"}
REPLIES = {"success", "info"}                 # toujours en ???

# mot-clé du titre -> type attendu (§2)
ROLES = [
    (r"^à faire|^activité", "question"),
    (r"^réponse|correction|ce qu'il faut en retenir", "success"),
    (r"^à retenir|objectifs|je sais|^programme", "abstract"),
    (r"^définition|^rappel", "note"),
    (r"^méthode|^détail|^justification|^pourquoi", "tip"),
    (r"hors programme|pour aller plus loin|^vers ", "info"),
    (r"à ne pas confondre", "danger"),
]

EMOJI_TITRE_DOC = {"cours": "📖", "exercices": "✏️", "tp": "🧪", "bilan": "🛠️"}
SECTIONS_FIXES = [  # (motif du titre, emoji imposé)
    (r"^0\.", "🔎"),
    (r"synthèse", "🧠"),
    (r"pour s'entraîner", "📝"),
]
EMOJI_RESERVES = {"🔎": r"^0\.", "🧠": r"synthèse", "📝": r"pour s'entraîner"}
EMOJI_TEXTE_PERMIS = {"👉", "⭐"}            # §3, exceptions
LANGAGES = {"python", "pycon", "text"}
LARGEUR_SVG_MAX = 470

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿⭐⭕⌚⌛⏩-⏺]"
    "️?")

# ---------------------------------------------------------------------------


class Rapport:
    def __init__(self, nom):
        self.nom, self.items = nom, []

    def ecart(self, ligne, section, msg):
        self.items.append((ligne, section, "ÉCART", msg))

    def avoir(self, ligne, section, msg):
        self.items.append((ligne, section, "À VOIR", msg))

    def afficher(self):
        nb_e = sum(1 for i in self.items if i[2] == "ÉCART")
        nb_v = len(self.items) - nb_e
        print(f"\n=== {self.nom} : {nb_e} écart(s), {nb_v} point(s) à voir ===")
        for ligne, section, niv, msg in sorted(self.items):
            print(f"  l.{ligne:<4} {section:<3} {niv:<7} {msg}")
        if not self.items:
            print("  Conforme.")
        return nb_e


def type_document(chemin, lignes):
    nom = chemin.stem.lower()
    for l in lignes:
        if l.startswith("# "):
            for t, e in EMOJI_TITRE_DOC.items():
                if e.rstrip("️") in l:
                    return t
            break
    if re.match(r"c\d+e\d+", nom):
        return "exercices"
    if re.match(r"c\d+c\d+", nom):
        return "cours"
    if "bilan" in nom:
        return "bilan"
    if "tp" in nom:
        return "tp"
    return "cours"


def masquer(texte):
    """Retire du texte courant ce qui n'est pas de la prose."""
    t = re.sub(r"<!--.*?-->", " ", texte)
    t = re.sub(r"(`+).+?\1", " ", t)                # code en ligne
    t = re.sub(r"\$\$.*?\$\$|\$[^$]+\$", " ", t)     # formules
    t = re.sub(r"\]\([^)]*\)", "]", t)              # cibles de liens
    t = re.sub(r"\{[^}]*\}", " ", t)                # attributs
    t = re.sub(r"\+\+[\w+\-]+\+\+", " ", t)         # touches
    return t


def emojis(texte):
    return [m.group(0) for m in EMOJI.finditer(texte)]


def sans_vs(e):
    return e.replace("️", "")


def verifier(chemin):
    lignes = chemin.read_text(encoding="utf-8").split("\n")
    r = Rapport(chemin.name)
    genre = type_document(chemin, lignes)

    en_code = False
    cloture = ""
    bloc_debut = 0
    bloc_numerote = False
    en_yaml = lignes and lignes[0].strip() == "---"
    nb_danger = 0
    cite_lignes = False
    a_linenums = False
    objectifs_ligne = None           # encadré d'objectifs en attente de sa liste
    sections = set()
    precedente, contexte = "", ""
    pycon_signale = 0
    if not any(x.startswith("# ") for x in lignes):
        r.ecart(1, "§3", f"document sans titre de niveau 1 "
                f"(# {EMOJI_TITRE_DOC[genre]} …)")

    for n, l in enumerate(lignes, 1):
        s = l.strip()

        # --- en-tête YAML ---
        if en_yaml:
            if n > 1 and s == "---":
                en_yaml = False
            continue

        # --- blocs de code (§5) ---
        m = re.match(r"^(\s*)(```+|~~~+)\s*(.*)$", l)
        if m and not en_code:
            en_code, cloture, bloc_debut = True, m.group(2), n
            info = m.group(3).strip()
            bloc_numerote = "linenums" in info
            a_linenums |= bloc_numerote
            if info.startswith("{=latex}") or info == "{=latex}":
                r.ecart(n, "§1", "bloc ```{=latex} : visible sur le site ; "
                        "utiliser <!-- latex: … -->")
            elif info.startswith("{"):
                r.ecart(n, "§5", f"attributs pandoc « {info} » : syntaxe MkDocs "
                        "attendue (```python linenums=\"1\")")
            else:
                lang = info.split()[0] if info else ""
                if lang not in LANGAGES:
                    r.avoir(n, "§5", f"bloc de code « {lang or 'sans langage'} » : "
                            "python, pycon ou text attendu")
            continue
        if en_code:
            if m and m.group(2)[0] == cloture[0] and len(m.group(2)) >= len(cloture):
                en_code = False
                continue
            code = l
            if re.match(r"^\s*>>> ", code) and pycon_signale != bloc_debut and \
               re.search(r"```python", lignes[bloc_debut - 1]):
                pycon_signale = bloc_debut
                r.ecart(bloc_debut, "§5", "session interactive (>>>) dans un bloc python : "
                        "utiliser ```pycon")
            contenu = code[len(re.match(r"^\s*", lignes[bloc_debut - 1]).group(0)):]
            if len(contenu) > 79:
                r.avoir(n, "§5", f"ligne de code de {len(contenu)} caractères "
                        "(PEP 8 : 79)")
            hors_chaines = re.sub(r"(['\"]).*?\1", "", code)
            for e in emojis(hors_chaines):
                r.ecart(n, "§3", f"emoji {e} dans le code (hors chaîne affichée)")
            continue

        # --- bloc indenté de 4 espaces hors liste et encadré (§5) ---
        if re.match(r"^ {4,}\S", l) and precedente == "" and \
           not re.match(r"^\s*([-*+]|\d+\.|!!!|\?\?\?|===)", contexte):
            r.ecart(n, "§5", "bloc indenté de 4 espaces : utiliser ```text "
                    "pour un affichage")
            precedente = s
            continue
        if s:
            if not l.startswith(" "):
                contexte = l
        precedente = s

        # --- LaTeX et HTML visibles (§1) ---
        prose = masquer(l)
        if re.search(r"\\[a-zA-Z]{2,}", prose):
            r.ecart(n, "§1", "commande LaTeX visible : la placer dans "
                    "<!-- latex: … -->")
        if re.search(r"<(?!!--)[a-zA-Z/][^>]*>", prose):
            r.ecart(n, "§1", "balise HTML dans le source")

        # --- titres (§3) ---
        mt = re.match(r"^(#{1,6})\s+(.*)$", l)
        if mt:
            niveau, titre = len(mt.group(1)), mt.group(2).strip()
            es = emojis(titre)
            titre_bas = titre.lower()
            num = re.match(r"^(\d+(?:\.\d+)*)\.?\s", re.sub(EMOJI, "", titre).strip())
            if num:
                sections.add(num.group(1))
            if len(es) > 1:
                r.ecart(n, "§3", f"{len(es)} emoji dans un titre (un au plus)")
            if niveau == 1:
                attendu = EMOJI_TITRE_DOC[genre]
                if not titre.startswith(attendu) and \
                   not sans_vs(titre).startswith(sans_vs(attendu)):
                    r.ecart(n, "§3", f"titre de document sans {attendu} ({genre})")
            elif niveau == 2:
                if genre == "exercices":
                    for e in es:
                        if sans_vs(e) != "⭐":
                            r.ecart(n, "§3", f"emoji {e} sur un titre d'exercice "
                                    "(seul ⭐ est admis)")
                else:
                    if not es and not titre_bas.startswith("lexique"):
                        r.ecart(n, "§3", "titre de niveau 2 sans emoji")
                    if es and re.match(EMOJI.pattern + r"\s*\d", titre):
                        r.ecart(n, "§3", "emoji avant le numéro : écrire "
                                "« ## 1. 📚 Titre »")
                    nu = re.sub(r"^[\d.\s]*", "", re.sub(EMOJI, "", titre)).lower()
                    for motif, e in SECTIONS_FIXES:
                        if re.search(motif, titre_bas) or re.search(motif, nu):
                            if sans_vs(e) not in [sans_vs(x) for x in es]:
                                r.ecart(n, "§3", f"section à emoji fixe : {e} attendu")
                    for e in es:
                        motif = EMOJI_RESERVES.get(sans_vs(e))
                        if motif and not (re.search(motif, titre_bas)
                                          or re.search(motif, nu)):
                            r.ecart(n, "§3", f"emoji {e} réservé à une autre section")
            continue

        # --- encadrés (§2) ---
        ma = re.match(r'^(\s*)(!!!|\?\?\?\+?)\s+([\w-]+)(?:\s+"(.*)")?\s*$', l)
        if ma:
            marque, typ, titre = ma.group(2), ma.group(3), ma.group(4)
            if typ not in TYPES_ENCADRES:
                r.ecart(n, "§2", f"type d'encadré « {typ} » hors charte")
            if titre is None or titre.strip() == "":
                r.ecart(n, "§2", "encadré sans titre explicite")
                titre = ""
            for e in emojis(titre):
                r.ecart(n, "§2", f"emoji {e} dans un titre d'encadré")
            if typ in REPLIES and marque == "!!!":
                r.ecart(n, "§2", f"« {typ} » doit être replié (???)")
            if typ == "danger":
                nb_danger += 1
                if nb_danger == 2:
                    r.ecart(n, "§2", "plus d'un encadré danger dans le document")
            tb = titre.lower()
            for motif, attendu in ROLES:
                if re.search(motif, tb) and typ != attendu:
                    r.avoir(n, "§2", f"« {titre} » en {typ} : le rôle suggère "
                            f"{attendu}")
                    break
            if re.search(r"je sais|objectifs", tb):
                objectifs_ligne = n
            continue

        if objectifs_ligne and s:
            if re.match(r"^\d+\.\s", s):
                objectifs_ligne = None
            elif re.match(r"^[-*]\s", s):
                r.ecart(objectifs_ligne, "§2", "objectifs en liste à puces : "
                        "liste numérotée attendue")
                objectifs_ligne = None

        # --- images (§4) ---
        for mi in re.finditer(r"!\[([^\]]*)\]\(([^)\s]+)[^)]*\)(\{[^}]*\})?", l):
            alt, src, attr = mi.group(1), mi.group(2), mi.group(3) or ""
            if "width" in attr:
                r.ecart(n, "§4", f"attribut width sur {src} : à retirer")
            if len(alt) < 40:
                r.avoir(n, "§4", f"texte alternatif court ({len(alt)} car.) pour {src}")
            if not src.startswith("img/"):
                r.ecart(n, "§4", f"{src} : les schémas vont dans img/")
            if not re.match(r"^img/[a-z0-9_]+\.(svg|png)$", src):
                r.avoir(n, "§4", f"{src} : nom en minuscules, chiffres et _ attendu")
            fichier = chemin.parent / src
            if fichier.suffix == ".svg" and fichier.exists():
                tete = fichier.read_text(encoding="utf-8", errors="ignore")[:3000]
                vb = re.search(r'viewBox="[\d.\-]+[\s,]+[\d.\-]+[\s,]+([\d.]+)', tete)
                if vb and float(vb.group(1)) > LARGEUR_SVG_MAX:
                    r.ecart(n, "§4", f"{src} : {float(vb.group(1)):.0f} pt de large "
                            f"(max {LARGEUR_SVG_MAX}) : resserrer le dessin")
            elif fichier.suffix == ".svg":
                r.avoir(n, "§4", f"{src} introuvable : largeur non vérifiée")

        # --- emoji dans le texte (§3) ---
        for e in emojis(masquer(re.sub(r"!\[[^\]]*\]", "", l))):
            if sans_vs(e) not in EMOJI_TEXTE_PERMIS and \
               not re.match(r"^\s*-\s*\[", l):          # liens de « Pour s'entraîner »
                if re.match(r"^\s*\*\*", l):
                    r.ecart(n, "§3", f"emoji {e} sur une ligne en gras : en faire "
                            "un titre ### ou retirer l'emoji")
                else:
                    r.ecart(n, "§3", f"emoji {e} dans le texte courant")

        # --- typographie et vocabulaire (§6) ---
        if re.search(r"(?<![\w$\\])O\(", prose):
            r.ecart(n, "§6", "complexité en texte simple : écrire $\\mathcal{O}(…)$")
        if "§" in prose:
            r.ecart(n, "§6", "renvoi « § » : écrire « section 3 »")
        if re.search(r"\b(l'|un |d'|son |par |à l')index\b", prose, re.I):
            r.avoir(n, "§6", "« index » : le programme dit « indice »")
        if re.search(r"\bchap\.", prose):
            r.ecart(n, "§6", "« chap. » : écrire « chapitre IV »")
        if re.search(r"\bchapitre (?![IVXL]+\b)[A-Z]", prose):
            r.ecart(n, "§6", "renvoi à un chapitre par son nom : écrire « chapitre IV »")
        if re.search(r'"[^"]{2,}"', prose) and \
           not re.match(r"^\s*(!!!|\?\?\?|===)", l):
            r.avoir(n, "§6", "guillemets droits dans le texte : « … » attendus")
        if re.search(r"(?<![\d\s,.])\d{5,}(?![\d])", prose):
            r.avoir(n, "§6", "grand nombre sans espace (10 000)")
        if re.search(r"\blignes?\s+\d+", prose):
            cite_lignes = True

    # --- contrôles globaux ---
    if cite_lignes and not a_linenums:
        r.avoir(1, "§5", "le texte cite des numéros de ligne mais aucun bloc n'a "
                "linenums=\"1\"")

    # renvois internes « section 5.2 » vers une section inexistante
    for n, l in enumerate(lignes, 1):
        for ms in re.finditer(r"\bsection (\d+(?:\.\d+)*)", masquer(l)):
            if sections and ms.group(1) not in sections and \
               not re.search(r"C\d+[CE]\d+,\s*section", l):
                r.avoir(n, "§6", f"renvoi à la section {ms.group(1)} : "
                        "introuvable dans ce document")
    # renvois vers un autre cours : forme « cours C6C1, section 5.2 »
    cache = {}
    for n, l in enumerate(lignes, 1):
        p = masquer(l)
        for mr in re.finditer(r"(C\d+[CE]\d+)\s*(?:,\s*|\(\s*)(section\s+)?(\d+(?:\.\d+)+|\d+)\s*\)?", p):
            cours, mot, num = mr.group(1), mr.group(2), mr.group(3)
            if not mot or not re.search(r"cours\s+" + cours, p):
                r.ecart(n, "§6", f"renvoi « {mr.group(0).strip()} » : écrire "
                        f"« cours {cours}, section {num} »")
            cible = chemin.parent / f"{cours}.md"
            if cible.exists():
                if cours not in cache:
                    cache[cours] = set()
                    for t in cible.read_text(encoding="utf-8").split("\n"):
                        mt = re.match(r"^#{1,6}\s+(.*)$", t)
                        if mt:
                            mn = re.match(r"^(\d+(?:\.\d+)*)\.?\s",
                                          re.sub(EMOJI, "", mt.group(1)).strip())
                            if mn:
                                cache[cours].add(mn.group(1))
                if num not in cache[cours]:
                    r.ecart(n, "§6", f"renvoi vers {cours}, section {num} : "
                            "cette section n'existe pas dans " + cible.name)
                else:
                    r.avoir(n, "§6", f"renvoi vers {cours}, section {num} : "
                            "vérifier que la section dit bien ce qui est annoncé")
    return r.afficher()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = 0
    for nom in sys.argv[1:]:
        total += verifier(Path(nom))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
