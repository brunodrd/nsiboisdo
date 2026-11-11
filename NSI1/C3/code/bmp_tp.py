"""TP « Lire une image octet par octet ».

Le fichier logo.bmp doit être dans le même dossier que ce programme.
Exécutez le fichier pour lancer les tests : décommentez chaque ligne
du bloc final quand la fonction correspondante est écrite.
"""


# ============================================================ Partie 3 (fourni)
def compter_couleurs(nom_fichier: str) -> int:
    """Renvoie le nombre de couleurs différentes d'une image BMP
    à 24 bits par pixel, sans remplissage en fin de ligne."""
    donnees = open(nom_fichier, "rb").read()
    debut = donnees[10] + 256 * donnees[11]
    couleurs = []
    for i in range(debut, len(donnees), 3):
        pixel = donnees[i:i + 3]
        if pixel not in couleurs:
            couleurs.append(pixel)
    return len(couleurs)


# ============================================================ Partie 4
def entier_petit_boutiste(donnees: bytes, debut: int, nb_octets: int) -> int:
    """Renvoie l'entier naturel écrit en petit-boutiste dans les nb_octets
    octets de donnees qui commencent à la position debut.

    >>> entier_petit_boutiste(bytes([0x3A, 0x6D, 0x1C, 0x00]), 0, 4)
    1862970
    """
    # 1. Vérifier avec assert que les octets demandés sont dans donnees
    # 2. L'octet n° i (en partant de debut) a pour poids 256 ** i
    # À COMPLÉTER
    ...


def informations(nom_fichier: str) -> tuple:
    """Renvoie le triplet (largeur, hauteur, bits par pixel)
    de l'image BMP nom_fichier."""
    donnees = open(nom_fichier, "rb").read()
    assert donnees[0:2] == b"BM", "ce n'est pas un fichier BMP"
    # À COMPLÉTER avec entier_petit_boutiste et le tableau de l'en-tête
    ...


# ============================================================ Partie 5
def negatif(nom_source: str, nom_resultat: str) -> None:
    """Écrit dans nom_resultat le négatif de l'image BMP nom_source."""
    donnees = bytearray(open(nom_source, "rb").read())
    # À COMPLÉTER : remplacer chaque octet v des pixels par 255 - v
    open(nom_resultat, "wb").write(donnees)


# ============================================================ Tests
def test_entier_petit_boutiste():
    assert entier_petit_boutiste(bytes([0x3A, 0x6D, 0x1C, 0x00]), 0, 4) == 1862970
    assert entier_petit_boutiste(bytes([0x7C, 0x59, 0x1A]), 0, 3) == 0x1A597C
    # À COMPLÉTER : ajouter au moins deux tests


def test_informations():
    largeur, hauteur, bits = informations("logo.bmp")
    # À COMPLÉTER : vérifier les valeurs trouvées dans les parties 2 et 3,
    # puis la relation taille = début des pixels + largeur × hauteur × bits / 8


if __name__ == "__main__":
    print("nombre de couleurs :", compter_couleurs("logo.bmp"))
    # test_entier_petit_boutiste(); print("entier_petit_boutiste : OK")
    # test_informations(); print("informations : OK")
    # negatif("logo.bmp", "logo_negatif.bmp")
