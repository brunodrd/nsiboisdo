"""Exercices 7 à 10 – Coder un texte (C3E5).

Exécutez le fichier pour lancer les tests : décommentez chaque ligne
du bloc final quand la fonction correspondante est écrite.
Le fichier message_latin1.txt doit être dans le même dossier que ce programme.
"""


# ============================================================ Exercice 7
def nb_octets_utf8(car: str) -> int:
    """Renvoie le nombre d'octets utilisés par UTF-8 pour coder le caractère car.

    >>> nb_octets_utf8("é")
    2
    """
    # Comparer ord(car) aux bornes du tableau du cours (0x7F, 0x7FF, 0xFFFF)
    # À COMPLÉTER
    ...


# ============================================================ Exercice 8
def convertir(source: str, encodage_source: str,
              cible: str, encodage_cible: str) -> None:
    """Écrit dans le fichier cible le texte du fichier source,
    lu avec encodage_source et écrit avec encodage_cible."""
    # À COMPLÉTER
    ...


# ============================================================ Exercice 9
def code_utf8(car: str) -> list:
    """Renvoie la liste des octets (entiers de 0 à 255) qui codent
    le caractère car en UTF-8, calculés à l'aide du tableau du cours.

    >>> code_utf8("é")
    [195, 169]
    """
    # n // 64 donne les bits de n sauf les 6 derniers ; n % 64 donne les 6 derniers
    # À COMPLÉTER
    ...


# ============================================================ Exercice 10
def reparer(texte: str) -> str:
    """Répare un texte écrit en UTF-8 mais lu par erreur en ISO-8859-1."""
    # À COMPLÉTER
    ...


# ============================================================ Tests
def caracteres_unicode():
    """Renvoie la liste de tous les points de code que UTF-8 peut coder
    (on exclut U+D800 à U+DFFF, réservés à UTF-16)."""
    return [chr(n) for n in range(0x110000) if not 0xD800 <= n <= 0xDFFF]


def test_nb_octets_utf8():
    assert nb_octets_utf8("A") == 1
    assert nb_octets_utf8("é") == 2
    assert nb_octets_utf8("€") == 3
    assert nb_octets_utf8("\U0001F600") == 4
    for car in caracteres_unicode():
        assert nb_octets_utf8(car) == len(car.encode("utf-8"))


def test_code_utf8():
    assert code_utf8("A") == [0x41]
    assert code_utf8("ç") == [0xC3, 0xA7]
    assert code_utf8("€") == [0xE2, 0x82, 0xAC]
    for car in caracteres_unicode():
        assert code_utf8(car) == list(car.encode("utf-8"))


def test_reparer():
    assert reparer("Ã§a") == "ça"
    assert reparer("L'Ã©tÃ©") == "L'été"


def test_convertir():
    convertir("message_latin1.txt", "latin-1", "message_utf8.txt", "utf-8")
    texte = open("message_utf8.txt", encoding="utf-8").read()
    assert texte == open("message_latin1.txt", encoding="latin-1").read()


if __name__ == "__main__":
    # test_nb_octets_utf8(); print("nb_octets_utf8 : OK")
    # test_convertir(); print("convertir : OK")
    # test_code_utf8(); print("code_utf8 : OK")
    # test_reparer(); print("reparer : OK")
    pass
